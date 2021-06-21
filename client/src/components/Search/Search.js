import React, { useState } from 'react';
import { SearchWrapper } from './Search.styles';

import { URL_USERS_REQUEST_githubUsers } from '../../URLs/URLs';

import SearchByRepoView from './SearchByRepoView/SearchByRepoView';
import SearchByUserView from './SearchByUserView/SearchByUserView';
import SubmitButton from '../UIElements/SubmitButton/SubmitButton';
import DoubleOptionToggleSwitch from '../UIElements/DoubleOptionToggleSwitch/DoubleOptionToggleSwitch';

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

    const toggleSearchType = () => {
        if(searchType === 'user') {
            setSearchType('repository')
        } else {
            setSearchType('user')
        }
    };

    const saveInputHandler = (event) => {
        const targetVal = event.target.value;
        console.log('saveInputHandler', targetVal, event.target.id);
        switch(event.target.id) {
            case 'Github nick':
                return setSearchGithubNick(targetVal);
            case 'Min repository count':
                return setSearchMinRepoCount(targetVal);
            case 'Max repository count':
                return setSearchMaxRepoCount(targetVal);
            case 'Repository name': 
                return setSearchRepoName(targetVal);
            case 'technology':
                return setSearchTech(targetVal);
            case 'Min stars count':
                return setSearchMinStarsCount(targetVal);
            case 'Max stars count':
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
                repositoriesCountMax: searchMaxRepoCount
            };
            //temporary we need to use fetch instead of axios because of cors policy
            fetch(URL_USERS_REQUEST_githubUsers, {
                method: 'POST', // *GET, POST, PUT, DELETE, etc.
                mode: 'no-cors', // no-cors, *cors, same-origin
                cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
                credentials: 'same-origin', // include, *same-origin, omit
                headers: {
                  'Content-Type': 'application/json'
                  // 'Content-Type': 'application/x-www-form-urlencoded',
                },
                redirect: 'follow', // manual, *follow, error
                referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
                body: JSON.stringify(requestObject) // body data type must match "Content-Type" header
              })
            .then(res => console.log('responseeee', res))
            .catch(e => console.log(e));
        } else if (searchType === 'repository') {
            requestObject = {
                name: searchRepoName,
                technology: searchTech,
                starsMin: searchMinStarsCount,
                starsMax: searchMaxStarsCount
            }
            console.log('send request', requestObject);
        }

    };

    return(
        <SearchWrapper>
            <p>Search by {searchType}</p>
            <DoubleOptionToggleSwitch 
                labelFirst='Click to search by repo'
                labelSecond='Click to search by user'
                taskFunktion={() => toggleSearchType()} 
            />
            {printContent(searchType)}
            <SubmitButton label='Search' taskFuntion={() => sendSearchRequest()}/>
        </SearchWrapper>
    );
};

export default Search;