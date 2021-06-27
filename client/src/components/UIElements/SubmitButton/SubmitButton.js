import React from 'react';

const SubmitButton = ({ label, taskFunction }) => {
    return(
        <button onClick={() => taskFunction()}>{label}</button>
    );
};

export default SubmitButton;