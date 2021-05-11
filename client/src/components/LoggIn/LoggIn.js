import React, { useContext, useState } from 'react';
import { useHistory } from 'react-router-dom';
import { Wrapper } from './LogIn.styles';
import { UserContext } from '../../Context/authProvider';

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
    }
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
        </Wrapper>
    );
};

export default LoggIn;