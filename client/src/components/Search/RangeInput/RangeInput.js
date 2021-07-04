import React from 'react';

const RangeInput = ({ label, passInput, minValue, maxValue, valueStep }) => {
    return(
        <>
            <label htmlFor={label}>{label}</label>
            <input  type='range'
                    id={label}
                    name={label}
                    min={minValue}
                    max={maxValue}
                    step={valueStep}
                    onChange={(event => passInput(event))}
                    ></input>
        </>
    );
};

export default RangeInput;