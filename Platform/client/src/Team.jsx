import Card from 'react-bootstrap/Card';
import CardGroup from 'react-bootstrap/CardGroup';
import './App.scss';
import profile from './Images/stranger.jpg';
import kaiya from './Images/kaiyacropped.jpg';
import kim from './Images/kim.jpg';
import pauline from './Images/pauline.jpg';
import jess from './Images/jess.webp';
import ed from './Images/ed.webp';

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
                    <br />
                    <br />
                </divy>

                <CardGroup class = 'wrapper' display="inline-block">
                    <Card bg = 'black' text = 'white' class='card'>
                        <div style={{textAlign: 'center'}}>
                            <Card.Img src={kaiya} style={{width: '20vw', height: '30vw', borderRadius: 200, alignItems: 'center'}}/>
                        </div>
                        <Card.Body>
                        <Card.Title style={{textAlign:'center'}}>Kaiya</Card.Title>
                        <Card.Text style={{textAlign:'center'}}>
                            PhD Research Student @University of Strathclyde
                        </Card.Text>
                        </Card.Body>
                        <Card.Footer>
                        <small className="muted" style={{textAlign:'center'}}>Learn more</small>
                        </Card.Footer>
                    </Card>
                    <Card bg = 'black' text = 'white' class='card'>
                        <div style={{textAlign: 'center'}}>
                            <Card.Img src={jess} style={{width: '20vw', height: '30vw', borderRadius: 200, alignItems: 'center'}}/>
                        </div>
                        <Card.Body>
                        <Card.Title style={{textAlign:'center'}}>Jess</Card.Title>
                        <Card.Text style={{textAlign:'center'}}>
                            Software Engineer @Skyscanner
                        </Card.Text>
                        </Card.Body>
                        <Card.Footer>
                        <small className="muted" style={{textAlign:'center'}}>Learn more</small>
                        </Card.Footer>
                    </Card>
                    <Card bg = 'black' text = 'white' class='card'>
                        <div style={{textAlign: 'center'}}>
                            <Card.Img src={kim} style={{width: '20vw', height: '30vw', borderRadius: 200, alignItems: 'center'}}/>
                        </div>
                        <Card.Body>
                        <Card.Title style={{textAlign:'center'}}>Kim</Card.Title>
                        <Card.Text style={{textAlign:'center'}}>
                            PhD Research Student @University of Strathclyde
                        </Card.Text>
                        </Card.Body>
                        <Card.Footer>
                        <small className="muted" style={{textAlign:'center'}}>Learn more</small>
                        </Card.Footer>
                    </Card>
                </CardGroup>

                <divy>
                    <br />
                    <br />
                    <br />
                    <br />
                    <br />
                </divy>


                <CardGroup class = 'wrapper' display="inline-block">
                    <Card bg = 'black' text = 'white' class='card'>
                        <div style={{textAlign: 'center'}}>
                            <Card.Img src={ed} style={{width: '20vw', height: '30vw', borderRadius: 200, alignItems: 'center'}}/>
                        </div>
                        <Card.Body>
                        <Card.Title style={{textAlign:'center'}}>Ed</Card.Title>
                        <Card.Text style={{textAlign:'center'}}>
                            Software Engineer @PwC
                        </Card.Text>
                        </Card.Body>
                        <Card.Footer>
                        <small className="muted" style={{textAlign:'center'}}>Learn more</small>
                        </Card.Footer>
                    </Card>
                    <Card bg = 'black' text = 'white' class='card'>
                        <div style={{textAlign: 'center'}}>
                            <Card.Img src={pauline} style={{width: '20vw', height: '30vw', borderRadius: 200, alignItems: 'center'}}/>
                        </div>
                        <Card.Body>
                        <Card.Title style={{textAlign:'center'}}>Pauline</Card.Title>
                        <Card.Text style={{textAlign:'center'}}>
                            Security Engineer @Check Point
                        </Card.Text>
                        </Card.Body>
                        <Card.Footer>
                        <small className="muted" style={{textAlign:'center'}}>Learn more</small>
                        </Card.Footer>
                    </Card>
                    <Card bg = 'black' text = 'white' class='card'>
                        <div style={{textAlign: 'center'}}>
                            <Card.Img src={profile} style={{width: '20vw', height: '30vw', borderRadius: 200, alignItems: 'center'}}/>
                        </div>
                        <Card.Body>
                        <Card.Title style={{textAlign:'center'}}>Join us!</Card.Title>
                        <Card.Text style={{textAlign:'center'}}>
                            Tell us more about you!
                        </Card.Text>
                        </Card.Body>
                        <Card.Footer>
                        <small className="muted" style={{textAlign:'center'}}>Learn more</small>
                        </Card.Footer>
                    </Card>
                </CardGroup>

            </body>
};

export { TeamComponent };
