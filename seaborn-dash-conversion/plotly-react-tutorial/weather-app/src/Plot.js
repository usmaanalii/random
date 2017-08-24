/* global Plotly */
import React from 'react';

class Plot extends React.Component {
  
  drawPlot = () => {
    Plotly.newPlot('plot', [{
      x: this.props.xData,
      y: this.props.yData,
      type: this.props.type
    }], {
      margin: {
        t: 0, r: 0, l: 30
      },
      xaxis: {
        gridColor: 'transparent'
      }
    }, {
      displayModeBar: false
    });
    
    document.getElementById('plot').on('plotly_click', this.props.onPlotClick);
  }
  
  componentDidMount() {
    this.drawPlot();
  }
  
  componentDidUpdate() {
    this.drawPlot();
  }

    render() {
        return (
            <div id="plot"></div>
        );
    }
}

export default Plot;

/**
 * - the div above is the DOM element that will be referenced in our
 *   Plotly.newPlot call
 * - calling ^ in render() would mean it running multiple times a second
 *   so use componentDidMount()
 * - This is called once, only when the componet is rendered 
 */