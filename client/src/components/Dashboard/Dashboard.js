import React, { useContext } from 'react';
import { Redirect } from 'react-router-dom';
import { UserContext } from '../../Context/authProvider';

import { Container } from './Dashboard.styles';
import Menu from '../Menu/Menu';


const Dashboard = () => {

    const { context } = useContext(UserContext);

    console.log(context.user);

    const printContent = () => {
            return(
                <Container>
                    <Menu />
                    <h1>Success!</h1>
                    <p>your email: {context.user.userEmail}</p>
                </Container>
            );
    };

    return(
        <div>
            {context.user ? printContent() : <Redirect to='/' />}
        </div>
    );
};

export default Dashboard;