import { React, useState, useEffect, useRef } from "react";
import { getExampleData } from './Service/Example';
import { getAnalysis } from "./Service/Analysis";
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
    const [analysis, setAnalysis] = useState({});
    const [refresh, setRefresh] = useState(false);

    useEffect(() => {
        const updateAnalysis = async () => {
            const requestBody = points.map((x) => ({
                latitude: x[1],
                longitude: x[0]
            }));
            const response = await getAnalysis(requestBody);
            setAnalysis(response);
        };
        console.log(points);
        updateAnalysis();
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

    return <RootInterfaceComponent analysis={analysis} globeSelectedArea={globeSelectedArea} points={points} addPoint={addPoint} resetPoints={resetPoints}/>;
};

const MenuComponent = (props) => {

    return <Card bg = 'dark' class='search' text='white'
                style={{
                position: "absolute",
                width: "40%",
                height: "80%",
                left: "5%",
                top: "20%",
                overflowY:scroll,
                }}>
                <Card.Body>
                    <Card.Title style={{textAlign:'center'}}>Select Characteristics</Card.Title>
                    <Form>
                        <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                            
                        
                    <Accordion defaultActiveKey={['0']} alwaysOpen class='accord' style={{background: 'dark'}}>
                        <Accordion.Item eventKey="0">
                            <Accordion.Header>Accessibility</Accordion.Header>
                            <Accordion.Body>
                                <subcat>Access1</subcat>
                                <br/>
                                <div class="side-by-side">
                                    <div>
                                        <Form.Label>Average</Form.Label>
                                        <Form.Control type="number" placeholder="0" readOnly/>
                                    </div>
                                    <div>
                                        <Form.Label>Min</Form.Label>
                                        <Form.Control type="number" placeholder="0" readOnly/>
                                    </div>
                                    <div>
                                        <Form.Label>Max</Form.Label>
                                        <Form.Control type="number" placeholder="0" readOnly/>
                                    </div>
                                </div>

                                <subcat>Access2</subcat>
                                <br/>
                                <div class="side-by-side">
                                    <div>
                                        <Form.Label>Average</Form.Label>
                                        <Form.Control type="number" placeholder="0" readOnly/>
                                    </div>
                                    <div>
                                        <Form.Label>Min</Form.Label>
                                        <Form.Control type="number" placeholder="0" readOnly/>
                                    </div>
                                    <div>
                                        <Form.Label>Max</Form.Label>
                                        <Form.Control type="number" placeholder="0" readOnly/>
                                    </div>
                                </div>

                                <subcat>Access3</subcat>
                                <br/>
                                <div class="side-by-side">
                                    <div>
                                        <Form.Label>Average</Form.Label>
                                        <Form.Control type="number" placeholder="0" readOnly/>
                                    </div>
                                    <div>
                                        <Form.Label>Min</Form.Label>
                                        <Form.Control type="number" placeholder="0" readOnly/>
                                    </div>
                                    <div>
                                        <Form.Label>Max</Form.Label>
                                        <Form.Control type="number" placeholder="0" readOnly/>
                                    </div>
                                </div>
                            </Accordion.Body>
                        </Accordion.Item>
                        <Accordion.Item eventKey="1">
                            <Accordion.Header>Turbine</Accordion.Header>
                            <Accordion.Body>
                                <subcat>Turbine1</subcat>
                                <br/>
                                <div class="side-by-side">
                                    <div>
                                        <Form.Label>Average</Form.Label>
                                        <Form.Control type="number" placeholder="0" />
                                    </div>
                                    <div>
                                        <Form.Label>Min</Form.Label>
                                        <Form.Control type="number" placeholder="0" />
                                    </div>
                                    <div>
                                        <Form.Label>Max</Form.Label>
                                        <Form.Control type="number" placeholder="0" />
                                    </div>
                                </div>

                                <subcat>Turbine2</subcat>
                                <br/>
                                <div class="side-by-side">
                                    <div>
                                        <Form.Label>Average</Form.Label>
                                        <Form.Control type="number" placeholder="0" />
                                    </div>
                                    <div>
                                        <Form.Label>Min</Form.Label>
                                        <Form.Control type="number" placeholder="0" />
                                    </div>
                                    <div>
                                        <Form.Label>Max</Form.Label>
                                        <Form.Control type="number" placeholder="0" />
                                    </div>
                                </div>

                                <subcat>Turbine3</subcat>
                                <br/>
                                <div class="side-by-side">
                                    <div>
                                        <Form.Label>Average</Form.Label>
                                        <Form.Control type="number" placeholder="0" />
                                    </div>
                                    <div>
                                        <Form.Label>Min</Form.Label>
                                        <Form.Control type="number" placeholder="0" />
                                    </div>
                                    <div>
                                        <Form.Label>Max</Form.Label>
                                        <Form.Control type="number" placeholder="0" />
                                    </div>
                                </div>
                            </Accordion.Body>
                        </Accordion.Item>
                    </Accordion>
                    </Form.Group>
                    </Form>
                </Card.Body>
                <Card.Footer>
                <small className="muted" style={{textAlign:'center'}}>Learn more</small>
                </Card.Footer>
            </Card>

    // return <div style={{
    //     position: "absolute",
    //     width: "40%",
    //     height: "80%",
    //     left: "5%",
    //     top: "20%",
    //     border: "3px solid white",
    //     backgroundColor: "white",
    // }}>
    //     <Container className="m-auto m-2">
    //         <Row>
    //             <h1>This is the top row!</h1>
    //             { JSON.stringify(props.points) }
    //         </Row>
    //         <Row>
    //             <Button onClick={props.resetPoints}>
    //                 Reset
    //             </Button>
    //         </Row>
    //         <Row>
    //             {JSON.stringify(props.analysis)}
    //         </Row>
    //     </Container>
    // </div>
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
        <MenuComponent points={props.globeSelectedArea} resetPoints={props.resetPoints} analysis={props.analysis}/>
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
            polygonCapColor={() => 'rgba(200, 0, 0, 0.25)'}
            polygonsAltitude={0}
            polygonsTransitionDuration={0}
        />
    </div>;
}

const TestComponent = () => {

    const [data, setData] = useState([]);

    const updateData = async () => {
        const newData = await getExampleData();
        setData(newData);
    };

    useEffect(() => {
        updateData();
    }, []);

    return <>
        <h2>This is the test component</h2>
        <table>
        <thead>
        <td>
        Date
        </td>
        <td>
        Temperature
        </td>
        </thead>
        <tbody>
        {data.map(item => {
            return <tr key={item.date}>
                <td>
                {item.date}
                </td>
                <td>
                {item.temperatureC}
                </td>
                </tr>;
        })}
        </tbody>
        </table>
        </>
};

export { WorkspaceComponent }
