import './App.scss';
import Button from 'react-bootstrap/Button';
import Image from 'react-bootstrap/Image';
import turbines from './Images/turbines.jpg';
import profile from './Images/profilegrey.jpg';
import Card from 'react-bootstrap/Card';
import CardGroup from 'react-bootstrap/CardGroup';
import { Input } from 'react-chat-elements'

// RCE CSS
import 'react-chat-elements/dist/main.css'
// MessageBox component
import { MessageBox } from 'react-chat-elements'
import { ChatItem } from 'react-chat-elements'
import { MessageList } from 'react-chat-elements'


const IndepthComponent = () => {
    return (
        <body class='loading-page'>
            <div className="bg2">

                <div class='msg'>

                    <div class= 'box' style={{textAlign:'left',borderRadius: 15}}><text>
                    Summary:<br />
                    - The probability of no weather delays in repairing turbines is slightly below the ideal value, which may lead to some delays in maintenance.<br />
                    - The expected delay to repair hours is higher than the standard, potentially impacting the overall efficiency of the wind farm.<br />
                    - The availability of wind turbine power percentage is excellent, indicating minimal downtime for power generation.<br />
                    - The operations and maintenance cost per kW per year is lower than average, which is beneficial for the overall financial feasibility of the wind farm.<br />
                    - The expected downtime per year is higher than desired, impacting the continuous energy production.<br />
                    - The annual energy production exceeds the standard, providing higher output potential for the wind farm.<br /><br />
                    Recommendations: Overall, this location shows promise for a wind farm considering its high availability of wind turbine power, lower operations and maintenance costs, and higher annual energy production. However, the higher expected delay to repair hours and downtime per year should be carefully evaluated to assess their potential impact on the overall efficiency and profitability of the wind farm.
                    <br />
                    </text></div>

                    <br/>
                    <br/>

                    <MessageList
                        className='message-list'
                        lockable={true}
                        toBottomHeight={'100%'}
                        dataSource={[
                        {
                        position:"left",
                        type:"text",
                        title:"PengWindGPT",
                        text:"Let me know if you have any questions!",
                        },
                        {
                        position:"right",
                        type:"text",
                        title:"You",
                        text:"In the area selected, how much higher is the O&M cost compared to the average value?",
                        },
                        {
                        position:"left",
                        type:"text",
                        title:"PengWindGPT",
                        text:"Area selected: £20 higher than the average O&M cost per kilowatt per year.",
                        },
                        ]}
                    />

                    <br />
                    <br />
                    <Input
                        placeholder="Type here..."
                        multiline={true}
                    />
                </div>

            
                

            </div>
        </body>
    )
};

export { IndepthComponent };


