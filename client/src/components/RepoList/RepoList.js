import React, { useEffect, useState, useContext } from 'react';
import { RepoListWrapper, RepoListView } from './RepoList.styles';

import { usersGithubUsers } from '../../dummyData/usersGithubUsers';
import { UserContext } from '../../Context/authProvider';

import RepoListItem from './RepoListItem/RepoListItem';

const RepoList = () => {
    const [viewGithubUsers, setViewGithubUsers] = useState([]);
    const { context } = useContext(UserContext);
    useEffect(() => {
        //here we will fetch data from endpoint using user ID
        if(context.user) {
            setViewGithubUsers(usersGithubUsers);
        }
    }, []);

    const generateList = () => {
        return viewGithubUsers.map( el => <RepoListItem 
                                            key={el.username}
                                            username={el.username} 
                                            repositories_count={el.repositories_count}
                                            githubUser={el}
                                          />);
    }

    return(
        <RepoListWrapper>
            <RepoListView>
                {generateList()}
            </RepoListView>
        </RepoListWrapper>
    );
};

export default RepoList;