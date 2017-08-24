import React from 'react';
import './App.css';
import xhr from 'xhr';

import Plot from './Plot.js'

class App extends React.Component {
  state = {
    location: '',
    data: {},
    dates: [],
    temps: [],
    selected: {
      date: '',
      temp: null
    }
  };

  fetchData = (event) => {
    event.preventDefault();
    
    var location = encodeURIComponent(this.state.location);
    
    var urlPrefix = 'http://api.openweathermap.org/data/2.5/forecast?q=';
    var urlSuffix = '&APPID=50df8e915277555b2d85b37990ee5ba9&units=metric';
    var url = urlPrefix + location + urlSuffix;
    
    var self = this; 
    // because this will change as it enters the function below
    
    xhr({
      url: url
    }, function (error, data) {
      var body = JSON.parse(data.body);
      var list = body.list;
      var dates = [];
      var temps = [];
      for (var i = 0; i < list.length; i++) {
        dates.push(list[i].dt_txt);
        temps.push(list[i].main.temp);
      }
      self.setState({
        data: body,
        dates: dates,
        temps: temps,
        selected: {
          date: '',
          temp: null
        }
      });
    });
  };

  changeLocation = (event) => {
    this.setState({
      location: event.target.value
    });
  };
  
  onPlotClick = (data) => {
    if (data.points) {
      this.setState({
        selected: {
          date: data.points[0].x,
          temp: data.points[0].y
        }
      });
    }
  };

  render() {
    var currentTemp = 'not loaded yet';
    if (this.state.data.list) {
      currentTemp = this.state.data.list[0].main.temp;
    }
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
        {/*
          Render the current temperature and the forecast if we have data
          otherwise null  
          */}
          {(this.state.data.list) ? (
            <div className="wrapper">
              {/* Render the current temperature if no specified date */}
              <p className="temp-wrapper">
                <span className="temp">
                  { this.state.selected.temp ? this.state.selected.temp : currentTemp }
                </span>
                <span className="temp-symbol">°C</span>
                <span className="temp-date">
                  { this.state.selected.temp ? this.state.selected.date : '' }
                </span>
              </p>
              <h2>Forecast</h2>
              <Plot
                xData={this.state.dates}
                yData={this.state.temps}
                onPlotClick={this.onPlotClick}
                type="scatter"
              />
            </div>
          ) : null}
    
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