import React from 'react';

import { LangDropdown } from '../../../i18n/ENG';

const Dropdown = ({ label, optionsArray, passInput }) => {

    const { mainLabel } = LangDropdown;

    const optionsGenerator = (options) => {
        return options.map( option => <option   key={option}
                                                value={option}>
                                                {option}</option>);
    };

    return(
        <>
            <label htmlFor={label}>{mainLabel}{label}:</label>
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