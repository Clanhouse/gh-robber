import React, { useState } from 'react';

const DoubleOptionToggleSwitch = ({ labelFirst, labelSecond, taskFunktion }) => {
    //true is option 1, false option 2
    const [switchState, setSwitchState] = useState(true);
    const toggleHandler = () => {
        setSwitchState(!switchState);
        taskFunktion();
    };
    return(
        <div onClick={() => toggleHandler()}>
            <p>{switchState ? labelFirst : labelSecond }</p>
        </div>
    );
};

export default DoubleOptionToggleSwitch;