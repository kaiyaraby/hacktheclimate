import { React, useState, useEffect } from "react";
import {
    createBrowserRouter,
    RouterProvider,
} from "react-router-dom";
import "./index.css";
import { getExampleData } from './Service/Example';

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
]);

const App = () => {
    return <RouterProvider router={router} />
};

export { App };
