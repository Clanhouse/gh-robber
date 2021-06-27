import React, { useContext } from 'react';
import { useHistory } from 'react-router-dom';
import { Wrapper, LoginWindow } from './LogIn.styles';
import { UserContext } from '../../Context/authProvider';

import GoogleLogin from 'react-google-login';

const LoggIn = () => {
    const { logInUser, context } = useContext(UserContext);

    let history = useHistory();

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
                <h1>Welcome to Github Robber!</h1>
                <p>Please, log in using Your google Account</p>
                <GoogleLogin 
                    clientId="420218048324-i18dme6ipl1mj6jbjcra2ft4v83v26d4.apps.googleusercontent.com"
                    buttonText="Login"
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