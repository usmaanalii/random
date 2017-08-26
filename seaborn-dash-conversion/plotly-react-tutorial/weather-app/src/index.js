import React from 'react';

import ReactDOM from 'react-dom';

import './index.css';

import { createStore, applyMiddleware } from 'redux';

import thunkMiddleware from 'redux-thunk';

import { Provider } from 'react-redux';

import App from './App';

import registerServiceWorker from './registerServiceWorker';

import mainReducer from './reducers';

var store = createStore(
  mainReducer,
  applyMiddleware(thunkMiddleware)
);

ReactDOM.render(
    <Provider store={store}>
        <App />
    </Provider>,
  document.getElementById('root')
);
    
registerServiceWorker();