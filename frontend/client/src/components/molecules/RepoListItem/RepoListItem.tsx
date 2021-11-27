import { FunctionComponent } from "react";
import { RepoListItemWrapper, RepoListItemItems } from "./RepoListItem.styles";
import AddFavorite from "../Favorites/AddFavorite/AddFavorite";

import { LangRepoListItem } from "../../i18n/ENG";
import { IFavoriteUser } from "../../context/FavoriteUser/FavoriteUsers.types";

type IRepoListItemProps = {
  user: IFavoriteUser;
};

const RepoListItem: FunctionComponent<IRepoListItemProps> = ({ user }) => {
  const { label1, label2 } = LangRepoListItem;

  return (
    <RepoListItemWrapper>
      <RepoListItemItems>
        {label1}
        {user.username}
      </RepoListItemItems>
      <RepoListItemItems>
        {label2}
        {user.repositories_count}
      </RepoListItemItems>
      <AddFavorite user={user} />
    </RepoListItemWrapper>
  );
};

export default RepoListItem;
