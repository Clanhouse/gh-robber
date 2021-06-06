import React, { useContext } from 'react';
import { Redirect } from 'react-router-dom';
import { UserContext } from '../../Context/authProvider';

import { Container } from './Dashboard.styles';
import Menu from '../Menu/Menu';
import RepoList from '../RepoList/RepoList';


const Dashboard = () => {

    const { context } = useContext(UserContext);

    console.log(context.user);

    const printContent = () => {
            return(
                <Container>
                    <Menu />
                    <RepoList />
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