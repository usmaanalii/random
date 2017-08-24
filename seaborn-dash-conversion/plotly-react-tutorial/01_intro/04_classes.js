/**
 * Classes
 *  - React has the virtual DOM, to minimize rerendering upon state change
 *
 * What is application state, and how do we manage it in React?
 *  - It ranges from 'checkbox being checked' to 'data was fetched'
 */

/**
 * Example: Counter
 *  - Counts how often a button is clicked
 *  - Use class notation to create 'stateful' components
 *  - Create a new class that extends React.Component (used as a base to
 *    build upon)
 *  - Assign the class to a render method, returning ReactElements
 */

class Counter extends React.Component {

    render() {
        return (
            <p>This is the Counter component</p>
        );
    }
}

// Render this, like other components with ReactDOM.render
ReactDOM.render(<Counter/>
document.getElementById('container'))

// Separate *Button* component, taking the prop *text* (functional - no state)
var Button = function(props) {
    return (
        <button>{props.text}</button>
    )
}

// Render the *Button* into the *Counter* with the text "Click me!"
class Counter extends React.Component {
    render() {
        return (
            <div>
                <p>This is the Counter component!</p>
                <Button text="Click me!"/>
            </div>
        );
    }
}

// Increase the number every time a user clicks on out *Button*, via onClick
class Counter extends React.Component {
    render() {
        return (
            <div>
                <p>This is the Counter component! The button was clicked { this.state.clicks } times</p>
                <Button text="Click me!" onClick={function() {
                    console.log('click!');
                }}/>
            </div>
        );
    }
}

/**
 * Differentiate between react components and real DOM nodes
 *  - Event handlers like onClick, onMouseOver.. only work on real DOM nodes
 *  - Need to attach the onClick handler to the native DOM *button* node inside
 *    the *Button* component
 */
var Button = function(props) {
    return (
        <button onClick={props.onClick}>{props.text}</button>
    );
}

/**
 * Add state to our *Counter* component
 *  - state is a plain object in react, that can have 0 or more props
 *  - Counter's state will have a clicks property with an initial value of 0
 *  - You need to set the iniital state, via the class constructor method
 */
class Counter extends React.Component {

    constructor() {
        super();
        this.state = {
            clicks: 0
        };
    }

    render() {
        //  ...
    }
}

// Use *this.state* to access the current state within our components

// Render the current number of clicks as text
class Counter extends React.Component {

    constructor() {
        super();
        this.state = {
            clicks: 0
        };
    }

    render() {
        return (
            <div>
                <p>This is the Counter component! The button was clicked { this.state.clicks } times.</p>
                <Button text="Click me!" onClick={function() {
                    console.log('click!');
                }}/>
            </div>
        );
    }
}

/**
 * Use the *this.setState* helper function, to change the state of a component
 *  - Need to *bind* the context of increment to the class in the constructor,
 *    since *this* is undefined in increment() due to ES6 classes functionality
 * 
 */
class Counter extends React.Component {

    constructor() {
        super();
        this.state = {
            clicks: 0
        };
        this.increment = this.increment.bind(this);
    }
    
    increment() {
        this.this.setState({
            clicks: this.state.clicks + 1
        });
    };

    render() {
        return (
            <div>
                <p>This is the Counter component! The button was clicked { this.state.clicks } times.</p>
                <Button text="Click me!" onClick={this.increment}/>
            </div>
        );
    }
}
