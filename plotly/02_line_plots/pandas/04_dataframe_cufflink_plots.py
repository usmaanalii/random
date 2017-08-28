import plotly.plotly as py
import cufflinks as cf
import pandas as pd

cf.set_config_file(offline=False, world_readable=True, theme='ggplot')

df = cf.datagen.lines()
df.head()

layout = dict(
    width=600,
    height=600
)

df.iplot(kind='scatter', layout=layout, filename='cufflinks-cf-simple-line')