import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

# Create random data with numpy
N = 500
random_x = np.linspace(0, 1, N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x=random_x,
    y=random_y
)

data = [trace]

layout = go.Layout(
    width=600,
    height=600
)

fig = go.Figure(data=data, layout=layout)

py.iplot(fig, filname='basic-line')