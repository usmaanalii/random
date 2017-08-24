import React, {Component} from 'react';
import './App.css';

class App extends Component {
  state = {
    location: ''
  };

  fetchData = (event) => {
    event.preventDefault();
    console.log('fetch data for', this.state.location);
  };

  changeLocation = (event) => {
    this.setState({
      location: event.target.value
    });
  };

  render() {
    return (
      <div>
        <h1>Weather</h1>
        <form onSubmit={this.fetchData}>
          <label>I want to know the weather for
            <input
              placeholder={"City, Country"}
              type="text"
              value={this.state.location}
              onChange={this.changeLocation}
            />
          </label>
        </form>
      </div>
    );
  }
}

export default App;

/**
 * - You want to store the value of the text input in our local component
 *   state, to be able to grab it from the fetchData() method
 * - This makes our input a "controlled input"
 *
 * - Store the currently entered location in *this.state.location*
 * - Add a utility method called *changeLocation*, that is called onChange
 *   of the text input, setting the state to the current state
 *
 * - When saving anything to local state, the variable needs to be predefined
 *   hence the state = { location: '' } code
 */