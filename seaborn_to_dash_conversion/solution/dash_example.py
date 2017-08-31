import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from data import (
    pace_deliv_values,
    pace_bvrz_values,

    pace_regression_x,
    pace_regression_y,

    spin_deliv_values,
    spin_bvrz_values,

    spin_regression_x,
    spin_regression_y,

    delivery_number_min,
    delivery_number_max,

    bvrz_min,
    bvrz_max,

    innings_changovers
)

from utilities import (
    print_inning_lines
)

app = dash.Dash()

colors = dict(
    pace='#D9437D',
    spin='#367D9F',
    over_line='#888886'
)

# pace scatter plot values
trace1 = go.Scatter(
    x=pace_deliv_values,
    y=pace_bvrz_values,
    mode='markers',
    marker=dict(
        color=colors['pace'],
    ),
    opacity=0.3,
    name='pace'
)

# pace regression line
trace2 = go.Scatter(
    x=pace_regression_x,
    y=pace_regression_y,
    line=dict(
        width=4
    ),
    marker=dict(
        color=colors['pace']
    ),
    hoverinfo='none',
    showlegend=False
)

# spin scatter plot values
trace3 = go.Scatter(
    x=spin_deliv_values,
    y=spin_bvrz_values,
    mode='markers',
    marker=dict(
        color=colors['spin']
    ),
    opacity=0.3,
    name='spin'
)

# spin regression line
trace4 = go.Scatter(
    x=spin_regression_x,
    y=spin_regression_y,
    line=dict(
        width=4
    ),
    marker=dict(
        color=colors['spin']
    ),
    hoverinfo='none',
    showlegend=False
)

# list[dicts]
#   - represents a list of dicts, each dict contains the code to construct a
#     single line
inning_lines = print_inning_lines(innings_changovers, bvrz_min,
                                  bvrz_max, color=colors['over_line'])

app.layout = html.Div(style={}, children=[
    html.H1(
        children='Cricviz Demo App',
        style={
            'textAlign': 'center'
        }
    ),

    html.Div(children='Bounce Velocity Ratio to Match Delivery Number', style={
        'textAlign': 'center'
    }),

    dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [trace1, trace2, trace3, trace4],
            'layout': go.Layout(
                xaxis=dict(
                    title='Match Delivery',
                    zeroline=False,
                    range=[delivery_number_min - 50, delivery_number_max]
                ),
                yaxis=dict(
                    title='Bounce Velocity Ratio',
                    range=[bvrz_min, bvrz_max]
                ),
                shapes=inning_lines
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
