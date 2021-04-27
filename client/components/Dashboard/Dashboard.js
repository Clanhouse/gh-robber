import React, { useContext } from 'react';
import { UserContext } from '../../context/contextProvider';

const Dashboard = () => {

    const { context } = useContext(UserContext);

    console.log(context.user);

    const printContent = () => {
        if(context.user) {
            return(
                <>
                    <h1>Zalogowałeś się!</h1>
                    <p>twój email: {context.user.userEmail}</p>
                </>
            );
        }
        if(context.user === null) {
            return(
                <h1>Jesteś niezalogowany :(</h1>
            );
        }
    };

    return(
        <div>
            {printContent()}
        </div>
    )
};

export default Dashboard;