import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
import numpy as np

N = 500
x = np.linspace(0, 1, N)
y = np.random.randn(N)

df = pd.DataFrame({'x': x, 'y': y})
df.head()

x2 = np.linspace(0, 1, N)
y2 = np.random.randn(N) + 3

df2 = pd.DataFrame({'x': x2, 'y': y2})
df2.head()

data = [
    go.Scatter(
        x=df.x,
        y=df.y,
        name='random around 0'
    ),

    go.Scatter(
        x=df2.x,
        y=df2.y,
        name='random around 3'
    )
]

layout = go.Layout(
    title='scatter plot with pandas',
    yaxis=dict(title='random distribution'),
    xaxis=dict(title='linspace'),
    width=600,
    height=600
)

fig = go.Figure(data=data, layout=layout)

py.iplot(fig, filename='basic-line-plot')
