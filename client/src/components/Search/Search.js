import React, { useState } from 'react';
import { SearchWrapper } from './Search.styles';

import { URL_USERS_REQUEST_githubUsers_test } from '../../URLs/URLs';

import SearchByRepoView from './SearchByRepoView/SearchByRepoView';
import SearchByUserView from './SearchByUserView/SearchByUserView';
import SubmitButton from '../UIElements/SubmitButton/SubmitButton';
import DoubleOptionToggleSwitch from '../UIElements/DoubleOptionToggleSwitch/DoubleOptionToggleSwitch';

import { LangSearch, LangSearchByRepoView, LangSearchByUserView } from '../../i18n/ENG';

const Search = () => {
    //we can search by user or by repo
    const [searchType, setSearchType] = useState('user');
    const [searchGithubNick, setSearchGithubNick] = useState(null);
    const [searchMinRepoCount, setSearchMinRepoCount] = useState(null);
    const [searchMaxRepoCount, setSearchMaxRepoCount] = useState(null);
    const [searchRepoName, setSearchRepoName] = useState(null);
    const [searchTech, setSearchTech] = useState(null);
    const [searchMinStarsCount, setSearchMinStarsCount] = useState(null);
    const [searchMaxStarsCount, setSearchMaxStarsCount] = useState(null);

    const { searchBy, toggleSwitchLabelFirst, toggleSwitchLabelSecond, submitButton } = LangSearch;
    const { repositoryName, technology, minStarsCount, maxStarsCount } = LangSearchByRepoView;
    const { githubNick, minRepoCount, maxRepoCount } = LangSearchByUserView;

    const toggleSearchType = () => {
        if(searchType === 'user') {
            setSearchType('repository')
        } else {
            setSearchType('user')
        }
    };

    const saveInputHandler = (event) => {
        const targetVal = event.target.value;
        switch(event.target.id) {
            case githubNick:
                return setSearchGithubNick(targetVal);
            case minRepoCount:
                return setSearchMinRepoCount(targetVal);
            case maxRepoCount:
                return setSearchMaxRepoCount(targetVal);
            case repositoryName: 
                return setSearchRepoName(targetVal);
            case technology:
                return setSearchTech(targetVal);
            case minStarsCount:
                return setSearchMinStarsCount(targetVal);
            case maxStarsCount:
                return setSearchMaxStarsCount(targetVal);
            default:
                return null;
        }
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
    };

    const sendSearchRequest = () => {
        let requestObject = {};
        if(searchType === 'user') {
            requestObject = {
                username: searchGithubNick,
                repositoriesCountMin: searchMinRepoCount,
                repositoriesCountMax: searchMaxRepoCount,
                offset: 1,
                resultsNum: 5,

            };
            //temporary we need to use fetch instead of axios because of cors policy
            fetch(URL_USERS_REQUEST_githubUsers_test, {
                method: 'POST', // *GET, POST, PUT, DELETE, etc.
                mode: 'no-cors', // no-cors, *cors, same-origin
                cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
                credentials: 'same-origin', // include, *same-origin, omit
                headers: {
                  'Content-Type': 'application/json',
                  'Accept': 'application/json'
                  // 'Content-Type': 'application/x-www-form-urlencoded',
                },
                redirect: 'follow', // manual, *follow, error
                referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
                body: JSON.stringify(requestObject) // body data type must match "Content-Type" header
              })
            .then(res => console.log('response', res))
            .catch(e => console.log(e));
        } else if (searchType === 'repository') {
            requestObject = {
                name: searchRepoName,
                technology: searchTech,
                starsMin: searchMinStarsCount,
                starsMax: searchMaxStarsCount
            }
        }

    };

    return(
        <SearchWrapper>
            <p>{searchBy}{searchType}</p>
            <DoubleOptionToggleSwitch 
                labelFirst={toggleSwitchLabelFirst}
                labelSecond={toggleSwitchLabelSecond}
                taskFunction={() => toggleSearchType()} 
            />
            {printContent(searchType)}
            <SubmitButton label={submitButton} taskFunction={() => sendSearchRequest()}/>
        </SearchWrapper>
    );
};

export default Search;