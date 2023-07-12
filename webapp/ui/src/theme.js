import { createTheme } from "@mui/material/styles";

export const theme = createTheme({
  palette: {
    primary: {
      light: '#7bc8f6',
      main: 'rgba(20, 104, 153)'
    },
    secondary: {
      light: 'rgba(255, 245, 128)',
      main: 'rgba(222, 212, 0)',
      dark: 'rgba(153, 131, 0)'
    },
    error: {
      main: 'rgba(255, 91, 61)'
    },
    black: {
      main: 'rgba(37, 31, 27)'
    }
  },
  breakpoints: {
    values: {
      xs: 0,
      sm: 600,
      md: 900,
      lg: 1200,
      xl: 1536,
      xxl: 1860
    }
  }
});
