import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from scipy.stats import weibull_min
from scipy.stats import lognorm
from scipy.special import gamma
from scipy.special import gammainc
from scipy.integrate import quad
from scipy.optimize import minimize
from statsmodels.distributions.empirical_distribution import ECDF
from scipy.stats import chisquare
from sklearn.model_selection import train_test_split
import netCDF4 as nc
import xarray as xr
from tqdm import tqdm
import warnings
from matplotlib.colors import LinearSegmentedColormap
import cartopy
from shapely.geometry import Point
from math import cos, sin, asin, sqrt, radians
import cartopy.crs as ccrs
from shapely.geometry import Point
from shapely.ops import nearest_points
from geopy.distance import geodesic
from cartopy.feature import NaturalEarthFeature
from global_land_mask import globe


coastline_feature = NaturalEarthFeature(
    category='physical', name='coastline', scale='10m',
    facecolor='none')


# -----------------------------------------------------------------------------------------
# **********************************Access Modelling***************************************
# -----------------------------------------------------------------------------------------

class Discrete_Model:
    '''
    Class using a Discrete Time Markov Chain to calculate offshore accessibility statistics
    '''

    def __init__(self, data, H_th, t_req, method='Access'):
        '''
        @param data: csv, dataframe with datetime column labelled 'Time' and waveheight labelled 'H'
        @param H_th: float, wave height in metres
        @param t_req: int, required time to carry out operation in hours
        @param method: str, choice of 'Access' or 'Weather' to determine which states are being modelled
        '''
        # Initialise input variables to be class attributes
        self.H_th = H_th
        self.data = data
        self.t_req = t_req
        self.method = method

        # Run set-up functions
        self.data_setup()
        self.calculate_probs()

        # Calculate the outputs using defined class functions
        self.P_0 = np.mean(self.states)
        self.ed_total = self.calc_expected_delay(self.t_req)

    # -----------------------------------------------------------------------------------------------------
    # Initialisation functions
    # -----------------------------------------------------------------------------------------------------
    def data_setup(self):
        '''
        Sets up data sets for storm times and calm times to fit Weibulls
        '''

        df = self.data

        # Set up boolean column of whether weather conditions are stormy (if threshold wave height exceeded)
        df['Storm'] = df.H >= self.H_th

        # Calculate probabilities of each weather state as the proportion of time spent in each state
        self.P_s = np.mean(df.Storm)
        self.P_c = 1 - self.P_s

        # Define the time required to carry out op.
        T = self.t_req

        # Initialise a vector of ones for instant access
        instant_access = np.ones(len(df) - T)
        # For each time i...
        for i in range(len(df) - T):
            # For each of the next T time steps after time i...
            for j in range(T):
                # ...if time i+j is stormy there's no access at time i so set access status=0 and move to next time
                if df.Storm[i + j]:
                    instant_access[i] = 0
                    break
                # otherwise we complete T consecutive calm period and keep state as 1

        # Append 0s to the end of instant_access list to equalize length with data
        df['instant_access'] = list(instant_access) + [0] * T

        # Define states attribute to be weather or accessibility state dependent on chosen method
        self.states = df.Storm if self.method == 'Weather' else [int(d) for d in instant_access]
        self.instant_access = [int(d) for d in instant_access]

        # Define n to be number of recorded time steps
        n = len(df)
        # Define zero vector to store delay times
        delay = np.zeros(n)
        # For each time i backwards from second to last time...
        for i in range(n - 2, -1, -1):
            # If access hasn't yet occurred increment delay time by 1 from next chronological element
            if df.instant_access[i] == 0:
                delay[i] = delay[i + 1] + 1
            # Otherwise reset delay to 0 as we have access at that point
            else:
                delay[i] = 0

        # Insert delays as a column in the dataframe
        df['delay'] = delay

        # Redefine data attribute with updated dataframe
        self.data = df

        # Locate last access point as points after this are considered censored in terms of delay
        last_access = df[df['instant_access'] == 1].index[-1]
        # Set class attribute as list of delay times.
        self.delays = list(df.delay[:last_access])

    def calculate_probs(self):
        '''
        Calculate transition matrix and stationary probabilities for DTMC
        '''
        # Calculate transition matrix as observed probs
        self.m = transition_matrix(self.states)
        # Calculate stationary probabilities as eigenvector of the transition matrix
        self.pi = np.linalg.eig(self.m)[1][0]

    def calc_P_0(self, T=None, return_states=False):
        '''
        Calculate instant_access probability
        '''

        # If no time selected set T to be the initial input required op time
        if T == None:
            T = self.t_req

        # Convert T from float to integer to use as index
        T = int(T)

        # Copy data
        df = self.data

        # If using Weather chain...
        if self.method == 'Weather':
            # ...calculate instant access probability as chance of calm state*chance of staying for T-1 consecutive
            p = self.P_c * self.m[0][0] ** (T - 1)

        # Otherwise using Access chain...
        else:
            # Calculate as mean of observed instant access (equivalent to calc through Markov chain)
            if T == self.t_req:
                instant_access = self.instant_access
            else:
                instant_access = np.ones(len(self.data) - T)
                # For each time i...
                for i in range(len(self.data) - T):
                    # For each of the next T time steps after time i...
                    for j in range(T):
                        # ...if time i+j is stormy there's no access at time i so set access status=0 and move to next time
                        if self.data.Storm[i + j]:
                            instant_access[i] = 0
                            break
                        # otherwise we complete T consecutive calm period and keep state as 1

            # Calculate p as the mean of instant access (proportion spent in state 1)
            p = np.mean(instant_access)
            if np.isnan(p):
                p = 0
            # Return tuple including states if return_states=True
            if return_states:
                ret = (p, instant_access)
            else:
                ret = p

        return ret

    def calc_expected_delay(self, T=None):
        '''
        Calculated expected delay time
        '''
        # If no T inputted use original input op time
        if T == None:
            T = self.t_req

        # If using weather method...
        if self.method == 'Weather':
            # ... solve simultaneous equations of recursive expected times (see notes)

            # Set up transition probs
            P_cc = self.m[0][0]
            P_cs = self.m[0][1]
            P_sc = self.m[1][0]
            P_ss = self.m[1][1]

            # Set vectors b and x as defined in simultaneous equations
            b = [1] * T
            x = np.zeros(T)

            # Set TxT identity matrix
            a = np.eye(T)
            # Convert to the matrix A in defined simultaneous equations
            a[:, 0] = np.array([1 - P_ss] + [-P_cs] * (T - 1))
            s = np.arange(len(a))
            a[s[:-1], s[1:]] = [-P_cc] * (T - 1)
            a[0, 1] = -P_sc

            # Solve equations
            x = np.linalg.solve(a, b)
            # Return expected delay as sum of product of exp wait from each state weighted by their resp starting prob
            ed = self.P_c * x[0] + self.P_s * x[1]
            return ed
        else:
            # Otherwise if using Access method multiply expected wait time from state 0 (1/P0,1) by its starting prob
            # If T is originally inputted operation. time use existing attributes
            if T == self.t_req:
                ed = (1 - np.mean(self.states)) / self.m[0][1]
                return ed
            else:
                # Otherwise recalculate states and probability to calculate
                (p, states) = self.calc_P_0(T, return_states=True)
                states = [int(d) for d in states]
                m = transition_matrix(states)
                ed = (1 - np.mean(states)) / m[0][1]
                return ed

    def time_effect(self, Ts, plot='Scatter'):
        '''
        Compare access probability and delay times for varying operation time
        '''
        # Set up 2 empty subplots
        fig, ax = plt.subplots(1, 2, figsize=(15, 2.5))
        # On first set of axes...
        sca = ax[0]
        # Calculate access prob for each operation time
        prob = [self.calc_P_0(t) for t in Ts]
        # Plot operation time against prob
        # If plot option is scatter produce scatter plot
        if plot == 'Scatter':
            sca.scatter(Ts, prob, s=5)
        # Otherwise line plot
        else:
            sca.plot(Ts, prob, 'k--')
        # Set x limit to maximum operation time
        sca.set_xlim(min(Ts), max(Ts))
        # Label x and y axes
        sca.set(xlabel=r'Required Access Window, $t$ (h)', ylabel='Probability of Instant Access')
        # Add grid
        plt.grid()

        # On second set of axes...
        sca = ax[1]
        # Calculate expected delay for each operation time
        ed = [self.calc_expected_delay(t) for t in Ts]
        # Plot operation time against expected delay
        # If option is scatter produce scatter plot
        if plot == 'Scatter':
            sca.scatter(Ts, ed, s=5)
        # Otherwise line plot
        else:
            sca.plot(Ts, ed, 'k--')
        # Set x axis limit to be the maximum operation time
        sca.set_xlim(min(Ts), max(Ts))
        # Label x and y axes
        sca.set(xlabel=r'Required Access Window, $t$ (h)', ylabel='Expected Delay (h)')
        plt.grid()

    def CIs(self, val='Delay', opt='Markov', remove_extremes=False, alpha=0.05, split=1, delay_method='Obs'):
        '''
        Calculate extreme values
        '''
        # Transition matrix
        m = self.m
        # Data set
        data = self.data
        # States of access
        states = data.instant_access
        # Standard normal alpha%/1-alpha% quantile
        z = norm.ppf(1 - alpha)
        # Size of dataset
        n = len(data)

        def markov_m_CI(states, m, alpha=0.05, i=0, j=1):
            '''
            Calculate CI for transition matrix probabilities
            '''
            # Define original transition prob
            p_ij = m[i][j]
            # Calculate total number of state i
            f = np.sum(states) if i == 1 else len(states) - np.sum(states)
            # Calculate normal quantile
            z = norm.ppf(1 - alpha / 2)
            # Calculate lower and upper CI limit as defined by Crow (1979)
            lower = p_ij - z * np.sqrt((p_ij * (1 - p_ij)) / f)
            upper = p_ij + z * np.sqrt((p_ij * (1 - p_ij)) / f)
            # Flip CI if lower limit is higher than upper limit
            if lower > upper:
                (lower, upper) = (upper, lower)
            return lower, upper

        def markov_p_CI(states, m, alpha=0.05):
            '''
            Calculate CI for base probabilities of state 1 (probability of instant access)
            '''
            # Define normal quantile
            z = norm.ppf(alpha / 2)
            # Calculate number of accessible states
            S = np.sum(states)
            # Calculate point estimate for prob of instant access as mean proportion of time spent in state 1
            p_hat = np.mean(states)
            # Calculate the product-moment correlation coefficient between adjacent states
            theta_hat = (m[1][1] - p_hat) / (1 - p_hat)

            # For small values of P_0 or P_1 calculate the Anderson-Burstein CI as...
            if p_hat < 0.1 or p_hat > 0.9:
                # Define the adjustment factor
                d = 0.5
                # Calculate Pearson-Hartley Poisson CI lower and upper limits (Pearson and Hartley 1966)
                L = S - z * np.sqrt(S / n)
                U = S + z * np.sqrt(S / n)
                # Calculate the Modified Anderson-Burstein CI using base Pearson-Hartley Poisson CI (Crow 1979)
                p_ui = U / (n + d + 0.5 * (U - S))
                p_li = L / (n - 0.5 * (S - 1 - L))
                # Calculate adjusted MAB interval for improved accuracy (Bedrick and Aragon 1989)
                lower = p_hat - (p_hat - p_li) * (1 + 2 * theta_hat / (1 - theta_hat)) ** 0.5 * (1 - p_hat) ** 0.5 / (
                            1 - 0.5 * p_hat)
                upper = p_hat + (p_ui - p_hat) * (1 + 2 * theta_hat / (1 - theta_hat)) ** 0.5 * (1 - p_hat) ** 0.5 / (
                            1 - 0.5 * p_hat)

            # For all other values of P_0 & P_1 calculate the CI using the Crow pivotal sample proportion method...
            else:
                # Calculate statistic h as a function of product moment correlation coefficient
                h = 1 + 2 * theta_hat / (1 - theta_hat) * (1 - (1 - theta_hat ** n) / (n * (1 - theta_hat)))
                # Calculate lower and upper CI using sample proportion method (Crow 1979)
                lower = (S + 0.5 * z ** 2 + (
                            0.5 + z * np.sqrt(h * (S + 0.5 - (S + 0.5) ** 2 / n + 0.25 * z ** 2 * h)))) / (
                                    n + z ** 2 * h)
                upper = (S - 0.5 * z ** 2 + (
                            0.5 + z * np.sqrt(h * (S - 0.5 - (S - 0.5) ** 2 / n + 0.25 * z ** 2 * h)))) / (
                                    n + z ** 2 * h)

            # Flip CI if lower limit is greater than upper limit
            if lower > upper:
                (lower, upper) = (upper, lower)

            return (lower, upper)

        def markov_delay_CI(data, m, alpha=0.05, remove_extremes=False, delay_method='Obs'):
            '''
            Calculate CI for Expected Delay
            '''
            # Calculate 1-alpha% standard normal quantile
            z = norm.ppf(1 - alpha)
            # Define states of accessibility
            states = data.instant_access
            # Calculate the confidence interval of instant access probabability
            p_ci = markov_p_CI(states, m, alpha)
            m_ci = markov_m_CI(states, m)
            n = len(data)

            # Calculate expectation and variance of p using confidence interval
            exp_p = 1 - np.mean(p_ci)
            se_p = np.diff(p_ci)[0] / (2 * z)
            var_p = np.var(states)
            print(f'Var p: {var_p}')
            print(f'Exp p: {exp_p}')
            # If using Taylor approach, calculate lambda in terms of the transition probability m...
            if delay_method == 'Taylor':
                # Calculate expectation and variance of m using confidence interval
                exp_m = (m_ci[1] + m_ci[0]) / 2
                var_m = ((m_ci[1] - m_ci[0]) / (2 * z)) ** 2 * len(data) ** 2
                # Use Taylor series approximations to calculate the expectation and variance of lambda (1/m)
                exp_lambda = 1 / exp_m
                var_lambda = 1 / ((1 - exp_m) ** 4) * var_m
                print(f'Var m: {var_m}')
                print(f'Exp m: {exp_m}')
                print(f'Var lam: {var_lambda}')
                print(f'Exp m: {exp_lambda}')
            # If using observed data instead of approximation...
            elif delay_method == 'Obs':
                # Define data as list of expected wait times from inaccessible states
                d = data[data['Storm'] == 0].delay[:data[data['instant_access'] == 1].index[-1]]
                # If dataset heavily affected by outliers can opt to remove (remove data points further than 2 s.ds away)
                if remove_extremes:
                    d = remove_outliers(d)
                # Calculate expectation and variance of lambda from observed data
                exp_lambda = np.mean(d)
                var_lambda = np.var(d)
            else:
                print('INVALID METHOD FOR DELAY CI CALCULATION')

            # Combine variances using Taylor series method (Wolter 2006)
            var_c = var_p * var_lambda + var_p * exp_lambda ** 2 * var_lambda * exp_p ** 2
            # Define centre of confidence interval as the expected calculated value
            centre = self.ed_total
            # If applying CI to a smaller future set variance is in terms of a smaller data length
            if split != 1:
                n = n * (1 - split) / split
            # Calculate standard error using variance estimator
            se = np.sqrt(var_c / n)
            # Define upper and lower CI limits
            lower = pos(centre - z * se)  # Define as positive (i.e. above 0) since negative delay not possible
            upper = pos(centre + z * se)

            # Flip CI if lower limit is greater than upper limit
            if lower > upper:
                (lower, upper) = (upper, lower)
            return (lower, upper)

        # If using Markov method...
        if opt == 'Markov':
            # If calculating CI for delay time...
            if val == 'Delay':
                # Calulate delay CI
                return markov_delay_CI(data, m, alpha, remove_extremes, delay_method)
            # Otherwise calculating CI for prob of instant access...
            else:
                # Calculate p_0 CI
                return markov_p_CI(states, m, alpha)
        # Otherwise calculate empirically...
        else:
            # If calculating delay CI...
            if val == 'Delay':
                # Calc delay CI using sample mean and variance
                u = np.mean(self.delays)
                v = np.var(self.delays)
                return (u - z * np.sqrt(v / n), u + z * np.sqrt(v / n))
            # Otherwise calculating instant access prob CI...
            else:
                # Calc instant access prob CI using sample mean and variance
                u = np.mean(states)
                v = np.var(states)
                return (u - z * np.sqrt(v / n), u + z * np.sqrt(v / n))

    def empirical(self, T=None, H=None, remove_extremes=False):
        '''
        Calculate the empirical access probability and expected delay
        '''
        # Set T_req and H_th as original inputs if not specified for function
        if T == None:
            T = self.t_req
        if H == None:
            H = self.H_th

        # Calculate P_0 as the mean of instant access status (proportion spent in state 1)
        P_0 = np.mean(self.instant_access)

        # If extreme values problematic in data set...
        if remove_extremes:
            # ...remove delay times more than 2 standar deviations from mean delay time
            delays = remove_outliers(self.delays)
        else:
            # otherwise use all delay times
            delays = self.delays

        # Calculate mean delay time
        ed_total = np.mean(delays)

        return (P_0, ed_total)



