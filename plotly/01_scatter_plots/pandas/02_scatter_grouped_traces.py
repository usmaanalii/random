import plotly.plotly as py
import pandas as pd

df = pd.read_csv(
    'http://www.stat.ubc.ca/~jenny/notOcto/STAT545A/examples/gapminder/data/gapminderDataFiveYear.txt', sep='\t')
df2007 = df[df.year == 2007]
df1952 = df[df.year == 1952]
df.head(2)

fig = {
    'data': [
        {
            'x': df[df.year == year].gdpPercap,
            'y': df[df.year == year].lifeExp,
            'name': year,
            'mode': 'markers'
        } for year in [1952, 1982, 2007]
    ],
    'layout': {
        'xaxis': {
            'title': 'GDP per Capita',
            'type': 'log'
        },
        'yaxis': {
            'title': 'Life Expectancy'
        },
        'width': 600,
        'height': 600
    }
}

py.iplot(fig, filename='pandas-grouped-scatter')
