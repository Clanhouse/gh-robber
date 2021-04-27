import React, { createContext, useState, useEffect } from 'react';

export const UserContext = createContext();

const ContextProvider = ({children}) => {
    const [context, setUser] = useState({ user: null });

    useEffect(() => {
        //here we going to put authentication function when it will be avalible on backend. It will be mutating user.
        //whole this component will need major changes :)
    }, []);

    const logInUser = (input) => {
        setUser(input);
    };

    return(
        <UserContext.Provider value={{context, logInUser}}>
            {children}
        </UserContext.Provider>
    );
};

export default ContextProvider;