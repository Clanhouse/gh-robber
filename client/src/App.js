import React from 'react';
import { theme } from './styles/Theme';
import { ThemeProvider } from 'styled-components';

const App = () => {
  return (
    <div className="App">
        <ThemeProvider theme={theme}>
          smt
        </ThemeProvider>
    </div>
  );
}

export default App;
