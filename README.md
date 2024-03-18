<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="150" height="150">
  </a>

  <h3 align="center">PengWind</h3>

  <p align="center">
    Python package using stochastic methods to estimate accessibility traits based on historic wave height data.
    <br />
    <a href="https://github.com/kaiyaraby/statistical_access_modelling"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/kaiyaraby/statistical_access_modelling/Examples_and_validation/Example">View Demo</a>
    ·
    <a href="https://github.com/kaiyaraby/statistical_access_modelling">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
The aim of this project is to present a framework for resource assessment, to enable to developers to use environmental data to identify high-value locations for wind farms.
The user can select an area over which to assess several KPIs including:
- Wind speed
  - Mean
  - Max
  - Min
  - Standard Deviation
  - Wind rose
    
- Access
    - Expected delay time
    - Probability of instant access
      
- Availability
- Downtime
- Annual Energy Production
- Operation & Maintenance Cost per kW

Traditionally, to incorporate the true variability of weather conditions, Monte Carlo simulations are often employed. However, these are computationally complex and limit the area over which resource, especially complex estimates such as Downtime, AEP, or O&M cost could be calculated. Through implementation of a number of novel computationally efficient models we have enabled calculation of these estimates quickly over large areas.
[![Product Name Screen Shot][product-screenshot]](https://example.com)



<p align="right">(<a href="#readme-top">back to top</a>)</p>






<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- Modelling -->
## Modelling
### Access Modelling
When unscheduled maintenance or repairs need to be carried out, vessels may only be sent out when the weather conditions are safe for a vessel, for the time needed to travel and carry out the operation.
\noindent We may define three distinct states: 
\begin{itemize}
    \item 0: Weather conditions unsuitable
    \item 1a: Access possible, but insufficient time remaining to carry out repair
    \item 1b: Access possible, and sufficient time remaining to carry out repair
\end{itemize}

<img src="images/flowchart.png" alt="Logo" width="150" height="150">

\subsubsection{Markov Chain Models}
Discrete Time Markov Chains (DTMCs) are characterised by a discrete time state space, where at each time the state may take a single value. In this report, we focus on two state models, as shown below. 

<img src="images/flowchart.png" alt="Logo" width="150" height="150">
\noindent 
From a current state we may remain or move to the alternate state with probabilities determined by their related transition matrix:
$$
\pi = \begin{bmatrix}
    P_{0,0} & P_{0,1}\\
    P_{1,0} & P_{1,1}
\end{bmatrix}.
$$
\subsection{Markov Access Model}
We first model the accessibility, $\mathbf{X} = \{X_1, X_2, \cdots, X_n\}$, where $X_t=1$ indicates that there is an access window beginning at time $t$. This model assumes a constant probability of accessibility, $Pr(X_t=1)=P$, and of transition between states
$$Pr(X_t=i|X_{t-1}=j)=P_{i,j}.$$
\subsubsection{Probability of Instant Access}
For $0.1\leq P
\leq 0.9$, we may construct a confidence interval for $P$ as $(P_L, P_U)$ \cite{Bedrick1989, crow1979approximate}, where the limits are defined as
\begin{align}
    P_U&=\frac{S+\frac{z_{\frac{\alpha}{2}}}{2}+\left[\frac{1}{2}+z_\frac{\alpha}{2}\sqrt{h\left(\hat{\theta}\right)\left\{S+\frac{1}{2}-\frac{\left(S+\frac{1}{2}\right)^2}{n}+\frac{z_\frac{\alpha}{2}^2h\left(\hat{\theta}\right)}{4}\right\}}\right]}
    {n+z_\frac{\alpha}{2}^2h\left(\hat{\theta}\right)}\\
        P_L&=\frac{S+\frac{z_{\frac{\alpha}{2}}}{2}-\left[\frac{1}{2}+z_\frac{\alpha}{2}\sqrt{h\left(\hat{\theta}\right)\left\{S-\frac{1}{2}-\frac{\left(S-\frac{1}{2}\right)^2}{n}+\frac{z_\frac{\alpha}{2}^2h\left(\hat{\theta}\right)}{4}\right\}}\right]}
    {n+z_\frac{\alpha}{2}^2h\left(\hat{\theta}\right)},
\end{align}
where $S=\sum^n_{i=1}X_i$ denotes the number of observed access points, $z_{1-\frac{\alpha}{2}}$ is the $(1-\frac{\alpha}{2})^{th}$ quantile of the standard normal distribution and \begin{align}
    h(\theta)=1+\frac{2\theta}{1-\theta}\frac{1-(1-\theta^n)}{n(1-\theta)}
\end{align} is a function of the product-moment correlation coefficient between adjacent states $X_k$ and $X_{k+1}$, given by $\theta=\frac{P_{1,1}-P}{1-P}$ \cite{Bedrick1989}.\\
\newline
If $P$, or $1-P$ is very small (here we consider 0.1 to be an appropriate threshold), then this method is not appropriate and we instead utilise a modified Anderson-Burstein interval \cite{crow1979validation}.
Since $S$ is assumed to be Poisson-distributed with parameter $nP$, then we may write
\begin{align}
    P_U&=\hat{P}+\left(P_{UI}-\hat{P}\right)\sqrt{1+\frac{2\hat{\theta}}{1-\hat{
    \theta}}}\\
    P_L &= \hat{P}-\left(\hat{P}-P_{LI}\right)\sqrt{1+\frac{2\hat{\theta}}{1-\hat{
    \theta}}},
\end{align}
where $(L,U)$ is the Pearson-Hartley confidence interval for the Poisson mean with parameter $nP$, and
\begin{align}
    P_{UI} &=\frac{U}{n+d+\frac{1}{2}(U-S)}\\
    P_{LI} &= \frac{L}{n-\frac{1}{2}(S-1-L)}
\end{align}
are the Anderson-Burstein confidence limits  with adjustment factor $d$ \cite{anderson1967approximating, anderson1968approximating}.
\subsubsection{Expected Delay}
The expected delay, $\lambda$, is given by 
\begin{align}
    \lambda &= P\lambda_1+(1-P)\lambda_0\\
    &= P\cdot 0+(1-P)\lambda_0\\
    &= (1-P)\lambda_0,
\end{align}
where $\lambda_0$ is calculated as
\begin{align}
    &\lambda_0 = P_{0,0}\cdot(\lambda_0+1)+P_{0,1}\cdot 1\\
    \Rightarrow &\lambda_0= 1+P_{0,0}\lambda_0\\
    \Rightarrow &\lambda_0(1-P_{0,0})=1\\
    \Rightarrow &\lambda_0=\frac{1}{1-P_{0,0}}\\
    \Rightarrow&\lambda_0=\frac{1}{P_{0,1}}.
\end{align}
The expected value for $\lambda_0$ is given by the sample mean of wait times from inaccessible states, $\hat{\lambda}_0$. To assess the variance of this parameter we then consider the variance of its inverse $P_{0,1}.$ \\
\newline
Confidence intervals for the transition matrix properties are outlined as \cite{Wan2020}
\begin{align}
    P_{i,j}^U &= p_{i,j}+ z_{1-\frac{\alpha}{2}}\sqrt{\frac{p_{i,j}(1-p_{i,j})}{f_i}}\\
    P_{i,j}^L &= p_{i,j}- z_{1-\frac{\alpha}{2}}\sqrt{\frac{p_{i,j}(1-p_{i,j})}{f_i}}
\end{align}
where $f_i = \sum^n_{k=1} \mathbb{I}(X_k = i)$ is the number of observed values of state $i$. 

\noindent We may then calculate the variance for $\lambda=\frac{1}{P_{0,1}}$ \cite{Wolter2006}
\begin{align}
    V\left(\frac{1}{P_{0,1}}\right)&=\left(\frac{1}{\hat{P}_{0,1}}\right)^2\left[\frac{V(1)}{1^2}+\frac{V(\hat{P}_{0,1})}{\hat{P}_{0,1}^2}-\frac{2C\left(1,\hat{P}_{0,1}\right)}{1\cdot \hat{P}_{0,1}}\right]\\
    &=\frac{1}{\hat{P}_{0,1}^2}\frac{V(\hat{P}_{0,1})}{\hat{P}_{0,1}^2}\\
    &=\frac{V(\hat{P}_{0,1})}{\hat{P}_{0,1}^4}\\
    &=\frac{SE(\hat{P}_{0,1})^2}{\hat{P}^4_{0,1}}\\
    &=\frac{\left(\frac{P^U_{0,1}-P_{0,1}^L}{2z_{1-\frac{\alpha}{2}}}\right)^2}{\hat{P}_{0,1}^4}\\
    &=\frac{(P_{0,1}^U-P_{0,1}^L)^2}{4\hat{P}_{0,1}^4z^2_{1-\frac{\alpha}{2}}}.
\end{align}
The order of this model is also entirely linear, but with a smaller factor, thus reducing the computation time from the empirical.
[![Product Name Screen Shot][product-screenshot]](https://example.com)


<p align="right">(<a href="#readme-top">back to top</a>)</p>






<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Kaiya Raby - kaiya.raby@strath.ac.uk

Project Link: [https://github.com/hacktheclimate]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

This package uses the methods outlined in  [Feuchtwang and Infield 2013](https://onlinelibrary.wiley.com/doi/abs/10.1002/we.1539). Further information about how these models have been developed can be found in the linked [document](https://github.com/statistical_access_modelling/Examples_and_validation/Derivation.pdf)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
