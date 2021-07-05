import Dashboard from '../components/Dashboard/Dashboard';
import LoggIn from '../components/LoggIn/LoggIn';
import Search from '../components/Search/Search';
import RepoList from '../components/RepoList/RepoList';
import FavoriteList from '../components/Favorites/FavoriteList/FavoriteList';

export const routes = {
    loggin: () => <LoggIn />,
    dashboard: () => <Dashboard />,
};

export const dashboardRoutes = {
    repolist: () => <RepoList />,
    search: () => <Search />,
    favorites: () => <FavoriteList />
};
  