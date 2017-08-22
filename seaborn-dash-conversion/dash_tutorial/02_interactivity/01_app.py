import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

# Interactivity
#   - How to make the graphs interactive

# * Dash App Layout

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='my-id', value='initial value', type="text"),
    html.Div(id='my-div')
])


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)

# NOTE:
#   - Inputs and outputs declared thorugh app.callback
#   - ^^ are the properties of properties of a component
#       - input -> value property of component with id = my-id
#       - output -> children property of component with id = my-id
#   - When the input changes, the function wrapped by callback is called
#     and provided with the new value of the input property as an argument
#   - No children element passed to the property of my-div, since it takes
#     the value provided by input


if __name__ == '__main__':
    app.run_server()