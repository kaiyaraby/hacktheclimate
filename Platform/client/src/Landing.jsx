import './App.scss';
import Button from 'react-bootstrap/Button';
import Image from 'react-bootstrap/Image';
import turbines from './Images/turbines.jpg';

const LandingComponent = () => {
    return (
    <div>

    <div className="bg" />

    <div class='text-on-image'>
        <heady class='headyurl'> wind.jolpi.ca </heady><br/>
        <heady class='heady'> Offshore Wind Analysis Tool </heady>
        <p class='ohmy'>
        The aim of this project is to present a framework for resource assessment, 
        to enable to developers to use environmental data to identify high-value locations for wind farms. <br/>
        The user can select an area over which to assess several KPIs such as Annual Energy Yield, Expected Downtime and Operation and Maintenance Cost 
        per kW per year. These may be assessed quickly, over a very large area, to allow comparison of potential sites.
        <br/><br/>
        These models combine traditional estimates with a Discrete Time Markov Chain Model capturing the behaviour and stochasticity
        of weather conditions, trained on over 16 GB of combined environmental data from the Vestas Climate Library and HubOcean. The incorporation of this model allows for accurate estimation of 
        weather delays and associated downtime. 
        <br/><br/>
        The user may also produce a more in-depth analysis based on conditions at a single point, and compare change in conditions over time.
            <br />
            <z> <div class="link-container">
  <a href="https://github.com/kaiyaraby/hacktheclimate" target="_blank" class="gita">
    <svg height="32" aria-hidden="true" viewBox="0 0 16 16" version="1.1" width="32" data-view-component="true" class="logo octicon octicon-mark-github v-align-middle color-fg-default">
      <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
    </svg>
    <span>Source Code</span>
  </a>
</div> </z>
        </p>
        
    </div>

    </div>
    )
};

export { LandingComponent };


