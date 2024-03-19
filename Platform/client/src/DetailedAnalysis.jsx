import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

const DetailedAnalysisComponent = () => {
    return (
        <>
            <div style={{position: "absolute", width: "100%", height: "10%", backgroundColor: "lightblue"}}>
            </div>
         <div style={{position: "absolute", width: "100%", height: "88%", top: "12%", overflowY: "scroll"}}>
            <h1>
                this works!
            </h1>
            <Container>
                <Row>
                    This is row 1
                </Row>
                <Row>
                    This is row 2
                </Row>
            </Container>

        </div>

        </>
    )
};

export { DetailedAnalysisComponent };
