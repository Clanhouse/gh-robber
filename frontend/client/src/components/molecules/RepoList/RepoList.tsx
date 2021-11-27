import { useEffect, useState } from "react";
import { RepoListWrapper, RepoListView } from "./RepoList.styles";

import { usersGithubUsers } from "../../dummyData/usersGithubUsers";

import RepoListItem from "../RepoListItem/RepoListItem";
import useAuthUserContext from "../../context/Auth/useAuthUserContext";

const RepoList = () => {
  const [viewGithubUsers, setViewGithubUsers] = useState<typeof usersGithubUsers>(
    []
  );
  const [user] = useAuthUserContext();

  useEffect(() => {
    //here we will fetch data from endpoint using user ID
    if (!user) {
      return;
    }
    setViewGithubUsers(usersGithubUsers);
  }, [user]);

  const generateList = () => {
    return viewGithubUsers.map((el) => {
      const user = { ...el, id: el.id.toString() };

      return <RepoListItem key={el.username} user={user} />;
    });
  };

  return (
    <RepoListWrapper>
      <RepoListView>{generateList()}</RepoListView>
    </RepoListWrapper>
  );
};

export default RepoList;
