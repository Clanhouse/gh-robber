import { Router, Outlet } from "react-location";

import FavoriteProvider from "./context/FavoriteUser/FavoriteUsers.provider";
import AuthProvider from "./context/Auth/authProvider";
import { routes, location } from "./routes";

const App = () => {
  return (
    <Router routes={routes} location={location}>
      <AuthProvider>
        <FavoriteProvider>
          <Outlet />
        </FavoriteProvider>
      </AuthProvider>
    </Router>
  );
};

export default App;
