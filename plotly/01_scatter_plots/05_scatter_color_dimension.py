import plotly.graph_objs as go
import plotly.plotly as py
import numpy as np

trace1 = go.Scatter(
    y=np.random.randn(500),
    mode='markers',
    marker=dict(
        size='16',
        color=np.random.randn(500),  # set color variable equan to a variable
        colorscale='Viridis',
        showscale=True
    )
)

data = [trace1]

layout = go.Layout(
    width=600,
    height=600
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='scatter-plot-with-colorscale')

y