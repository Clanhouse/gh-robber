import { useContext } from "react";
import { FavoriteContext } from "./FavoriteUsers.provider";

const useFavoriteUsers = () => {
  const context = useContext(FavoriteContext);

  if (!context) {
    throw new Error(
      "Favorite contex can be used only within the FavoriteContext.Provider."
    );
  }

  return context;
};

export default useFavoriteUsers;
