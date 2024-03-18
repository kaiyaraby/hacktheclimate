import {
    createBrowserRouter,
    RouterProvider,
} from "react-router-dom";
import "./index.css";
import 'bootstrap/dist/css/bootstrap.min.css';
import { TeamComponent } from "./Team";
import { WorkspaceComponent } from "./Workspace";
import { LandingComponent } from "./Landing";


const router = createBrowserRouter([
    {
        path: "/",
        element: <LandingComponent />,
    },
    {
        path: "/Team",
        element: <TeamComponent />,
    },
    {
        path: "/Workspace",
        element: <WorkspaceComponent />,
    },
]);

const App = () => {
    return <RouterProvider router={router} />
};

export { App };
