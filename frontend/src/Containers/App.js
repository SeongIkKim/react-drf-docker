import React from "react";
import Article from "../Components/Article";
import { Provider as ReduxProvider } from "react-redux";
import configureStore from "../Redux/store";

const reduxStore = configureStore(window.REDUX_INITIAL_DATA);

function App() {
  return (
    <ReduxProvider store={reduxStore}>
      <div className="App">
        <Article />
      </div>
    </ReduxProvider>
  );
}

export default App;