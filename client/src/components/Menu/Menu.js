import React, { useContext } from 'react';
import { Link, useHistory } from 'react-router-dom';
import { UserContext } from '../../Context/authProvider';

import { GoogleLogout } from 'react-google-login';

import { MenuWrapper } from './Menu.styles';

import { LangMenu } from '../../i18n/ENG';

const Menu = () => {
    const { logInUser } = useContext(UserContext);
    let history = useHistory();
    const logOut = () => {
        logInUser({ user: null });
        history.push('/');
    };

    const { link1, link2 } = LangMenu;

    return(
        <MenuWrapper>
            <Link to='dashboard/search'>{link1}</Link>
            <GoogleLogout
                clientId="420218048324-i18dme6ipl1mj6jbjcra2ft4v83v26d4.apps.googleusercontent.com"
                buttonText="Logout"
                onLogoutSuccess={logOut}
            />
            <Link to='dashboard/favorites'>{link2}</Link>
        </MenuWrapper>
    );
};

export default Menu;