import plotly.plotly as py
import cufflinks as cf
import pandas as pd

cf.set_config_file(offline=False, world_readable=True, theme='ggplot')

df = cf.datagen.lines(3)
df.head()

colors = ['red', 'blue', 'black']
dashes = ['solid', 'dash', 'dashdor']
widths = [2, 4, 6]

layout = dict(
    width=600,
    height=600
)

plot_url = df.iplot(kind='scatter', mode='lines', colors=colors, dash=dashes, filename='cufflinks-line-style-and-color')