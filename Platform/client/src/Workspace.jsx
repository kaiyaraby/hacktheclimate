import { React, useState, useEffect, useRef } from "react";
import { getExampleData } from './Service/Example';
import { getAccessibilityAnalysis, getTurbineAnalysis } from "./Service/Analysis";
import Globe from "react-globe.gl";
import EarthTexture from "./earthtexture.jpg";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";
import Card from 'react-bootstrap/Card';
import Form from 'react-bootstrap/Form';
import Accordion from 'react-bootstrap/Accordion';

const accessCoverage = {
    type: "feature",
    geometry: {
        type: "Polygon",
        coordinates: [
            [
                [11.0, 51.0],
                [-4.0, 51.0],
                [-4.0, 61.0],
                [11.0, 61.0],
            ]
        ]
    }
};

const WorkspaceComponent = (props) => {

    const [points, setPoints] = useState([]);
    const [globeSelectedArea, setGlobeSelectedArea] = useState([]);
    const [accessibilityAnalysis, setAccessibilityAnalysis] = useState({});
    const [turbineAnalysis, setTurbineAnalysis] = useState({});
    const [refresh, setRefresh] = useState(false);

    useEffect(() => {
        const updateTurbineAnalysis = async () => {
            const requestBody = points.map((x) => ({
                latitude: x[1],
                longitude: x[0]
            }));
            const response = await getTurbineAnalysis(requestBody);
            setTurbineAnalysis(response);
        };
        const updateAccessibilityAnalysis = async () => {
            const requestBody = points.map((x) => ({
                latitude: x[1],
                longitude: x[0]
            }));
            const response = await getAccessibilityAnalysis(requestBody);
            setAccessibilityAnalysis(response);
        }
        updateAccessibilityAnalysis();
        updateTurbineAnalysis();
    }, [points, refresh]);

    const addPoint = (lat, lng) => {
        let newPoints = points;
        points.push([lng, lat]);
        setPoints(newPoints);
        setGlobeSelectedArea([{
            type: "feature",
            geometry: {
                type: "Polygon",
                coordinates: [points]
            }
        }]);
        setRefresh(!refresh);
    };

    const resetPoints = () => {
        setPoints([]);
        setGlobeSelectedArea([]);
    };

    return <RootInterfaceComponent accessibilityAnalysis={accessibilityAnalysis} turbineAnalysis={turbineAnalysis} globeSelectedArea={globeSelectedArea} points={points} addPoint={addPoint} resetPoints={resetPoints}/>;
};

const TurbineParameterComponent = (props) => {
    return (
        <Accordion.Item eventKey={props.input.eventKey}>
            <Accordion.Header>Turbine Parameters</Accordion.Header>
            <Accordion.Body>
                {props.input.items.map(x => (
                <>
                    <div className="m-1">
                        <Form.Label>{x.parameter}</Form.Label>
                        <Form.Control type="text" placeholder={x.value} readOnly/>
                    </div>
                    <div className="m-1" />
                </>
                ))}
            </Accordion.Body>
        </Accordion.Item>
    )

}

const DataRangeComponent = (props) => {
    return (
        <Accordion.Item eventKey={props.input.eventKey}>
            <Accordion.Header>{props.input.title}</Accordion.Header>
            <Accordion.Body>
                {props.input.items.map(x => (
                <>
                <strong>{x.title}</strong>
                <div className="side-by-side">
                    <div className="m-1">
                        <Form.Label>Average</Form.Label>
                        <Form.Control type="text" placeholder={x.average} readOnly/>
                    </div>
                    <div className="m-1">
                        <Form.Label>Min</Form.Label>
                        <Form.Control type="text" placeholder={x.min} readOnly/>
                    </div>
                    <div className="m-1">
                        <Form.Label>Max</Form.Label>
                        <Form.Control type="text" placeholder={x.max} readOnly/>
                    </div>
                </div>
                <div className="m-1" />
                </>
                ))}
            </Accordion.Body>
        </Accordion.Item>
    )
}

