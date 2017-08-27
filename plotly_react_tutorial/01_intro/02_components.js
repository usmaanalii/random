/**
 * Components
 *  - Functions that return a ReactElement
 */

// This can be used like any DOM Node, via createElement() calls
var Wrapper = function(props) {
    return React.createElement('div', { className: 'wrapper' });
}

React.createElement(Wrapper);

// Component functions get passed props
var Wrapper = function(props) {
    // Render the children we get passed from the createElement(Wrapper) call
    return React.createElement('div', { className: 'wrapper' }, props.children);
}

React.createElement(Wrapper, {}, 'Hello World');

// Render heading inside Wrapper component
React.createElement(Wrapper, null,
    React.createElement('h1', null, 'Hello World')
)
// -> <div class="wrapper"><h1>Hello World</h1></div>