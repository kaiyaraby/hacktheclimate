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
From a current state we may remain or move to the alternate state with probabilities determined by their related transition matrix:


$$
\pi = \begin{bmatrix}
    P_{0,0} & P_{0,1}\\
    P_{1,0} & P_{1,1}
\end{bmatrix}.
$$

We use this chain to model the accessibility,  $\mathbf{X} = \{X_1, X_2, \cdots, X_n\},$  where $X_t=1$ indicates that there is an access window beginning at time $t$.

This model assumes a constant probability of accessibility, $Pr(X_t=1)=P$, and of transition between states


$$Pr(X_t=i|X_{t-1}=j)=P_{i,j}.$$





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
