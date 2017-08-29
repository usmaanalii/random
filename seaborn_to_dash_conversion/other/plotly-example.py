import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
from scipy import stats

df = pd.read_csv('usmaan_test_data.csv')

df.head()

# add count of delivery number
df['deliv'] = [n + 1 for n in range(len(df))]

# drop null bounces
df = df.dropna(subset=['bvrz']).copy()
df.head()

# bvrz values
pace_bvrz_values = df.bvrz[df.pace == 1]
pace_bvrz_values.head(2)
spin_bvrz_values = df.bvrz[df.pace == 0]
spin_bvrz_values.head(2)

# value counts
pace_deliv_values = df.deliv[df.pace == 1]
spin_deliv_values = df.deliv[df.pace == 0]

pace_slope, pace_intercept, pace_r_value, pace_p_value, pace_std_err = stats.linregress(
    pace_deliv_values, pace_bvrz_values)

spin_slope, spin_intercept, spin_r_value, spin_p_value, spin_std_err = stats.linregress(
    spin_deliv_values, spin_bvrz_values)

# Create a trace
trace1 = go.Scatter(
    x=pace_deliv_values,
    y=pace_bvrz_values,
    mode='markers',
    name='pace'
)

trace2 = go.Scatter(
    x=spin_deliv_values,
    y=spin_bvrz_values,
    mode='markers',
    name='spin'
)

trace3 = go.Scatter(
    x=pace_deliv_values,
    y=pace_intercept + pace_slope * pace_deliv_values,
    line=go.Line(width=5),
    name=None
)

trace4 = go.Scatter(
    x=spin_deliv_values,
    y=spin_intercept + spin_slope * spin_deliv_values
)

data = [trace1, trace2, trace3, trace4]

layout = go.Layout(
    width=600,
    height=600,
    xaxis=dict(
        title="Match Delivery",
        range=[-100, 1400],
        showline=False
    ),
    yaxis=dict(
        title="Bounce Velocity Ratio",
        range=[0.38, 0.75]
    )
)

fig = dict(data=data, layout=layout)

py.iplot(fig, filename='pace-velocity')
