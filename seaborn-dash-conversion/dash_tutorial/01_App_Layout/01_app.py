import dash
import dash_core_components as doc
import dash_html_components as html

# Dash App Layout

# * Generating HTML with Dash
# - Dash apps are composed of two parts
#       1. Layout -> what it looks like
#       2. Interactivity
# - Components are maintained in dash_core_components and
#   dash_html_components, but they can be build with React.js

app = dash.Dash()

app.css.append_css(
    {"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    doc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5],
                    'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

# NOTE:
#       - layout is composed of a tree of "components" like html.Div
#       - dash_html_components provides html.H! -> <h1>...</h1> etc..
#       - can generate components with html/css/js with interactivity
#       - applications are described via keyword attributes
#       - peep the children property html.H1(children=...) == html.H1(...)

# * More about HTML
# - dash_html_components -> component class for every HTML tag
#                           keyword argument for all HTML arguments

# - html.H1('Hello Dash', style={'textAlign': 'center', 'color': '#7FDFF'})
#   becomes
#   <h1 style="text-align: center; color: #7FDFF">Hello Dash</h1>

if __name__ == '__main__':
    app.run_server(debug=True)
