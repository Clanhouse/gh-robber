import React, { useContext } from 'react';
import { useHistory } from 'react-router-dom';
import { UserContext } from '../../Context/authProvider';

import { GoogleLogout } from 'react-google-login';

import { MenuWrapper } from './Menu.styles';

const Menu = () => {
    const { logInUser } = useContext(UserContext);
    let history = useHistory();
    const logOut = () => {
        logInUser({ user: null });
        history.push('/');
    };

    return(
        <MenuWrapper>
            menu
            <GoogleLogout
                clientId="420218048324-i18dme6ipl1mj6jbjcra2ft4v83v26d4.apps.googleusercontent.com"
                buttonText="Logout"
                onLogoutSuccess={logOut}
            />
        </MenuWrapper>
    );
};

export default Menu;