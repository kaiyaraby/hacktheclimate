import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import { App } from './App';
import reportWebVitals from './reportWebVitals';
import 'bootstrap/dist/css/bootstrap.css';

const myElement = <h1>I Love JSX!</h1>;
const Team =(<div>
            <h2>Meet the Team</h2>
            <p> whatever</p>
            </div>)




const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(Team);

// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>
// );
