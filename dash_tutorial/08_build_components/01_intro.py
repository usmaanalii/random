# Writing your own components
#   - It is built on top of React.js

# From React.js to Python
#   - Dash provides a framework that converts React components into Python
#     classes, compatible with the Dash ecosystem

# How this works
#   - Components are serailized as JSON, components properties must be
#     serailizable
#   - Dash extracts information from React doctrings, about name, properties
#     and description of components via React Docgen, exported as JSON
#   - Dash reads the JSON file and creates Python classes that subclass
#     a core Dash component.
#   - Dash app crawls through the apps layour property, checking which
#     component packages are included, and then extracts the components's
#     necessary JS/CSS bundles, which render the components
#   - Dash's layour is serailized as JSON, and served to Dash's front-end