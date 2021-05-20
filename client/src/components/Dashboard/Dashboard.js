import React, { useContext } from 'react';
import { UserContext } from '../../Context/authProvider';


const Dashboard = () => {

    const { context } = useContext(UserContext);

    console.log(context.user);

    const printContent = () => {
        if(context.user) {
            return(
                <>
                    <h1>Success!</h1>
                    <p>your email: {context.user.userEmail}</p>
                </>
            );
        }
        if(context.user === null) {
            return(
                <h1>Youmare not logged in :(</h1>
            );
        }
    };

    return(
        <div>
            {printContent()}
        </div>
    );
};

export default Dashboard;