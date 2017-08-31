import pandas as pd
import numpy as np
import statsmodels.api as sm
from utilities import (
    get_innings_changes
)

import os
os.chdir('/Applications/XAMPP/xamppfiles/htdocs/xampp/repos/random/seaborn_to_dash_conversion/solution')


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
bvrz_min = np.percentile(df['bvrz'], 1)
bvrz_max = np.percentile(df['bvrz'], 99)

# delivery number at inning changeovers
innings_changovers = get_innings_changes(df)

# Exploration
df.head(10)
