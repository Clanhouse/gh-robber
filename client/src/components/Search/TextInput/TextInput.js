import React from 'react';

const TextInput = ({ label, passInput }) => {
    return(
        <>
            <label htmlFor={label}>{label}</label>
            <input  id={label} 
                    type='text' 
                    placeholder={label}
                    onChange={event => passInput(event)}></input>
        </>
    );
};

export default TextInput;