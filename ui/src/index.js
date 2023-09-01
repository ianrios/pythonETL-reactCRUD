import React from 'react';
import ReactDOM from 'react-dom';

import reportWebVitals from './reportWebVitals';

import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';
import './index.css';

import App from './components/app';

import { AppProvider } from './context/app-context';


// const theme = createTheme({

// });

// using file structure borrowed from:
// https://blog.webdevsimplified.com/2022-07/react-folder-structure/

// using kebab-case file naming conventions:
// https://www.verytechnology.com/iot-insights/the-design-behind-kebab-case-ing-our-react-apps

ReactDOM.render(
  <React.StrictMode>
    {/* <ThemeProvider theme={theme}> */}
    <AppProvider>
      <App />
    </AppProvider>
    {/* </ThemeProvider> */}
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
