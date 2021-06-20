import React from 'react';

const SubmitButton = ({ label, taskFuntion }) => {
    return(
        <button onClick={() => taskFuntion()}>{label}</button>
    );
};

export default SubmitButton;