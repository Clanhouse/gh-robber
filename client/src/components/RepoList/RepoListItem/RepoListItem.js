import React from 'react';
import { RepoListItemWrapper, RepoListItemItems } from './RepoListItem.styles';
import  AddFavorite from '../../Favorites/AddFavorite/AddFavorite';

import { LangRepoListItem } from '../../../i18n/ENG';

const RepoListItem = ({ githubUser, username, repositories_count }) => {
    const { label1, label2 } = LangRepoListItem;
    
    return(
        <RepoListItemWrapper>
            <RepoListItemItems>{label1}{username}</RepoListItemItems>
            <RepoListItemItems>{label2}{repositories_count}</RepoListItemItems>
            <AddFavorite githubUser={githubUser}/>
        </RepoListItemWrapper>
    );
};

export default RepoListItem;