import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
import numpy as np

N = 500
x = np.linspace(0, 1, N)
y = np.random.randn(N)

df = pd.DataFrame({'x': x, 'y': y})
df.head()

data = [
    go.Scatter(
        x=df.x,
        y=df.y
    )
]

fig = dict(data=data, layout=dict(width=600, height=600))

py.iplot(fig, filename='basic-line-plot')