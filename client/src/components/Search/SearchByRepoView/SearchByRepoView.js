import React from 'react';
import TextInput from '../TextInput/TextInput';
import Dropdown from '../Dropdown/Dropdown';
import RangeInput from '../RangeInput/RangeInput';

const SearchByRepoView = ({ saveInput }) => {

    const technologiesArr = ['JavaScript', 'Python', 'C#', 'COBOL'];

    return(
        <div>
            <TextInput label='Repository name' passInput={data => saveInput(data)} />
            <Dropdown label='technology' 
                      optionsArray={technologiesArr}
                      passInput={data => saveInput(data)}/>
            <RangeInput label='Stars count'
                        passInput={data => saveInput(data)}
                        minValue={1}
                        maxValue={100}
                        valueStep={10} />
        </div>
    );
};

export default SearchByRepoView;