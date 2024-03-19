import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Image from 'react-bootstrap/Image';

import Heatmap_2022_percentage_of_time_operation from "./DataAssets/heatmap_2022_percentage_of_time_spent_at_rated_operation.png";
import Heatmap_avg_wind_speed_2012_and_2022 from "./DataAssets/heatmap_avg_wind_speed_2012_and_2022.gif";

import AEY from "./DataAssets/AEY.png";
import Availability from "./DataAssets/Availability.png";
import Downtime from "./DataAssets/Downtime (hours).png";
import OMCost from "./DataAssets/OM_cost.png";

const AreaAnalysisComponent = () => {
    return (
        <>
            <div style={{position: "absolute", width: "100%", height: "10%", backgroundColor: "lightblue"}}>
            </div>
         <div style={{position: "absolute", width: "100%", height: "90%", top: "10%", overflowY: "scroll"}}>
            <div className="m-4" />
            <Container fluid>
                <div className="m-4" />
                <h3>Selected Area Analysis</h3>
                <div className="m-4" />
                <Image className="m-auto" src={AEY} alt=""/>
                <Image className="m-auto" src={Availability} alt=""/>
                <Image className="m-auto" src={Downtime} alt=""/>
                <Image className="m-auto" src={OMCost} alt=""/>
                <Image className="m-auto" src={Heatmap_2022_percentage_of_time_operation} alt=""/>
                <Image className="m-auto" src={Heatmap_avg_wind_speed_2012_and_2022} alt=""/>
            </Container>
        </div>

        </>
    )
};

export { AreaAnalysisComponent };
