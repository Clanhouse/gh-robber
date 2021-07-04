import React from 'react';
import TextInput from '../TextInput/TextInput';
import RangeInput from '../RangeInput/RangeInput';

import { LangSearchByUserView } from '../../../i18n/ENG';

const SearchByUserView = ({ saveInput }) => {
    const { githubNick, minRepoCount, maxRepoCount } = LangSearchByUserView;

    return(
        <div>
            <TextInput label={githubNick} passInput={data => saveInput(data)}/>
            <RangeInput label={minRepoCount}
                        passInput={data => saveInput(data)}
                        minValue={1}
                        maxValue={100}
                        valueStep={10} />
            <RangeInput label={maxRepoCount}
                        passInput={data => saveInput(data)}
                        minValue={1}
                        maxValue={100}
                        valueStep={10} />
        </div>
    );
};

export default SearchByUserView;