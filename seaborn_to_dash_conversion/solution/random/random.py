from sql import cur
import pandas as pd
import timeit

data = cur.fetchall()

df = pd.DataFrame(data)

%timeit df.date.apply(lambda x: x.date().strftime('%d-%m-%y'))
%timeit map(lambda x: x.date().strftime('%d-%m-%y'), df.date)
%timeit df['date'].map(lambda x: x.date().strftime('%d-%m-%y'))

df.date.apply(lambda x: x.date().strftime('%d-%m-%y'))
