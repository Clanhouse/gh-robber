import React from 'react';
import { BrowserRouter, Route } from 'react-router-dom';
import { theme } from './styles/Theme';
import { ThemeProvider } from 'styled-components';

import { routes } from './Router/Routes';
import AuthProvider from './Context/authProvider';

const App = () => {
  return (
      <BrowserRouter>
        <AuthProvider>
          <ThemeProvider theme={theme}>
            <Route exact path="/" component={routes.loggin} />
            <Route path="/dashboard" component={routes.dashboard} />
          </ThemeProvider>
        </AuthProvider>
      </BrowserRouter>
  );
}

export default App;
