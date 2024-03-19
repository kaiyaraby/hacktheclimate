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