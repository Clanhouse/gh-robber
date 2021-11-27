import useFavoriteUsers from "../../../context/FavoriteUser/useFavoriteUsers";
import { FavoriteWrapper, FavoriteItem } from "./FavoriteList.style";

const FavoriteList = () => {
  const [favoriteUsers] = useFavoriteUsers();

  return (
    <FavoriteWrapper>
      <h1>Favorities Users</h1>
      <ul>
        {favoriteUsers.map((user) => (
          <FavoriteItem key={user.id}>{user.username}</FavoriteItem>
        ))}
      </ul>
    </FavoriteWrapper>
  );
};

export default FavoriteList;
