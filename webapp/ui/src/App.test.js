import { render, screen } from '@testing-library/react';
import { StyledEngineProvider } from '@mui/material/styles';
import { ThemeProvider } from "@mui/material/styles";
import { theme } from './theme';
import App from './App';

test('renders autoeq', () => {
  render(
    <StyledEngineProvider injectFirst>
      <ThemeProvider theme={theme}>
        <App />
      </ThemeProvider>
    </StyledEngineProvider>
  );
  const searchElement = screen.getByText(/Select your headphones at the top/i);
  expect(searchElement).toBeInTheDocument();
});
