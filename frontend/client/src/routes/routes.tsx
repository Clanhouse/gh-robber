import Dashboard from "../components/Dashboard/Dashboard";
import Login from "../components/Login/Login";
import Search from "../components/Search/Search";
import RepoList from "../components/RepoList/RepoList";
import FavoriteList from "../components/Favorites/FavoriteList/FavoriteList";
import Home from "../components/Home/Home";
import { ReactLocation, Route } from "react-location";

export const routes: Route[] = [
  { path: "/", element: () => <div>home!</div> },
  { path: "login", element: <div>login</div> },
  {
    path: "dashboard",
    children: [
      {
        path: "repolist",
        element: <div>RepoList</div>,
      },
      {
        path: "search",
        element: <div>Search</div>,
      },
      {
        path: "favorites",
        element: <div>FavoriteList</div>,
      },
    ],
  },
];

export const location = new ReactLocation();
