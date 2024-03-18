import {
    createBrowserRouter,
    RouterProvider,
    Outlet
} from "react-router-dom";
import "./index.css";
import 'bootstrap/dist/css/bootstrap.min.css';

import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import { LinkContainer } from "react-router-bootstrap";

import { TeamComponent } from "./Team";
import { WorkspaceComponent } from "./Workspace";
import { LandingComponent } from "./Landing";

const NavbarComponent = () => {
  return (
    <Navbar expand="lg" className="bg-body-tertiary">
      <Container>
        <LinkContainer to="/">
            <Navbar.Brand href="#home">PengWind</Navbar.Brand>
        </LinkContainer>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <LinkContainer to="/">
                <Nav.Link href="/">Home</Nav.Link>
            </LinkContainer>
            <LinkContainer to="/Workspace">
                <Nav.Link href="/Workspace">Workspace</Nav.Link>
            </LinkContainer>
            <LinkContainer to="/Team">
                <Nav.Link href="/Team">About</Nav.Link>
            </LinkContainer>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

const AppRoot = () => {
    return <>
        <NavbarComponent />
        <Outlet />
    </>
};

const router = createBrowserRouter([
    {
        path: "/",
        element: <AppRoot />,
        children: [
            {
                path: "",
                element: <LandingComponent />
            },
            {
                path: "Team",
                element: <TeamComponent />
            },
            {
                path: "Workspace",
                element: <WorkspaceComponent />
            }
        ]
    }
]);

const App = () => {

    return <>
        <RouterProvider router={router}/>
    </>
};

export { App };
