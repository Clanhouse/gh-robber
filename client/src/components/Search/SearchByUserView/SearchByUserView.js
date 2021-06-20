import React from 'react';
import TextInput from '../TextInput/TextInput';
import RangeInput from '../RangeInput/RangeInput';

const SearchByUserView = ({ saveInput }) => {
    return(
        <div>
            <TextInput label='Github nick' passInput={data => saveInput(data)}/>
            <RangeInput label='Repository count'
                        passInput={data => saveInput(data)}
                        minValue={1}
                        maxValue={100}
                        valueStep={10} />
        </div>
    );
};

export default SearchByUserView;