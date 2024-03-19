import './App.scss';
import Button from 'react-bootstrap/Button';
import Image from 'react-bootstrap/Image';
import turbines from './Images/turbines.jpg';

const LandingComponent = () => {
    return (
    <div>

    <div className="bg" />

    <div class='text-on-image'>
        <heady class='heady'> Offshore Wind Analysis Tool </heady>
        <p class='ohmy'>
        The aim of this project is to present a framework for resource assessment, 
        to enable to developers to use environmental data to identify high-value locations for wind farms. 
        The user can select an area over which to assess several KPIs such as Wind speed, Wind rose, Expected delay in maintaince, Annual Energy Production and others.
            <br />
            <z> <div class="link-container">
  <a href="https://github.com/kaiyaraby/hacktheclimate" target="_blank">
    <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub Logo" class="logo"/>
    <span>Source Code</span>
  </a>
</div> </z>
        </p>
        
    </div>

    </div>
    )
};

export { LandingComponent };


