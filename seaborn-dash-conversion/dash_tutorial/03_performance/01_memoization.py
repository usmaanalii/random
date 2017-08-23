# Performance
#   - Speeding up the callbacks will make the app snappier
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import datetime
import os
from flask_caching import Cache

# * Memoization
#   - Stores the results of a function after its called, and
#     re-uses the result, if the function is called with the same
#     arguments

#   - Dash apps are frequently deployed across multiple threads
#   - Each thread contains it's own memory, without sharing across
#     threads
#   - Use Flask-Caching library, which saves the results in a
#     shared memory database
#   - It also has time-based expirty

app = dash.Dash(__name__)
cache = Cache(app.server, config={
    # try 'filesystem' if you don't want to setup redis
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': os.environ.get('REDIS_URL', '')
})
app.config.supress_callback_exceptions = True

timeout = 20
app.layout = html.Div([
    html.Div(id='flask-cache-memoized-children'),
    dcc.RadioItems(
        id='flask-cache-memoized-dropdown',
        options=[
            {'label': 'Option {}'.format(i), 'value': 'Option {}'.format(i)}
            for i in range(1, 4)
        ],
        value='Option 1'
    ),
    html.Div('Results are cached for {} seconds'.format(timeout))
])


@app.callback(
    Output('flask-cache-memoized-children', 'children'),
    [Input('flask-cache-memoized-dropdown', 'value')])
@cache.memoize(timeout=timeout)  # in seconds
def render(value):
    return 'Selected "{}" at "{}"'.format(
        value, datetime.datetime.now().strftime('%H:%M:%S')
    )


if __name__ == '__main__':
    app.run_server(debug=True)
