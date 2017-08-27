/**
 * JSX
 *  - Strange HTML-ish syntax
 *  - Is a wrapper for React.createElement
 *  - Makes the code look more like rendered HTML
 *  - Needs transpiling with a build tool
 */

<Wrapper>
    <h1 className="heading">Hello World</h1>
</Wrapper>

// Is the same as
React.createElement(Wrapper, null,
  React.createElement('h1', {className: 'heading'}, 'Hello World')
)

// You can pass properties, add children and use JS code via curly braces
var Wrapper = function(props) {
    return (
        <div className="wrapper">{ props.children }</div>
    );
};

