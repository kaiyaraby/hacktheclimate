import Card from 'react-bootstrap/Card';
import CardGroup from 'react-bootstrap/CardGroup';
import './App.scss';
import profile from './Images/penguinstranger.png';
import kaiya from './Images/kaiyacropped.jpg';
import kim from './Images/kim.jpg';
import pauline from './Images/pauline.jpg';
import jess from './Images/jess.webp';
import ed from './Images/ed.jpg';

const TeamComponent =() => {
    return <body class='loading-page'>

                <div className="bg2" />

                <div class='heady2'>
                    <heady2> Meet the team </heady2>
                    
                </div>

                <divy>
                    <br />
                    <br />
                    <br />
                    <br />
                    
                </divy>

                <CardGroup class = 'wrapper' display="inline-block">
                    <Card bg = 'black' text = 'white' class='card'>
                        <div style={{textAlign: 'center'}}>
                            <Card.Img src={kaiya} style={{width: '13vw', height: '18vw', borderRadius: 200, alignItems: 'center'}}/>
                        </div>
                        <Card.Body>
                        <Card.Title style={{textAlign:'center'}}>Kaiya</Card.Title>
                        <Card.Text style={{textAlign:'center'}}>
                            Data Scientist (Area Analysis)
                        </Card.Text>
                        </Card.Body>
                    </Card>
                    <Card bg = 'black' text = 'white' class='card'>
                        <div style={{textAlign: 'center'}}>
                            <Card.Img src={jess} style={{width: '13vw', height: '18vw', borderRadius: 200, alignItems: 'center'}}/>
                        </div>
                        <Card.Body>
                        <Card.Title style={{textAlign:'center'}}>Jess</Card.Title>
                        <Card.Text style={{textAlign:'center'}}>
                            Data Pipelines Architect
                        </Card.Text>
                        </Card.Body>

                    </Card>
                    <Card bg = 'black' text = 'white' class='card'>
                        <div style={{textAlign: 'center'}}>
                            <Card.Img src={kim} style={{width: '13vw', height: '18vw', borderRadius: 200, alignItems: 'center'}}/>
                        </div>
                        <Card.Body>
                        <Card.Title style={{textAlign:'center'}}>Kim</Card.Title>
                        <Card.Text style={{textAlign:'center'}}>
                            Data Scientist (Point Analysis)
                        </Card.Text>
                        </Card.Body>

                    </Card>
                </CardGroup>
                <CardGroup class = 'wrapper' display="inline-block">
                    <Card bg = 'black' text = 'white' class='card'>
                        <div style={{textAlign: 'center'}}>
                            <Card.Img src={ed} style={{width: '13vw', height: '18vw', borderRadius: 200, alignItems: 'center'}}/>
                        </div>
                        <Card.Body>
                        <Card.Title style={{textAlign:'center'}}>Ed</Card.Title>
                        <Card.Text style={{textAlign:'center'}}>
                            Application Engineer
                        </Card.Text>
                        </Card.Body>
                    </Card>
                    <Card bg = 'black' text = 'white' class='card'>
                        <div style={{textAlign: 'center'}}>
                            <Card.Img src={pauline} style={{width: '13vw', height: '18vw', borderRadius: 200, alignItems: 'center'}}/>
                        </div>
                        <Card.Body>
                        <Card.Title style={{textAlign:'center'}}>Pauline</Card.Title>
                        <Card.Text style={{textAlign:'center'}}>
                            Front-End Engineer
                        </Card.Text>
                        </Card.Body>
                    </Card>
                    <Card bg = 'black' text = 'white' class='card'>
                        <div style={{textAlign: 'center'}}>
                            <Card.Img src={profile} style={{width: '13vw', height: '18vw', borderRadius: 200, alignItems: 'center'}}/>
                        </div>
                        <Card.Body>
                        <Card.Title style={{textAlign:'center'}}>Love</Card.Title>
                        <Card.Text style={{textAlign:'center'}}>
                            Made with love ♥
                        </Card.Text>
                        </Card.Body>
                    </Card>
                </CardGroup>

            </body>
};

export { TeamComponent };
