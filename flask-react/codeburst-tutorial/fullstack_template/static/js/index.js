import React from "react";
import ReactDOM from "react-dom";

class Example extends React.Component {
  constructor(props){
  	super(props);
  	this.state = {
      color: this.props.color,
      number: this.props.number,
      hello: this.props.hello
    };

    this.changeColor = this.changeColor.bind(this);
    this.increment = this.increment.bind(this);
    this.newGreeting = this.newGreeting.bind(this);
  }

  increment() {
    const { color } = this.state;
    console.log('color', color);
    this.setState(({number}) => ({
      number: number + 1
    }));
  }

  changeColor(event) {
    const newColor = event.target.value || 'black';
    this.setState({
      color: newColor
    })
  }

  newGreeting() {
    fetch(`${window.location.origin}/hello`)
      .then(response => response.json())
      .then(data => {
        const hello = data.hello;
        this.setState({ hello })
      });
  }

  componentDidMount() {
    this.newGreeting()
  }

  render() {
    return (
      <div
        style={
          { 'border': `2px solid ${this.state.color}` }
        }
      >
        <h1
          ref={node => this.h1Node = node}
          >Example H1
        </h1>
        <h2
          style={{color: this.state.color}}
        >
          {this.state.color}
        </h2>
        <h3
          onClick={this.increment}
          >{this.state.number}
        </h3>
        <h4
          onClick={this.newGreeting}
          >{this.state.hello}
        </h4>

        <input
          style={
            {'border': ` 1px solid ${this.state.color}`},
            {'fontSize': `1.${this.state.number}em`}
          }
          onKeyUp={event => this.changeColor(event)}
        />
      </div>
    )
  }
}

ReactDOM.render(
  <Example
    color="pink"
    number={1}
    hello="hello"
  />,
  document.querySelector('#root')
);
