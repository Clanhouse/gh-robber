import { BrowserRouter, Route } from "react-router-dom";
import { theme } from "./styles/Theme";
import { ThemeProvider } from "styled-components";

import { routes } from "./routes/routes";
import FavoriteProvider from "./context/FavoriteUser/FavoriteUsers.provider";
import AuthProvider from "./context/Auth/authProvider";

const App = () => {
  return (
    <BrowserRouter>
      <AuthProvider>
        <ThemeProvider theme={theme}>
          <FavoriteProvider>
            <Route exact path="/" component={routes.home} />
            <Route path="/login" component={routes.login} />
            <Route path="/dashboard" component={routes.dashboard} />
          </FavoriteProvider>
        </ThemeProvider>
      </AuthProvider>
    </BrowserRouter>
  );
};

export default App;
