import React, { useContext, useState } from 'react';
import Router from 'next/router';
import { UserContext } from '../../../context/contextProvider';

const Login = () => {
    const [userEmail, setUserEmail] = useState('');
    const [userPassword, setUserPassword] = useState('');

    const { logInUser } = useContext(UserContext);

    const logInHandler = (e) => {
        e.preventDefault();
        logInUser({
            user: {
                userEmail: userEmail,
                userPassword: userPassword
            }
        });
        Router.push('/dashboard');
    }

    return(
        <div>
            <h1>Zaloguj sie</h1>
            <form onSubmit={(event) => logInHandler(event)}>
                <input type="userEmail" placeholder="email"
                onChange={(event) => setUserEmail(event.target.value)}
                value={userEmail} />
                <input type="password" placeholder="password"
                onChange={(event) => setUserPassword(event.target.value)}
                value={userPassword} />
                <button type="submit">Zaloguj</button>
            </form>
        </div>
    );
};

export default Login;