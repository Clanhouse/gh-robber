import React, { useContext } from 'react';
import { Redirect, Route, useRouteMatch } from 'react-router-dom';
import { UserContext } from '../../Context/authProvider';

import { Container } from './Dashboard.styles';
import Menu from '../Menu/Menu';
import { dashboardRoutes } from '../../Router/Routes';


const Dashboard = () => {

    const { path } = useRouteMatch();

    const { context } = useContext(UserContext);

    console.log('logged user', context.user);

    const printContent = () => {
            return(
                <Container>
                    <Menu />
                    <Route exact path={`${path}`} component={dashboardRoutes.repolist} />
                    <Route path={`${path}/search`} component={dashboardRoutes.search} />                    
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