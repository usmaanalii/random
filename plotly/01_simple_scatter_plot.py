import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import pdir

# create random data with numpy
N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x=random_x,
    y=random_y,
    mode='markers'
)

# Plot and embed in ipython notebook
py.iplot(data, filename='basic-scatter')

# PLot with url
plot_url = py.plot(data, filename='basic-line')