const MenuComponent = (props) => {

    const turbineParameterInput = {
        eventKey: "3",
        items: [
            {
                parameter: "Parameter",
                value: 0
            }
        ]
    }

    const accessibilityInput = {
        eventKey: "0",
        title: "Accessibility Analysis",
        items: [
            {
                title: "Wave Height",
                min: props.accessibilityAnalysis.minWaveHeight,
                max: props.accessibilityAnalysis.maxWaveHeight,
                average: props.accessibilityAnalysis.meanWaveHeight
            },
            {
                title: "Instant Access Probability",
                min: props.accessibilityAnalysis.minInstantAccessProbability,
                max: props.accessibilityAnalysis.maxInstantAccessProbability,
                average: props.accessibilityAnalysis.meanInstantAccessProbability,
            },
            {
                title: "Expected Delay (Hours)",
                min: props.accessibilityAnalysis.minExpectedDelayHours,
                max: props.accessibilityAnalysis.maxExpectedDelayHours,
                average: props.accessibilityAnalysis.meanExpectedDelayHours
            }
        ]
    };

    const turbineInput = {
        title: "Turbine Analysis",
        eventKey: "1",
        items: [
            {
                title: "Availability",
                min: props.turbineAnalysis.minAvailability,
                max: props.turbineAnalysis.maxAvailability,
                average: props.turbineAnalysis.meanAvailability
            },
            {
                title: "O&M Cost (£/kW/Year)",
                min: props.turbineAnalysis.minCostPerKiloWatt,
                max: props.turbineAnalysis.maxCostPerKiloWatt,
                average: props.turbineAnalysis.meanCostPerKiloWatt,
            },
            {
                title: "Energy Yield (GWh)",
                min: props.turbineAnalysis.minAnnualExpectedPower,
                max: props.turbineAnalysis.maxAnnualExpectedPower,
                average: props.turbineAnalysis.meanAnnualExpectedPower
            },
            {
                title: "Downtime",
                min: props.turbineAnalysis.minDowntime,
                max: props.turbineAnalysis.maxDowntime,
                average: props.turbineAnalysis.meanDowntime
            }
        ]
    };

    return <Card bg = 'dark' className='search' text='white'
                style={{
                position: "absolute",
                width: "40%",
                height: "80%",
                left: "5%",
                top: "15%",
                overflowY: "scroll",
                }}>
                {props.points.length <= 2 ?
                <>
                    <div className="m-auto">
                        <p>Draw an area on the map to get started</p>
                    </div>
                </> :
                <>
                <Card.Body>
                    <Card.Title style={{textAlign:'center'}}>Create Analysis</Card.Title>
                    <Form>
                        <div className="d-grid gap-2 m-2">
                            <Button style={{backgroundColor: 'white'}} variant="light" className="m-2 margin-auto" size="lg" onClick={props.resetPoints}>
                                Reset Area Selection
                            </Button>
                        </div>
                        <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                            <Accordion defaultActiveKey={['0']}>
                                <DataRangeComponent input={accessibilityInput} />
                                <TurbineParameterComponent input={turbineParameterInput}/>
                                <DataRangeComponent input={turbineInput} />
                            </Accordion>
                        </Form.Group>
                    </Form>
                </Card.Body>
                <Card.Footer>
                <small className="muted" style={{textAlign:'center'}}>Learn more</small>
                </Card.Footer>
                </>}
            </Card>
};

const RootInterfaceComponent = (props) => {

    const windowHeight = window.innerHeight;
    const windowWidth = window.innerWidth;

    const shiftFactor = 0.4;
    const shiftAmount = windowWidth * shiftFactor;

    const menuHeight = windowHeight * 0.8;
    const menuWidth = windowWidth * shiftFactor;

    const globeElement = useRef(null);

    const onGlobeClick = ({lat, lng}, event) => {
        console.log("Left Click at " + lat + ", " + lng);
        props.addPoint(lat, lng);
    };

    const onGlobeRightClick = ({lat, lng}, event) => {
        console.log("Right Click at " + lat + ", " + lng);
    }
    return <>
        <GlobeComponent globeElement={globeElement} windowWidth={windowWidth} shiftAmount={shiftAmount} onGlobeClick={onGlobeClick} onGlobeRightClick={onGlobeRightClick} globeSelectedArea={props.globeSelectedArea} points={props.points}/>
        <MenuComponent points={props.points} resetPoints={props.resetPoints} accessibilityAnalysis={props.accessibilityAnalysis} turbineAnalysis={props.turbineAnalysis}/>
    </>;
};

const GlobeComponent = (props) => {

    return <div style={{
        marginLeft: `-${props.shiftAmount}}px`,
        position: "absolute"
    }}>
        <Globe
            ref={props.globeElement}
            width={props.windowWidth + props.shiftAmount}
            globeImageUrl={EarthTexture}
            showGraticules={true}
            showAtmosphere={true}
            onGlobeClick={props.onGlobeClick}
            onGlobeRightClick={props.onGlobeRightClick}
            polygonsData={props.globeSelectedArea}
            polygonCapColor={() => 'rgba(111, 111, 111, 0.15)'}
            polygonSideColor={() => 'rgba(111, 200, 111, 0.45)'}
            polygonsAltitude={0}
            polygonsTransitionDuration={0}
        />
    </div>;
}

export { WorkspaceComponent }
