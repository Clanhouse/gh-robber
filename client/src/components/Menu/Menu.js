import React, { useState, useEffect, useContext } from 'react';
import { Link, useHistory } from 'react-router-dom';
import { UserContext } from '../../Context/authProvider';
import { useIdleTimer } from 'react-idle-timer'

import { GoogleLogout, useGoogleLogout } from 'react-google-login';

import { MenuWrapper } from './Menu.styles';

import { LangMenu } from '../../i18n/ENG';

const Menu = () => {
    const { logInUser } = useContext(UserContext);
    const howMuchTime = 1000 * 62; //here we set how much time does user have until logout
    const [timeLeftMinutes, setTimeLeftMinutes] = useState(Math.floor(howMuchTime / 60000));
    const [timeLeftSeconds, setTimeLeftSeconds] = useState(parseInt(((howMuchTime % 60000) / 1000).toFixed(0)));
    const googleClientID = '420218048324-i18dme6ipl1mj6jbjcra2ft4v83v26d4.apps.googleusercontent.com';

    let history = useHistory();
    const logOut = () => {
        logInUser({ user: null });
        history.push('/');
    };

    const { signOut, loaded } = useGoogleLogout({
        onFailure: (e) => console.log(e),
        clientId: googleClientID,
        onLogoutSuccess: () => logOut(),
      });


    useEffect(() => {
        const countdownInterval = setInterval(() => {
            const minutes = Math.floor(getRemainingTime() / 60000);
            const seconds = parseInt(((getRemainingTime() % 60000) / 1000).toFixed(0));
            setTimeLeftMinutes(minutes);
            setTimeLeftSeconds(seconds === 60 ? 59 : seconds);
            console.log('odliczanie')
        }, 1000);
        return () => clearInterval(countdownInterval);
    }, [timeLeftSeconds, timeLeftMinutes]);

    const { link1, timer } = LangMenu;

    const handleOnIdle = event => {
        signOut();
      };
    
      const { getRemainingTime, getLastActiveTime } = useIdleTimer({
        timeout: howMuchTime,
        onIdle: handleOnIdle,
        debounce: 500
      });

    return(
        <MenuWrapper>
            <Link to='dashboard/search'>{link1}</Link>
            <GoogleLogout
                clientId={googleClientID}
                buttonText="Logout"
                onLogoutSuccess={logOut}
            />
            <p>{timer}</p>
            <p>{timeLeftMinutes}:{timeLeftSeconds < 10 ? `0${timeLeftSeconds}` : timeLeftSeconds}</p>
        </MenuWrapper>
    );
};

export default Menu;