import React, { useState } from 'react'
import { SearchWrapper } from './Search.styles';

import SearchByRepoView from './SearchByRepoView/SearchByRepoView';
import SearchByUserView from './SearchByUserView/SearchByUserView';

const Search = () => {
    //we can search by user or by repo
    const [searchType, setSearchType] = useState('user');

    const toggleSearchType = () => {
        if(searchType === 'user') {
            setSearchType('repository')
        } else {
            setSearchType('user')
        }
    };

    const saveInputHandler = (event) => {
        console.log('saveInputHandler', event.target.value, event.target.id)
    }

    const printContent = (typeOfSearch) => {
        switch(typeOfSearch) {
            case 'user': 
            return <SearchByUserView saveInput={(data) => saveInputHandler(data)}/>
            case 'repository':
            return <SearchByRepoView saveInput={(data) => saveInputHandler(data)}/>
            default: 
            return <SearchByUserView saveInput={(data) => saveInputHandler(data)}/>
        }
    }

    return(
        <SearchWrapper>
            <p onClick={() => toggleSearchType()}>Search by {searchType}</p>
            {printContent(searchType)}
        </SearchWrapper>
    );
};

export default Search;