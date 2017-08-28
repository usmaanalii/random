import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import pdir

left = []
y = []

data = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv")

# Setting colors for the plot
N = 53
c = ['hsl(' + str(h) + ',50%' + ',50%)' for h in np.linspace(0, 360, N)]

for i in range(int(N)):
    y.append((2000 + i))
    trace0 = go.Scatter(
        x=data['rank'],
        y=data['pop'] + (i * 1000000),
        mode='markers',
        marker=dict(
            size=14,
            line=dict(width=1),
            color=c[i],
            opacity=0.3
        ),
        name=y[i],
        text=data['state'])

    left.append(trace0)

layout = go.Layout(
    title='Stats of USA States',
    hovermode='closest',
    xaxis=dict(
        title='Pop',
        ticklen=5,
        zeroline=False,
        gridwidth=2,
    ),
    yaxis=dict(
        title='Rank',
        ticklen=5,
        gridwidth=2,
    ),
    width=600,
    height=600,
    margin=go.Margin(
        l=50,
        r=50,
        b=50,
        t=50,
        pad=4
    ),
    showlegend=False
)

fig = go.Figure(data=left, layout=layout)
py.iplot(fig)
