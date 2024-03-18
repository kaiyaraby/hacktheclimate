import { React, useState, useEffect } from "react";
import {
    createBrowserRouter,
    RouterProvider,
} from "react-router-dom";
import "./index.css";
import { getExampleData } from './Service/Example';
import Globe from "react-globe.gl";
import EarthTexture from "./earthtexture.jpg";

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
                "type": "Polygon",
                coordinates: [points]
            }
        }]);
        console.log(globeSelectedArea);
    };

    return <RootInterfaceComponent globeSelectedArea={globeSelectedArea} addPoint={addPoint} />;
};

const RootInterfaceComponent = (props) => {

    const onGlobeClick = ({lat, lng}, event) => {
        console.log("Left Click at " + lat + ", " + lng);
        props.addPoint(lat, lng);
    };

    const onGlobeRightClick = ({lat, lng}, event) => {
        console.log("Right Click at " + lat + ", " + lng);
    }
    return <GlobeComponent onGlobeClick={onGlobeClick} onGlobeRightClick={onGlobeRightClick} globeSelectedArea={props.globeSelectedArea} />;
};

const GlobeComponent = (props) => {

    return <Globe
        globeImageUrl={EarthTexture}
        showGraticules={true}
        showAtmosphere={true}
        onGlobeClick={props.onGlobeClick}
        onGlobeRightClick={props.onGlobeRightClick}
        polygonsData={props.globeSelectedArea}
        polygonCapColor={() => 'rgba(200, 0, 0, 0.6)'}
        polygonSideColor={() => 'rgba(0, 100, 0, 0.15)'}
    />;
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

const router = createBrowserRouter([
    {
        path: "/",
        element: <div>Hello world!</div>,
    },
    {
        path: "/test",
        element: <TestComponent />,
    },
    {
        path: "/workspace",
        element: <WorkspaceComponent />,
    },
]);

const App = () => {
    return <RouterProvider router={router} />
};

export { App };