# -----------------------------------------------------------------------------------------
# **********************************Plotting Functions*************************************
# -----------------------------------------------------------------------------------------
def heatmap(df, variable):
    """
    Creates geospatial heatmap of variable
    :param df: dataframe with columns 'Latitude', 'Longitude', and variable
    :param variable: string with variable name
    :return: None
    :output: plotted heatmap
    """
    lons = df['Longitude']
    lats = df['Latitude']
    values = df[variable]
    # Create a custom colormap ranging from yellow to red
    colors = [(1, 1, 0), (1, 0, 0)]  # Yellow to red
    cmap_name = 'yellow_red'
    n_bins = 100  # Number of bins
    cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)

    # Create a figure and axis with Cartopy projection
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

    # Plot the hexbin heatmap with the custom colormap
    hb = ax.hexbin(lons, lats, C=values, gridsize=30, cmap=cmap, transform=ccrs.PlateCarree())
    ax.set_xlim(np.min(lons), np.max(lons))
    ax.set_ylim(np.min(lats), np.max(lats))

    # Add colorbar
    cbar = plt.colorbar(hb, ax=ax, orientation='vertical', shrink=0.8)
    cbar.set_label(variable)
    ax.add_feature(cartopy.feature.LAND, facecolor='white', zorder=2)
    ax.coastlines()
    # Add coastlines
    # Add title
    # plt.title(variable)

    # Show the plot
    plt.show()

