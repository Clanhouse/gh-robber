import React from 'react';
import TextInput from '../TextInput/TextInput';
import Dropdown from '../Dropdown/Dropdown';
import RangeInput from '../RangeInput/RangeInput';

import { LangSearchByRepoView } from '../../../i18n/ENG';

const SearchByRepoView = ({ saveInput }) => {
    //list of technologies avalible to search - temporary. Needs to be fetched from server
    const technologiesArr = ['JavaScript', 'Python', 'C#', 'COBOL'];

    const { repositoryName, technology, minStarsCount, maxStarsCount } = LangSearchByRepoView;

    return(
        <div>
            <TextInput label={repositoryName} passInput={data => saveInput(data)} />
            <Dropdown label={technology} 
                      optionsArray={technologiesArr}
                      passInput={data => saveInput(data)}/>
            <RangeInput label={minStarsCount}
                        passInput={data => saveInput(data)}
                        minValue={1}
                        maxValue={100}
                        valueStep={10} />
            <RangeInput label={maxStarsCount}
                        passInput={data => saveInput(data)}
                        minValue={1}
                        maxValue={100}
                        valueStep={10} />
        </div>
    );
};

export default SearchByRepoView;