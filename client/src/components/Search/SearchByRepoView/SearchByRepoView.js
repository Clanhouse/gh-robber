import React from 'react';
import TextInput from '../TextInput/TextInput';
import Dropdown from '../Dropdown/Dropdown';
import RangeInput from '../RangeInput/RangeInput';

const SearchByRepoView = () => {
    return(
        <div>
            <TextInput />
            <Dropdown />
            <RangeInput />
        </div>
    );
};

export default SearchByRepoView;