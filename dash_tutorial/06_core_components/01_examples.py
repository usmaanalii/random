import dash_core_components as dcc
import plotly.graph_objs as go
from datetime import datetime as dt

# Dropdown
dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL'
)

# Multi Dropdown
dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    multi=True,
    value='MTL'
)

# Date Picker (Single)
dcc.DatePickerSingle(
    id='date-picker-single',
    date=dt(1997, 5, 10)
)

# Date Picker (Range)
dcc.DatePickerRange(
    id='date-picker-range',
    start_date=dt(1997, 5, 10),
    end_date_placeholder_text='Select a date'
)

# Another Date Picker (Single)
dcc.DatePickerSingle(
    id='date-picker-single',
    initial_visible_month=dt(1997, 5, 5),
    min_date_allowed=dt(1997, 4, 29),
    max_date_allowed=dt(1997, 6, 3)
    show_outside_days=True,
    view_portal=True,
    number_of_months_shown=1,
    placeholder='Try it out!'
)

# Another Date Picker (Range)
dcc.DatePickerRange(
    id='date-picker-range',
    start_date=dt(1997, 5, 10),
    end_date_placeholder_text="Clear the date!",
    first_day_of_week=3,
    minimum_nights=2,
    min_date_allowed=dt(1997, 4, 29),
    max_date_allowed=dt(1997, 6, 3),
    show_outside_days=True,
    calendar_orientation='vertical',
    number_of_months_shown=2,
    clearable=True,
    day_size=45,
    stay_open_on_select=True,
    reopen_calendar_on_clear=True,
    month_format='MM YY',
    display_format='MMMM D, Y'
)

# Slider
dcc.Slider(
    min=0,
    max=9,
    step=0.5,
    value=5,
)

# Slider #2
dcc.Slider(
    min=0,
    max=9,
    marks={i: 'Label {}'.format(i) for i in range(10)},
    value=5,
)

# RangeSlider (allows you to slide beginning and end)
dcc.RangeSlider(
    count=1,
    min=-5,
    max=10,
    step=0.5,
    value=[-3, 7]
)

# Label provided
dcc.RangeSlider(
    marks={i: 'Label {}'.format(i) for i in range(10)},
    min=-5,
    max=6,
    value=[-3, 4]
)

# Input
dcc.Input(
    placeholder='Enter a value...',
    type='text',
    value=''
)

# Checkboxes
dcc.Checklist(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    values=['MTL', 'SF']
)

# Checboxes (Inline)
dcc.Checklist(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    values=['MTL', 'SF'],
    labelStyle={'display': 'inline-block'}
)

# Radio Items
dcc.RadioItems(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL'
)

# Radio Items (Inline)
dcc.RadioItems(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL',
    labelStyle={'display': 'inline-block'}
)

# Markdown
dcc.Markdown('''
#### Dash and Markdown

Dash supports [Markdown](http://commonmark.org/help).

Markdown is a simple way to write and format text.
It includes a syntax for things like **bold text** and *italics*,
[links](http://commonmark.org/help), inline `code` snippets, lists,
quotes, and more.
''')

# Graphs
#   - Shares the same syntax as plotly.py
dcc.Graph(
    figure=go.Figure(
        data=[
            go.Scatter(x=[1, 2, 3], y=[3, 2, 4] mode='lines'),
            go.Scatter(x=[1, 2, 3], y=[4, 1, 5], mode='lines')
        ],
        layout=go.Layout(
            title='Quarterly Results',
            showlegend=False,
            margin=go.Margin(l=20, r=0, t=40, b=20)
        )
    ),
    style={'height': 300},
    id='my-graph'
)