# -----------------------------------------------------------------------------------------
# **********************************Helper Functions****************************************
# -----------------------------------------------------------------------------------------
def remove_outliers(d):
    '''
    Removes elements in data more than 2 standard deviations away from sample mean
    '''
    u = np.mean(d)
    s = np.std(d)
    return [el for el in d if np.abs(el - u) < 2 * s]


def pos(num):
    '''
    Returns positive part of a real number
    '''
    return num if num > 0 else 0


def transition_matrix(states, num_states=2):
    '''
    Calculate observed transition matrix
    '''
    # Define number of states
    n = num_states

    # Make square matrix
    M = [[0] * n for i in range(n)]

    # For pairs of elements and future elements...
    for (i, j) in zip(states, states[1:]):
        # ...increment transition matrix to create frequency matrix of transitions
        M[i][j] += 1

    # For each row...
    for row in M:
        # Sum the row...
        s = sum(row)
        # Assuming row is nonzero...
        if s > 0:
            # Divide frequencies by row sums to get probability matrix
            row[:] = [f / s for f in row]
    return M



def distance_to_coast(lon, lat):
    """
    Calculates euclidean distance in kilometres from coordinates to closet point on land
    :param lon: longitudinal coordinate of location
    :param lat: latitudinal coordinate of location
    :return: distance in kilometres to closest point on land
    """
    pt = Point(lon, lat)
    buffered_pt = pt.buffer(1) # Adjust buffer size as needed

    # Find the nearest point on the coastline
    nearest_coast_point = None
    min_distance = float('inf')
    for geometry in coastline_feature.geometries():
        for point in geometry.coords:
            coast_point = Point(point[0], point[1])
            distance = pt.distance(coast_point)
            if distance < min_distance:
                min_distance = distance
                nearest_coast_point = coast_point

    # Calculate the distance between the sea point and the nearest coastline point
    dist = geodesic((pt.y, pt.x), (nearest_coast_point.y, nearest_coast_point.x)).kilometers
    return dist


