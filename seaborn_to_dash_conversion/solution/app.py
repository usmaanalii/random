import pymysql

import pandas as pd
import numpy as np
import statsmodels.api as sm
import math
import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utilities import (
    print_inning_lines
)

#####
# Sql
#####

# Database credentials
host = 'db2.cricviz.com'
port = 3307
user = 'usmaan'
passwd = 'w6oovzdjFY'
db_name = 'cvdb'

# Database connection
db = pymysql.connect(
    host=host,
    user=user,
    passwd=passwd,
    db=db_name,
    port=port
)


def get_matches(limit):
    cur = db.cursor(pymysql.cursors.DictCursor)

    cur.execute("""
        SELECT m.name, m.id
        FROM obj_match m
        INNER JOIN bbb_ball b ON b.match_id = m.id
        INNER JOIN bbb_tracking bt ON bt.join_key=b.join_key
        WHERE m.international_class_id <= 2
        GROUP BY m.id
        ORDER BY m.start_date desc
        limit %s
        """, limit)
    data = cur.fetchall()
    cur.close()

    return data


matches = get_matches(10)


# Bounce data from Lord's test
def get_bounce_data(match_id):
    cur = db.cursor(pymysql.cursors.DictCursor)

    cur.execute(
        """
        SELECT
        h.innings_number AS inn,
        h.overs_unique,
        h.created AS date,
        IF (b.bowling_type = 'pace', 1, 0) AS pace,
        h.release_speed_kph AS speed,
        -h.bounce_velocity_ratio_z AS bvrz
        FROM bbb_tracking h
        JOIN bbb_ball b ON b.join_key = h.join_key
        WHERE h.match_id = %s
        """, match_id)

    data = cur.fetchall()
    cur.close()

    return data


###########
# Utilities
###########
def changeovers(items):
    """
    Used to retrieve a list of integers each of which represents the
    delivery number at which the innings/days change.

    @param data: dataframe representing the match data
    @return: list of integers
    """
    indexes = []
    previous = items[0]
    for index, x in enumerate(items):
        if x != previous:
            indexes.append(index)
            previous = x
    return indexes


def print_inning_lines(delivery_numbers, y0, y1, color='grey'):
    """
    Generates vertical plotly lines that can be added to graphs. This is done
    by setting it equal to the *shapes* parameter of
    *dash_core_components.Graph*.

    @param delivery_numbers: (list), of integers, each of which represent the
                             point on the x axis where the vertical line
                             should be placed
    @param y0: (integer), the lines starting point on the y axis
    @param y1: (integer), the lines ending point on the y axis
    @param color: (string), the color of the line
    @return: (list of dicts), each dict represents the code needed to
             generate a single line on the graph
    """

    lines = []
    for number in delivery_numbers:
        lines.append(
            {
                'type': 'line',
                'x0': number,
                'y0': y0,
                'x1': number,
                'y1': y1,
                'line': {
                    'width': 1,
                    'color': color
                }
            }
        )

    return lines


######
# Dash
######
app = dash.Dash()

colors = dict(
    pace='#D9437D',
    spin='#367D9F',
    over_line='#888886'
)


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

    html.Div([
        dcc.Dropdown(
            id='match-ids',
            options=[{'label': x['name'], 'value': x['id']} for x in matches],
            value='193945'
        )
    ], style={'width': '48%',
              'display': 'inline-block',
              'padding-top': '5%'}),

    dcc.RadioItems(
        id='line-option',
        options=[
            {'label': 'Innings', 'value': 'innings'},
            {'label': 'Days', 'value': 'days'}
        ],
        value='innings',
        labelStyle={'display': 'inline-block'}
    ),

    dcc.Graph(id='example-graph')
])


@app.callback(
    dash.dependencies.Output('example-graph', 'figure'),
    [dash.dependencies.Input('match-ids', 'value'),
     dash.dependencies.Input('line-option', 'value')])
def update_graph(match_id, line_option):

    match_data = get_bounce_data(int(match_id))

    ###################
    # Data Manipulation
    ###################

    # Bounce Data
    bounce_data_df = pd.DataFrame(match_data)

    # Add count of delivery number
    bounce_data_df['deliv'] = [n + 1 for n in range(len(bounce_data_df))]

    # Change the format of the date column
    #   TODO: Is this the most optimal solution?
    bounce_data_df.date = bounce_data_df.date.apply(
        lambda x: x.date().strftime('%d-%m-%y'))

    # Drop null bounces
    bounce_data_df = bounce_data_df.dropna(subset=['bvrz']).copy()

    # bvrz values
    pace_bvrz_values = bounce_data_df.bvrz[bounce_data_df.pace == 1]
    spin_bvrz_values = bounce_data_df.bvrz[bounce_data_df.pace == 0]

    # deliv number counts
    pace_deliv_values = bounce_data_df.deliv[bounce_data_df.pace == 1]
    spin_deliv_values = bounce_data_df.deliv[bounce_data_df.pace == 0]

    # local regression method using LOWESS
    lowess = sm.nonparametric.lowess

    # regression values for both axis based on the lowess algorithm
    pace_regression_x = lowess(pace_bvrz_values, pace_deliv_values)[:, 0]
    pace_regression_y = lowess(pace_bvrz_values, pace_deliv_values)[:, 1]

    spin_regression_x = lowess(spin_bvrz_values, spin_deliv_values)[:, 0]
    spin_regression_y = lowess(spin_bvrz_values, spin_deliv_values)[:, 1]

    # x axis (delivery number) limits, rounded to the nearest 100
    #   - TODO: This could be updated to round based on the number of
    #           deliveries, for example, if there were 80 deliveries,
    #           round to the nearest
    #           10 etc and so on...
    delivery_number_min = int(round(bounce_data_df.deliv.min(), -2))
    delivery_number_max = int(round(bounce_data_df.deliv.max(), -2))

    # y axis (bvrz) limits
    bvrz_min = np.percentile(bounce_data_df['bvrz'], 1)
    bvrz_max = np.percentile(bounce_data_df['bvrz'], 99)

    # list of delivery numbers corrsponding to the change of innings
    innings_changovers = changeovers(bounce_data_df.inn)

    # list of delivery numbers corrsponding to the change of day
    day_changeovers = changeovers(bounce_data_df.date)

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
    #   - represents a list of dicts, each dict contains the code to construct
    #     a single line
    inning_lines = print_inning_lines(innings_changovers, bvrz_min,
                                      bvrz_max, colors['over_line'])

    day_lines = print_inning_lines(day_changeovers, bvrz_min,
                                   bvrz_max, colors['over_line'])

    # Takes the radio button value
    if line_option == 'innings':
        lines = inning_lines
    else:
        lines = day_lines

    return {
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
            margin=dict(
                t=20
            ),
            shapes=lines
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)
