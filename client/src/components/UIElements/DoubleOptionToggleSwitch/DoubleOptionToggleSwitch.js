import React, { useState } from 'react';

const DoubleOptionToggleSwitch = ({ labelFirst, labelSecond, taskFunction }) => {
    //true is option 1, false option 2
    const [switchState, setSwitchState] = useState(true);
    const toggleHandler = () => {
        setSwitchState(!switchState);
        taskFunction();
    };
    return(
        <div onClick={() => toggleHandler()}>
            <p>{switchState ? labelFirst : labelSecond }</p>
        </div>
    );
};

export default DoubleOptionToggleSwitch;