import { createContext, useState, FunctionComponent } from "react";
import { IFavoriteContextValue } from "./FavoriteUsers.types";
import { IFavoriteUser } from "./FavoriteUsers.types";

export const FavoriteContext = createContext<IFavoriteContextValue | null>(null);

const FavoriteProvider: FunctionComponent = ({ children }) => {
  const [favoriteUsers, setFavoriteUsers] = useState<IFavoriteUser[]>([]);

  const addFavorite = (user: IFavoriteUser) => {
    if (favoriteUsers.includes(user)) {
      return;
    }

    setFavoriteUsers((prevFavoriteUsers) => {
      return [...prevFavoriteUsers, user];
    });
  };

  const removeFavorite = (user: IFavoriteUser) => {
    const updatedFavorites = favoriteUsers.filter((fav) => fav.id !== user.id);
    setFavoriteUsers(updatedFavorites);
  };

  const value: IFavoriteContextValue = [favoriteUsers, addFavorite, removeFavorite];

  return (
    <FavoriteContext.Provider value={value}>{children}</FavoriteContext.Provider>
  );
};

export default FavoriteProvider;
