export type IGoogleUser = {
  accessToken: string;
  userEmail: string;
  userID: string;
  userName: string;
};

export type IUser = IGoogleUser | null;

export type IUserContextValue = [IUser, React.Dispatch<React.SetStateAction<IUser>>];
