import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import reportWebVitals from './reportWebVitals';

import { createTheme, ThemeProvider } from "@mui/material/styles";

const theme = createTheme({
  palette: {
    primary: {
      light: '#7bc8f6',
      main: 'rgba(20, 104, 153)'
    },
    secondary: {
      main: 'rgba(222, 212, 0)',
      dark: 'rgba(153, 131, 0)'
    },
    error: {
      main: 'rgba(255, 91, 61)'
    },
    black: {
      main: 'rgba(37, 31, 27)'
    }
  }
});

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <ThemeProvider theme={theme}>
      <App />
    </ThemeProvider>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
