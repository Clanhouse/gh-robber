import { createContext, useState, FunctionComponent } from "react";
import { IUserContextValue, IUser } from "./AuthUserContext.types";

export const AuthUserContext = createContext<IUserContextValue | null>(null);

const AuthProvider: FunctionComponent = ({ children }) => {
  const [user, setUser] = useState<IUser>(null);

  const value: IUserContextValue = [user, setUser];

  return (
    <AuthUserContext.Provider value={value}>{children}</AuthUserContext.Provider>
  );
};

export default AuthProvider;