# -----------------------------------------------------------------------------------------
# **********************************Continuous Models**************************************
# -----------------------------------------------------------------------------------------
class Continuous_Model:
    """
    Continuous models class for analyzing access probability and expected delays.

    """

    def __init__(self, data, H_th, t_req, method='Moments'):
        """
        Initializes a WaveProbs object.

        Args:
            data (DataFrame): Input data containing wave characteristics.
            H_th (float): Threshold for significant wave height.
            t_req (float): Required access window in hours.
            method (str, optional): Method for fitting distributions ('Moments' or other).
                                    Defaults to 'Moments'.
        """

        self.H_th = H_th  # Threshold for significant wave height
        self.data = data  # Input data for analysis
        self.t_req = t_req  # Required access window
        self.method = method  # Method for fitting distributions ('Moments' or other)

        self.data_setup()  # Set up data for analysis
        self.fit_weibulls()  # Fit Weibull distributions

        # Set up Weibull parameters and features
        [k_H, H_0, H_c] = self.weibull_H
        self.H_m = weibull_min.mean(k_H, H_0, H_c)
        self.P_H = 1 - weibull_min.cdf(self.H_th, k_H, H_0, H_c)
        self.calm_statistics()  # Calculate calm-related statistics
        self.storm_statistics()  # Calculate storm-related statistics

        # Calculate the outputs
        self.P_0 = self.calc_P_0(self.t_req)  # Probability of instant access
        self.ed_total = self.calc_expected_delays(self.t_req)  # Calculate expected delays

    # -----------------------------------------------------------------------------------------------------
    # Initialisation functions
    # -----------------------------------------------------------------------------------------------------
    def data_setup(self):
        """
        Set up data sets for storm times and calm times to fit Weibull distributions.
        """

        # Reset index and create new columns for analysis
        df = self.data
        df['Hours'] = [i for i in range(len(df))]

        # Determine status of wave conditions and detect changes
        df['Status'] = df.H >= self.H_th
        df['Change'] = df.Status.diff()
        change_df = df[df.Change == True]

        # Calculate times between changes and identify starting condition
        change_times = [0] + [time for time in change_df.Hours]
        times_between = np.diff(change_times)
        start_condition = 'n' if int(df.Status[0]) == 0 else 'x'
        alt_condition = 'x' if start_condition == 'n' else 'n'

        # Create a dictionary to store distribution data
        distribution_data = {'H': df.H}
        distribution_data[str(start_condition)] = [time for time in times_between[0::2]]
        distribution_data[str(alt_condition)] = [time for time in times_between[1::2]]

        # Update attributes
        self.data = df
        self.distribution_data = distribution_data

    def fit_weibulls(self):
        """
        Fit Weibull distributions to calm times, storm times, and significant wave height.
        """

        def moment(x, k):
            x = [0] + np.sort(x)
            n = len(x)
            return np.sum([(1 - r / (n - 1)) ** k * (x[r + 1] - x[r]) for r in range(n - 1)])

        def moments_fit(x):
            # Calculate moments to estimate shape, loc, and scale parameters
            m_1 = np.mean(x)
            m_2 = moment(x, 2)
            m_3 = moment(x, 3)
            m_4 = moment(x, 4)
            shape = np.log(2) / (np.log(m_1 - m_2) - np.log(m_2 - m_4))
            loc = 0
            scale = (m_1 - loc) / gamma(1 + 1 / shape)
            return shape, loc, scale

        if self.method == 'Moments':
            # Fit Weibull distributions using moment-based estimation
            self.weibull_H = moments_fit(self.distribution_data['H'])
            self.weibull_n = moments_fit(self.distribution_data['n'])
            self.weibull_x = moments_fit(self.distribution_data['x'])
        else:
            # Fit Weibull distributions using Maximum Likelihood Estimation (MLE)
            self.weibull_H = weibull_min.fit(self.distribution_data['H'])
            self.weibull_n = weibull_min.fit(self.distribution_data['n'], floc=0)
            self.weibull_x = weibull_min.fit(self.distribution_data['x'], floc=0)

        # Store the fitted distributions for future reference
        self.distributions = {'H': self.weibull_H, 'n': self.weibull_n, 'x': self.weibull_x}

    # -----------------------------------------------------------------------------------------------------
    # Calculation of calm distrubution based statistics
    # -----------------------------------------------------------------------------------------------------
    def calm_statistics(self):
        """
        Calculate calm-related statistics based on fitted Weibull distribution parameters.
        """

        # Extract Weibull parameters for calm distribution
        (self.alpha_n, self.loc_n, self.beta_n) = self.weibull_n

        # Calculate parameters and statistics for the calm distribution
        self.g_n = (1 + 1 / self.alpha_n) ** self.alpha_n
        self.tau_n = weibull_min.mean(self.alpha_n, loc=self.loc_n, scale=self.beta_n)
        self.q_n = self.calc_q_n(self.t_req)
        self.M_qn = self.calc_M_qn(self.t_req)
        self.Q_n = self.calc_Q_n(self.t_req)
        self.M_qqn = self.calc_M_qqn(self.t_req)

    def calc_M_qn(self, T):
        """
        Calculate the normalized expected value of calm duration up to time T.

        Args:
            T (float): Time value.

        Returns:
            float: Normalized expected value of calm duration up to time T.
        """
        integral = quad(lambda t: t * self.calc_q_n(T), 0, T)
        I = integral[1] - integral[0]
        return 1 / self.tau_n * I

    def calc_Q_n(self, T):
        """
        Calculate the probability of no calm events up to time T.

        Args:
            T (float): Time value.

        Returns:
            float: Probability of no calm events up to time T.
        """
        return np.exp(-self.g_n * (T / self.tau_n) ** self.alpha_n)

    def calc_q_n(self, T):
        """
        Calculate the intensity function for calm events at time T.

        Args:
            T (float): Time value.

        Returns:
            float: Intensity function for calm events at time T.
        """
        return self.g_n * self.alpha_n / self.tau_n * (T / self.tau_n) ** (self.alpha_n - 1) * self.calc_Q_n(T)

    def calc_M_qqn(self, T):
        """
        Calculate the normalized second moment (calm) assuming Weibull distribution.

        Args:
            T (float): Time value.

        Returns:
            float: Normalized second moment (calm) up to time T.
        """
        return gammainc(1 + 2 / self.alpha_n, self.g_n * (T / self.tau_n) ** self.alpha_n) / (
                    2 * gamma(1 + 1 / self.alpha_n) ** 2)

    # -----------------------------------------------------------------------------------------------------
    # Calculation of storm distribution based statistics
    # -----------------------------------------------------------------------------------------------------

    def storm_statistics(self):
        """
        Calculate storm-related statistics based on fitted Weibull distribution parameters.
        """

        # Extract Weibull parameters for storm distribution
        (self.alpha_x, self.loc_x, self.beta_x) = self.weibull_x

        # Calculate parameters and statistics for the storm distribution
        self.g_x = (1 + 1 / self.alpha_x) ** self.alpha_x
        self.tau_x = weibull_min.mean(self.alpha_x, loc=self.loc_x, scale=self.beta_x)
        self.q_x = self.calc_q_x(self.t_req)
        self.M_qx = self.calc_M_qx(self.t_req)
        self.Q_x = self.calc_Q_x(self.t_req)
        self.M_qqx = self.calc_M_qqx(self.t_req)

    def calc_M_qx(self, T):
        """
        Calculate the normalized expected value of storm duration up to time T.

        Args:
            T (float): Time value.

        Returns:
            float: Normalized expected value of storm duration up to time T.
        """
        integral = quad(lambda t: t * self.calc_q_x(T), 0, T)
        I = integral[1] - integral[0]
        return 1 / self.tau_x * I

    def calc_Q_x(self, T):
        """
        Calculate the probability of no storm events up to time T.

        Args:
            T (float): Time value.

        Returns:
            float: Probability of no storm events up to time T.
        """
        return np.exp(-self.g_x * (T / self.tau_x) ** self.alpha_x)

    def calc_q_x(self, T):
        """
        Calculate the intensity function for storm events at time T.

        Args:
            T (float): Time value.

        Returns:
            float: Intensity function for storm events at time T.
        """
        return self.g_x * self.alpha_x / self.tau_x * (T / self.tau_x) ** (self.alpha_x - 1) * self.calc_Q_x(T)

    def calc_M_qqx(self, T):
        """
        Calculate the normalized second moment (storm) assuming Weibull distribution.

        Args:
            T (float): time needed to carry out operation

        Returns:
            float: Normalized second moment (storm) up to time T.
        """
        return gammainc(1 + 2 / self.alpha_x, self.g_x * (T / self.tau_x) ** self.alpha_x) / (
                    2 * gamma(1 + 1 / self.alpha_x) ** 2)

    # -----------------------------------------------------------------------------------------------------
    # Delay calculations
    # -----------------------------------------------------------------------------------------------------

    def calc_expected_delays(self, T=None):
        '''
        Calculate expected delays

        Args:
            T (float): time needed to carry out operation

        Returns:
            float: Number of hours until expected window of length t
        '''
        P_H = self.P_H
        tau_x = self.tau_x
        tau_n = self.tau_n
        if T == None:
            T = self.t_req
            M_qqx = self.M_qqx
            M_qqn = self.M_qqn
            Q_n = self.Q_n
            M_qn = self.M_qn
        else:
            M_qqx = self.calc_M_qqx(T)
            M_qqn = self.calc_M_qqn(T)
            Q_n = self.calc_Q_n(T)
            M_qn = self.calc_M_qn(T)

        self.ed_1 = P_H * M_qqx * tau_x  # Expected delay time of type 1
        self.ed_2a = (1 - P_H) ** 2 / P_H * M_qqn * tau_x  # Expected delay time of type 2a
        self.ed_2b = P_H * Q_n * T ** 2 / (2 * tau_x)  # Expected delay time of type 2b
        self.ed_3 = (1 - P_H * M_qn) * tau_x * P_H * Q_n * T  # Expected delay time of type 3
        self.ed_higher = (P_H + (1 - P_H) * M_qn + P_H * Q_n * T / tau_x) * (P_H + (1 - P_H) * M_qn) * tau_x / (
                    P_H * Q_n)
        self.ed_total = self.ed_1 + self.ed_2a + self.ed_2b + self.ed_3 + self.ed_higher  # Calculate total expected delay as sum
        return self.ed_total

    def calc_P_0(self, T=None):
        '''
        Calculate expected probability of instant access

        Args:
            T (float): time needed to carry out operation
        Returns:
            float: probability of instant access

        '''
        if T == None:
            return (1 - self.P_H) * (1 - self.M_qn - self.Q_n * self.t_req / self.tau_n)
        else:
            return (1 - self.P_H) * (1 - self.calc_M_qn(T) - self.calc_Q_n(T) * T / self.tau_n)

    # -----------------------------------------------------------------------------------------------------
    # Graphs and other Outputs
    # -----------------------------------------------------------------------------------------------------

    def compare_fit(self, var='n'):
        """
        Compare the fitted Weibull distribution with empirical data for a specified variable.

        Args:
            var (str): Variable to compare ('n' for calm duration, 'x' for storm duration, 'H' for significant wave height).

        Returns:
            None
        """

        # Extract data and distribution parameters
        data = self.distribution_data[var]
        shape, loc, scale = self.distributions[var]

        # Generate x values for the fitted Weibull distribution
        x = np.linspace(weibull_min.ppf(0.001, shape, loc=loc, scale=scale),
                        weibull_min.ppf(0.999, shape, loc=loc, scale=scale), 100)

        # Plot the fitted Weibull distribution and empirical data
        plt.plot(x, weibull_min.cdf(x, shape, loc=loc, scale=scale), 'b--', label='Fitted Weibull Distribution')
        x = np.linspace(min(data), max(data), 100)
        plt.ylabel('Probability Density')

        # Set x-axis label based on the variable
        if var == 'H':
            xlab = r'Significant Wave Height, $H_s$ (m)'
        elif var == 'n':
            xlab = 'Calm Duration (h)'
        else:
            xlab = 'Storm Duration (h)'

        plt.xlabel(xlab)
        ecdf = ECDF(data)
        plt.scatter(x, ecdf(x), c='k', s=2, label='Empirical Data')
        plt.xlim(min(x), max(x))
        plt.ylim(0, 1)
        plt.grid()
        plt.legend()

    def compare_fits(self):
        """
        Compare fitted Weibull distributions for multiple variables using subplots.

        Args:
            None

        Returns:
            None
        """

        # Create subplots for each variable
        fig, ax = plt.subplots(1, 3, figsize=(15, 2.5))

        for i, var in enumerate(['H', 'n', 'x']):
            sca = ax[i]
            data = self.distribution_data[var]
            shape, loc, scale = self.distributions[var]

            # Generate x values for the fitted Weibull distribution
            x = np.linspace(weibull_min.ppf(0.001, shape, loc=loc, scale=scale),
                            weibull_min.ppf(0.999, shape, loc=loc, scale=scale), 100)

            # Plot the fitted Weibull distribution and empirical data
            sca.plot(x, weibull_min.cdf(x, shape, loc=loc, scale=scale), 'b--', label='Fitted Weibull Distribution')
            x = np.linspace(min(data), max(data), 100)

            # Set x-axis label based on the variable
            if var == 'H':
                xlab = r'Significant Wave Height, $H_s$ (m)'
            elif var == 'n':
                xlab = 'Calm Duration (h)'
            else:
                xlab = 'Storm Duration (h)'

            sca.set(xlabel=xlab)

            # Set y-axis label for the first subplot only
            if i == 0:
                sca.set(ylabel='Probability Density')

            ecdf = ECDF(data)
            sca.scatter(x, ecdf(x), c='k', s=2, label='Empirical Data')
            sca.set_xlim(min(x), max(x))
            sca.set_ylim(0, 1)
            sca.grid()
            sca.legend()

    def time_effect(self, Ts):
        """
        Visualize the effect of different access window lengths on probability and expected delays.

        Args:
            minimum (float): Minimum access window length.
            maximum (float): Maximum access window length.

        Returns:
            None
        """

        fig, ax = plt.subplots(1, 2, figsize=(15, 2.5))
        sca = ax[0]
        probs = [self.calc_P_0(t) for t in Ts]
        sca.plot(Ts, probs, 'k--')
        sca.set_xlim(np.min(Ts), np.max(Ts))
        sca.set(xlabel=r'Required Access Window, $t$ (h)', ylabel='Probability of Instant Access')
        plt.grid()

        sca = ax[1]
        eds = [self.calc_expected_delays(t) for t in Ts]
        sca.plot(Ts, eds, 'k--')
        sca.set_xlim(np.min(Ts), np.max(Ts))
        sca.set(xlabel=r'Required Access Window, $t$ (h)', ylabel='Expected Delay (h)')
        plt.grid()

    def height_effect(self, minimum, maximum):
        """
        Visualize the effect of different access window lengths on probability based on height.

        Args:
            minimum (float): Minimum access window length.
            maximum (float): Maximum access window length.

        Returns:
            None
        """

        ts = np.arange(minimum, maximum, (maximum - minimum) / 100)
        probs = [self.calc_P_0(t) for t in ts]
        plt.plot(ts, probs, 'k--')
        plt.xlim(minimum, maximum)
        plt.xlabel(r'Required Access Window, $t$ (h)')
        plt.ylabel('Probability of Instant Access')
        plt.grid()

