export type IFavoriteUser = {
  id: string;
  username: string;
  repositories_count: number;
};

export type IFavoriteContextValue = [
  Array<IFavoriteUser>,
  (user: IFavoriteUser) => void,
  (user: IFavoriteUser) => void
];
