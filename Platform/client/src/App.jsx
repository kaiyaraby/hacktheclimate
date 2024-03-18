import {
    createBrowserRouter,
    RouterProvider,
} from "react-router-dom";
import "./index.css";
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
