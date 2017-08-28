import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

# Implement WebGL with Scattergl() for
#   - better speed
#   - interactivity and
#   - ability to plot more data

N = 100000

trace = go.Scattergl(
    x=np.random.randn(N),
    y=np.random.randn(N),
    mode='markers',
    marker=dict(
        color='#FFBAD2',
        line=dict(width=1),
    )
)

data = [trace]

layout = go.Layout(
    width=600,
    height=600
)

fig = go.Figure(data=data, layout=layout)

py.iplot(fig, filename='compare_webgl')
