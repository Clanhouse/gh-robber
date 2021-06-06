import React, { useContext } from 'react';
import { Redirect } from 'react-router-dom';
import { UserContext } from '../../Context/authProvider';


const Dashboard = () => {

    const { context } = useContext(UserContext);

    console.log(context.user);

    const printContent = () => {
            return(
                <>
                    <h1>Success!</h1>
                    <p>your email: {context.user.userEmail}</p>
                </>
            );
    };

    return(
        <div>
            {context.user ? printContent() : <Redirect to='/' />}
        </div>
    );
};

export default Dashboard;