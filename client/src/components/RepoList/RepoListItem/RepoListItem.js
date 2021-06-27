import React from 'react';
import { RepoListItemWrapper, RepoListItemItems } from './RepoListItem.styles';

import { LangRepoListItem } from '../../../i18n/ENG';

const RepoListItem = ({ username, repositories_count }) => {
    const { label1, label2 } = LangRepoListItem;
    
    return(
        <RepoListItemWrapper>
            <RepoListItemItems>{label1}{username}</RepoListItemItems>
            <RepoListItemItems>{label2}{repositories_count}</RepoListItemItems>
        </RepoListItemWrapper>
    );
};

export default RepoListItem;