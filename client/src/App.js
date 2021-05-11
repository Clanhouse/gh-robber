import React from 'react';
import { BrowserRouter, Route } from 'react-router-dom';
import { theme } from './styles/Theme';
import { ThemeProvider } from 'styled-components';

import { routes } from './Router/Routes';

const App = () => {
  return (
    <div className="App">
      <BrowserRouter>
          <ThemeProvider theme={theme}>
            <Route exact path="/" component={routes.loggin} />
            <Route path="/dashboard" component={routes.dashboard} />
          </ThemeProvider>
      </BrowserRouter>
    </div>
  );
}

export default App;
