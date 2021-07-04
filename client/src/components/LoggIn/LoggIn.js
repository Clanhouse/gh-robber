import React, { useContext } from 'react';
import { useHistory } from 'react-router-dom';
import { Wrapper, LoginWindow } from './LogIn.styles';
import { UserContext } from '../../Context/authProvider';

import GoogleLogin from 'react-google-login';

import { LangLoggIn } from '../../i18n/ENG';

const LoggIn = () => {
    const { logInUser, context } = useContext(UserContext);

    let history = useHistory();

    const { mainLabel, secondLabel, googleButtonLabel } = LangLoggIn;

    const responseGoogle = (response) => {
        logInUser({
            user: {
                userEmail: response.profileObj.email,
                userID: response.googleId,
                userName: response.profileObj.name,
                accessToken: response.accessToken
            }
        });
        history.push('/dashboard');
    };


    return(
        <Wrapper>
            <LoginWindow>
                <h1>{mainLabel}</h1>
                <p>{secondLabel}</p>
                <GoogleLogin 
                    clientId="420218048324-i18dme6ipl1mj6jbjcra2ft4v83v26d4.apps.googleusercontent.com"
                    buttonText={googleButtonLabel}
                    onSuccess={responseGoogle}
                    onFailure={responseGoogle}
                    cookiePolicy={'single_host_origin'}
                    isSignedIn={true}
                />
            </LoginWindow>
        </Wrapper>
    );
};

export default LoggIn;