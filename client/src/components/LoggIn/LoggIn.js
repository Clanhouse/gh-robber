import React, { useContext, useState } from 'react';
import { useHistory } from 'react-router-dom';
import { Wrapper } from './LogIn.styles';
import { UserContext } from '../../Context/authProvider';

import GoogleLogin from 'react-google-login';

const LoggIn = () => {
    const [userEmail, setUserEmail] = useState('');
    const [userPassword, setUserPassword] = useState('');

    const { logInUser } = useContext(UserContext);

    let history = useHistory();

    const logInHandler = (e) => {
        e.preventDefault();
        logInUser({
            user: {
                userEmail: userEmail,
                userPassword: userPassword
            }
        });
        history.push('/dashboard');
    };

    const responseGoogle = (response) => {
        console.log(response.googleId);
        logInUser({
            user: {
                userEmail: response.googleId,
                userPassword: null,
            }
        });
        history.push('/dashboard');
    };


    return(
        <Wrapper>
            <h1>Logg In</h1>
            <form onSubmit={(event) => logInHandler(event)}>
                <input type="userEmail" placeholder="email"
                onChange={(event) => setUserEmail(event.target.value)}
                value={userEmail} />
                <input type="password" placeholder="password"
                onChange={(event) => setUserPassword(event.target.value)}
                value={userPassword} />
                <button type="submit">Logg In</button>
            </form>
            <p>or</p>
            <GoogleLogin 
                clientId="420218048324-i18dme6ipl1mj6jbjcra2ft4v83v26d4.apps.googleusercontent.com"
                buttonText="Login"
                onSuccess={responseGoogle}
                onFailure={responseGoogle}
                cookiePolicy={'single_host_origin'}
            />
        </Wrapper>
    );
};

export default LoggIn;