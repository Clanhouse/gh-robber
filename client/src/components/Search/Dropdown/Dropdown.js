import React from 'react';

const Dropdown = ({ label, optionsArray, passInput }) => {

    const optionsGenerator = (options) => {
        return options.map( option => <option   key={option}
                                                value={option}>
                                                {option}</option>);
    };

    return(
        <>
            <label htmlFor={label}>Choose a {label}:</label>
            <select name={label} 
                    id={label} 
                    form={label}
                    onChange={event => passInput(event)}>
                {optionsGenerator(optionsArray)}
            </select>
        </>
    );
};

export default Dropdown;