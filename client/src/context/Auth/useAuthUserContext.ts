import { useContext } from "react";
import { AuthUserContext } from "./authProvider";

const useAuthUserContext = () => {
  const context = useContext(AuthUserContext);

  if (!context) {
    throw new Error(
      "User context can be used only within the UserContext.Provider."
    );
  }

  return context;
};

export default useAuthUserContext;
