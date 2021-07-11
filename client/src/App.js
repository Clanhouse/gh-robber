import React from 'react';
import { BrowserRouter, Route } from 'react-router-dom';
import { theme } from './styles/Theme';
import { ThemeProvider } from 'styled-components';

import { routes } from './Router/Routes';
import AuthProvider from './Context/authProvider';
import FavoriteProvider  from './Context/favoriteProvider'

const App = () => {
  return (
      <BrowserRouter>
        <AuthProvider>
          <ThemeProvider theme={theme}>
            <FavoriteProvider>
              <Route exact path="/" component={routes.loggin} />
              <Route path="/dashboard" component={routes.dashboard} />
            </FavoriteProvider>
          </ThemeProvider>
        </AuthProvider>
      </BrowserRouter>
  );
}

export default App;
