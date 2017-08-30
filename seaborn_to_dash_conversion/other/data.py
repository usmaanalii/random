import pandas as pd
import numpy as np
import statsmodels.api as sm
import os

os.chdir('/Applications/XAMPP/xamppfiles/htdocs/xampp/repos/random/seaborn_to_dash_conversion/other')

# Data
df = pd.read_csv('../usmaan_test_data.csv')

# add count of delivery number
df['deliv'] = [n + 1 for n in range(len(df))]

# drop null bounces
df = df.dropna(subset=['bvrz']).copy()

# bvrz values
pace_bvrz_values = df.bvrz[df.pace == 1]
spin_bvrz_values = df.bvrz[df.pace == 0]

# value counts
pace_deliv_values = df.deliv[df.pace == 1]
spin_deliv_values = df.deliv[df.pace == 0]

# local regression using LOWESS
lowess = sm.nonparametric.lowess

pace_regression_x = lowess(pace_bvrz_values, pace_deliv_values)[:, 0]
pace_regression_y = lowess(pace_bvrz_values, pace_deliv_values)[:, 1]

spin_regression_x = lowess(spin_bvrz_values, spin_deliv_values)[:, 0]
spin_regression_y = lowess(spin_bvrz_values, spin_deliv_values)[:, 1]

# y axis (bvrz) range values
bvrz_max = np.percentile(df['bvrz'], 99)
bvrz_min = np.percentile(df['bvrz'], 1)

# Exploration
len(df.inn.unique())


def get_innings_changes(data):
    delivery_numbers = []

    for i in range(2, 1 + len(data.inn.unique())):
        delivery_numbers.append(data[data.inn == i]['deliv'].idxmin())

    return delivery_numbers


def print_inning_lines(numbers=get_innings_changes(df), color='grey', y0=bvrz_min, y1=bvrz_max):
    lines = []
    for number in numbers:
        lines.append(
            {
                'type': 'line',
                'x0': number,
                'y0': y0,
                'x1': number,
                'y1': y1,
                'line': {
                    'width': 1,
                    'color': color
                }
            }
        )

    return lines
