import dash
import dash_html_components as html
import datetime

app = dash.Dash(__name__)

# Doesn't work
# app.layout = html.H1('The time is: ' + str(datetime.datetime.now()))


# Works
def serve_layout():
    return html.H1('The time is: ' + str(datetime.datetime.now()))


app.layout = serve_layout

if __name__ == '__main__':
    app.run_server()
