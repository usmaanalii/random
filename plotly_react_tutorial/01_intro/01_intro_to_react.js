/**
 * Introduction to React.js
 *
 * Why React.js?
 *  - TBAT build large apps with ever changing data
 *  - Express how apps should look at any given time
 *  - Use encapsulated, reusable and composable components
 */

/**
 * Getting Started
 *  - Two libraries
 *      o React - create elements
 *      o ReactDOM - renders elements
 */

// Generate <h1>Hello World</h1> via ReactDOM.render() with React,createElement()
ReactDOM.render(
    React.createElement('h1', {className: 'heading'}, 'Hello World'),
    document.getElementById('container')
);

/**
 * ReactDOm.render()
 *  - Takes 2 arguments
 *      o ReactElement to render
 *      o DOM node to render into (entry point)
 *  - It empties the DOM node we use as an entry point, so use
 *    React.createElement() to render multiple ReactElements
 */
 ReactDOM.render(
     React.createElement('h1', {className: 'heading'}, 'Hello World'),
     document.getElementById('container')
 );

/**
 * React.createElement()
 *  - Arguments
 *      o Node (ReactElement) to create
 *      o Properties, like type
 *      o children, as the third argument e.g "text"
 *  - Uses className not class since this is reserved in React
 */
React.createElement('input'); // -> <input></input>
React.createElement('input', { type: 'radio' }); // -> <input type="radio"></input>
React.createElement('input', { className: 'heading', type: 'radio' }); // -> <input></input>

// Child argument
React.createElement('h1', null, 'Hello World'); // -> <h1>Hello World</h1>

// Add a div around h1 via React.createElement
React.createElement('div', { className: 'wrapper' },
    React.createElement('h1', null, 'Hello World')
)

// Produces

/* <div class="wrapper">
    <h1>Hello World</h1>
</div> */

