import { React, useState, useEffect, useRef } from "react";
import { getExampleData } from './Service/Example';
import Globe from "react-globe.gl";
import EarthTexture from "./earthtexture.jpg";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";

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
        }, accessCoverage]);
        console.log(globeSelectedArea);
    };

    const resetPoints = () => {
        setPoints([]);
        setGlobeSelectedArea([]);
    };

    return <RootInterfaceComponent globeSelectedArea={globeSelectedArea} addPoint={addPoint} resetPoints={resetPoints}/>;
};

const MenuComponent = (props) => {

    return <div style={{
        position: "absolute",
        width: "40%",
        height: "100%",
        left: "2%",
        border: "3px solid white",
        backgroundColor: "white",
    }}>
        <Container className="m-auto m-2">
            <Row>
                <h1>This is the top row!</h1>
                { JSON.stringify(props.points) }
            </Row>
            <Row>
                <Button onClick={props.resetPoints}>
                    Reset
                </Button>
            </Row>
        </Container>
    </div>
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
        <GlobeComponent globeElement={globeElement} windowWidth={windowWidth} shiftAmount={shiftAmount} onGlobeClick={onGlobeClick} onGlobeRightClick={onGlobeRightClick} globeSelectedArea={props.globeSelectedArea} />
        <MenuComponent points={props.globeSelectedArea} resetPoints={props.resetPoints}/>
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
            polygonSideColor={() => 'rgba(0, 100, 0, 0.0)'}
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
