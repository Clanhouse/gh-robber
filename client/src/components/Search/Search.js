import React, { useState } from 'react'
import { SearchWrapper } from './Search.styles';

import SearchByRepoView from './SearchByRepoView/SearchByRepoView';
import SearchByUserView from './SearchByUserView/SearchByUserView';
import SubmitButton from '../UIElements/SubmitButton/SubmitButton';
import DoubleOptionToggleSwitch from '../UIElements/DoubleOptionToggleSwitch/DoubleOptionToggleSwitch';

const Search = () => {
    //we can search by user or by repo
    const [searchType, setSearchType] = useState('user');
    const [searchGithubNick, setSearchGithubNick] = useState(null);
    const [searchRepoCount, setSearchRepoCount] = useState(null);
    const [searchRepoName, setSearchRepoName] = useState(null);
    const [searchTech, setSearchTech] = useState(null);
    const [searchStarsCount, setSearchStarsCount] = useState(null);

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
            case 'Repository count':
            return setSearchRepoCount(targetVal);
            case 'Repository name': 
            return setSearchRepoName(targetVal);
            case 'technology':
            return setSearchTech(targetVal);
            case 'Stars count':
            return setSearchStarsCount(targetVal);
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
                repositoriesCountMin: searchRepoCount,
                repositoriesCountMax: searchRepoCount
            }
        } else if (searchType === 'repository') {
            requestObject = {
                name: searchRepoName,
                technology: searchTech,
                starsMin: searchStarsCount,
                starsMax: searchStarsCount
            }
        }

        console.log('send request', requestObject);
    };

    return(
        <SearchWrapper>
            <p>Search by {searchType}</p>
            <DoubleOptionToggleSwitch 
                labelFirst='Change to search by repo'
                labelSecond='Change to search by user'
                taskFunktion={() => toggleSearchType()} 
            />
            {printContent(searchType)}
            <SubmitButton label='Search' taskFuntion={() => sendSearchRequest()}/>
        </SearchWrapper>
    );
};

export default Search;