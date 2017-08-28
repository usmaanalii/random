import pandas as pd

df = pd.read_csv(
    'http://www.stat.ubc.ca/~jenny/notOcto/STAT545A/examples/gapminder/data/gapminderDataFiveYear.txt', sep='\t')

df2007 = df[df.year == 2007]
df1952 = df[df.year == 1952]

df.head(2)

fig = {
    'data': [
        {
            'x': df2007.gdpPercap,
            'y': df2007.lifeExp,
            'text': df2007.country,
            'mode': 'markers',
            'name': '2007'
        },
        {
            'x': df1952.gdpPercap,
            'y': df1952.lifeExp,
            'text': df1952.country,
            'mode': 'markers',
            'name': '1952'
        }
    ],
    'layout': {
        'xaxis': {
            'title': 'GDP Per Capita',
            'type': 'log'
        },
        'yaxis': {
            'title': 'Life Expectancy'
        },
        'width': 600,
        'height': 600
    }
}

py.iplot(fig, filename='pandas-multiple-scatter')

