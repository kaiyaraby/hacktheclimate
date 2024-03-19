import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Image from 'react-bootstrap/Image';

import WindRosePoint5180_152_Alt from "./DataAssets/windrose_point_5180_152_10years_option_B.gif";
import WindRosePoint5180_152 from "./DataAssets/windrose_point_5180_152_10years.gif";
import WindRosePoint5203_337 from "./DataAssets/windrose_point_5203_337_10years.gif";
import WindRosePoint5362_442 from "./DataAssets/windrose_point_5362_442_10years.gif";
import AirDensityPoint5180_152 from "./DataAssets/point_5180_152_10years_airdensity.gif";
import WindSpeedPoint5180_152 from "./DataAssets/point_5180_152_10years_windspeed.gif";

const WindRoseComponent = (props) => {
    return (
        <>
            <Row className="m-2">
                <Col>
                    <Image src={props.left} alt="" />
                </Col>
                <Col>
                    <Image src={props.right} alt="" />
                </Col>
            </Row>
        </>
    );
}

const LeftDisplayComponent = (props) => {
    return <>
        <Row className="m-2">
            <Col sm={10}>
                <Image className="m-auto" src={props.image} alt="" />
            </Col>
        </Row>
        <div className="m-4" />
    </>
};

const RightDisplayComponent = (props) => {
    return <>
        <Row className="m-2">
            <Col sm={10}>
                <Image className="m-auto" src={props.image} alt=""/>
            </Col>
        </Row>;
        <div className="m-4" />
    </>
};

const DetailedAnalysisComponent = () => {
    return (
        <>
            <div style={{position: "absolute", width: "100%", height: "10%", backgroundColor: "lightblue"}}>
            </div>
         <div style={{position: "absolute", width: "100%", height: "90%", top: "10%", overflowY: "scroll"}}>
            <div className="m-4" />
            <Container fluid>
                <div className="m-4" />
                <h3>Point Analysis</h3>
                <div className="m-4" />
                <RightDisplayComponent image={WindSpeedPoint5180_152} title="Title" text="Text"/>
                <WindRoseComponent left={WindRosePoint5180_152} right={WindRosePoint5180_152_Alt}/>
                <LeftDisplayComponent image={AirDensityPoint5180_152} title="Title" text="Text"/>
            </Container>

        </div>

        </>
    )
};

export { DetailedAnalysisComponent };
