import plotly.plotly as py
import plotly.graph_objs as go
from scipy import stats

df = pd.read_csv('usmaan_test_data.csv')
df.head()

pace_bvrz_vals = df.bvrz[df.pace == 0].dropna(how='any')
spin_bvrz_vals = df.bvrz[df.pace == 1].dropna(how='any')

pace_speed_vals = bvrz_pace_vals.index
spin_speed_vals = bvrz_spin_vals.index

pace_slope, pace_intercept, pace_r_value, pace_p_value, pace_std_err = stats.linregress(pace_speed_vals, pace_bvrz_vals)

spin_slope, spin_intercept, spin_r_value, spin_p_value, spin_std_err = stats.linregress(spin_speed_vals, spin_bvrz_vals)

delivery_count = [n + 1 for n in range(len(df))]

# Create a trace
trace1 = go.Scatter(
    x=pace_speed_vals,
    y=pace_bvrz_vals,
    mode='markers',
    name='pace'
)

trace2 = go.Scatter(
    x=spin_speed_vals,
    y=spin_bvrz_vals,
    mode='markers',
    name='spin'
)

trace3 = go.Scatter(
    x=pace_speed_vals,
    y=pace_intercept + pace_slope * pace_speed_vals,
    line=go.Line(width=5)
)

trace4 = go.Scatter(
    x=spin_speed_vals,
    y=spin_intercept + spin_slope * spin_speed_vals,
    line=go.Line(width=5)
)

data = [trace1, trace2, trace3, trace4]

layout = go.Layout(
    width=600,
    height=600,
    xaxis=dict(
        title="Match Delivery",
        range=[-100, 1400]
    ),
    yaxis=dict(
        title="Bounce Velocity Ratio",
        range=[0.38, 0.75]
    )
)

fig = dict(data=data, layout=layout)

py.iplot(fig, filename='pace-velocity')
