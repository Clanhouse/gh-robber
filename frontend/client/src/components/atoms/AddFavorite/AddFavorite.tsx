import { FunctionComponent } from "react";
import { IFavoriteUser } from "../../../context/FavoriteUser/FavoriteUsers.types";
import useFavoriteUsers from "../../../context/FavoriteUser/useFavoriteUsers";

const FavoriteIcon = () => <span>Un-Favorite</span>;
const FavoriteBorderIcon = () => <span>Favorite</span>;

type IFavoriteButtonProps = {
  user: IFavoriteUser;
};

const AddFavorite: FunctionComponent<IFavoriteButtonProps> = ({ user }) => {
  const [favoriteUsers, addFavorite, removeFavorite] = useFavoriteUsers();
  const isFavorite = favoriteUsers.map((fav) => fav.id).includes(user.id.toString());

  const toggleFavorites = (user: IFavoriteUser) => {
    isFavorite ? removeFavorite(user) : addFavorite(user);
  };

  return (
    <div>
      <input
        type="checkbox"
        name=""
        id=""
        checked={isFavorite}
        onClick={() => toggleFavorites(user)}
      />
      {isFavorite ? <FavoriteIcon /> : <FavoriteBorderIcon />}
    </div>
  );
};

export default AddFavorite;
