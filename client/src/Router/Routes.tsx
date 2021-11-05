import Dashboard from "../components/Dashboard/Dashboard";
import Login from "../components/Login/Login";
import Search from "../components/Search/Search";
import RepoList from "../components/RepoList/RepoList";
import FavoriteList from "../components/Favorites/FavoriteList/FavoriteList";

export const routes = {
  login: () => <Login />,
  dashboard: () => <Dashboard />,
};

export const dashboardRoutes = {
  repolist: () => <RepoList />,
  search: () => <Search />,
  favorites: () => <FavoriteList />,
};
