import React from 'react';
import { RepoListItemWrapper, RepoListItemItems } from './RepoListItem.styles';

const RepoListItem = ({ username, repositories_count }) => {
    return(
        <RepoListItemWrapper>
            <RepoListItemItems>Github nick: {username}</RepoListItemItems>
            <RepoListItemItems>Number of repositories: {repositories_count}</RepoListItemItems>
        </RepoListItemWrapper>
    );
};

export default RepoListItem;