lat = 50.99
long = -4

ops = ['reset', 'min_repair', 'med_repair', 'maj_repair', 'replac', 'ann_service']
t_reqs = [2,2,3,4,5,3]
ves = [0,0,0,1,2,0]
hs = [2,3,4]
frs = [7.5,3,0.275,0.04,0.08,1]
costs = [0,1000,18500,73500,334500,18500]
h_th = 2
rho = 1.293

cut_in = 3
cut_out = 25
rated_wsp = 10.59
rated_power = 12*10**6
area = np.pi*120**2
eta = 0.9
Cp = 0.489
hub_height = 150

turbine_parameters = [(cut_in, cut_out, rated_wsp), 
                      rated_power, 
                      area, 
                      eta,
                      Cp, 
                      hub_height]

class farm_level_assessment:
    
    def __init__(self, turbine_parameters, loc, v, i, j):
        (self.lon, self.lat) = loc
        self.v_ts = v
        [self.wsps, self.rated_power, self.area, self.eta, self.Cp, self.hub_height] = turbine_parameters
        self.i = i
        self.j = j
    def downtime_and_cost(self):
        cost = 0
        downtime = 0

        situations = [0,0,1,2,3,1]
        delay_situations = [(2,2), (3,2), (4,3), (5,4)]
        exp_delays = np.zeros(4)
        hs = ds[:,self.i, self.j].to_numpy()
        point_df = pd.DataFrame({'Time':range(len(hs)), 'H':hs})
        
        for i, sitch in enumerate(delay_situations):
            (t_req, h_th) = sitch
            dm = Discrete_Model(point_df, h_th, t_req)
            exp_delays[i] = dm.calc_expected_delay()
    
        for i, op in enumerate(ops):
            dist = distance_to_coast(lat, long)
            dist = distance_to_coast(lat, long)
            h_th = hs[ves[i]]
            travel_time = dist/80
            t = int(t_reqs[i]+travel_time)
            downtime += (exp_delays[situations[i]]+t_reqs[i]+travel_time)*frs[i]
            cost += costs[i]*frs[i]
            
        self.cost = cost
        self.downtime = downtime
        return (downtime, cost)
        
    def operation(self):
        v = self.v_ts
        (cut_in, cut_out, rated_wsp) = self.wsps
        perc_at_rated = len(np.where(v>=rated_wsp))/len(v)
        perc_operating = len(v[(np.where(v >= cut_in)) and (np.where(v <= cut_out))])
        self.power_ts = self.power()
        
    def power(self):
        p = np.zeros(len(self.v_ts))
        (cut_in, cut_out, rated_wsp) = self.wsps
        for i, u in enumerate(self.v_ts):
            if u>cut_in and u<=rated_wsp:
                p[i] = 0.5*self.area*self.Cp*rho*(u**3)*eta
            elif u>rated_wsp and u<=cut_out:
                p[i] = 0.5*self.area*self.Cp*rho*(rated_wsp**3)*eta
        self.power_ts = p
        return self.power_ts

    def availability(self):
        (downtime, cost) = self.downtime_and_cost()
        power_prod = self.power()
        prod_hours = len(np.where(power_prod!=0)[0])
        total_hours = 8760
        self.availability = (prod_hours-downtime)/total_hours
        return self.availability
        
    def aep(self):
        availability = self.availability()
        tpp = np.sum(self.power_ts)
        self.aep = tpp*availability
        return self.aep

    def cost_per_kw(self):
        aep = self.aep()
        self.cost_per_kw = self.cost*8760*self.availability/(aep/10**3)
        return self.cost_per_kw
        
# pt_assess = farm_level_assessment(turbine_parameters, (lat, long), v)
# pt_assess.operation()
# pt_assess.cost_per_kw()

ds = xr.open_dataarray("swh.nc")

g = 9.81
results_dict = {}
lats = ds.latitude.to_numpy()[33:35]
longs = ds.longitude.to_numpy()
warnings.filterwarnings("ignore")
for i, lat in tqdm(enumerate(lats), total=len(lats)):
    for j, long in tqdm(enumerate(longs), total=len(longs), leave=False):
        if globe.is_land(lat, long)==False:
            ts = ds[:, i, j].to_numpy()
            if np.sum(np.isnan(ts))==0:
                fs = [g/(2*np.pi)*(h/1.56)**0.5 for h in ts]
                vs = [0.87*(g/(2*np.pi)*f)**0.5*150**0.3 for f in fs]
                pt_assess = farm_level_assessment(turbine_parameters, (lat, long), vs, i, j)
                cost_per_kw = pt_assess.cost_per_kw()
                results_dict[(lat,long)] = [cost_per_kw, pt_assess.aep, pt_assess.downtime, pt_assess.availability]
