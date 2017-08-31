import pandas as pd
import numpy as np
import statsmodels.api as sm
import math
from sql import cur
from utilities import get_innings_changes

# Data
df = pd.DataFrame(cur.fetchall())

# Add count of delivery number
df['deliv'] = [n + 1 for n in range(len(df))]

# Drop null bounces
df = df.dropna(subset=['bvrz']).copy()

# bvrz values
pace_bvrz_values = df.bvrz[df.pace == 1]
spin_bvrz_values = df.bvrz[df.pace == 0]

# deliv number counts
pace_deliv_values = df.deliv[df.pace == 1]
spin_deliv_values = df.deliv[df.pace == 0]

# local regression method using LOWESS
lowess = sm.nonparametric.lowess

# regression values for both axis based on the lowess algorithm
pace_regression_x = lowess(pace_bvrz_values, pace_deliv_values)[:, 0]
pace_regression_y = lowess(pace_bvrz_values, pace_deliv_values)[:, 1]

spin_regression_x = lowess(spin_bvrz_values, spin_deliv_values)[:, 0]
spin_regression_y = lowess(spin_bvrz_values, spin_deliv_values)[:, 1]

# x axis (delivery number) limits, rounded to the nearest 100
#   - TODO: This could be updated to round based on the number of deliveries,
#           for example, if there were 80 deliveries, round to the nearest 10
#           etc and so on...
delivery_number_min = int(round(df.deliv.min(), -2))
delivery_number_max = int(round(df.deliv.max(), -2))

# y axis (bvrz) limits
bvrz_min = np.percentile(df['bvrz'], 1)
bvrz_max = np.percentile(df['bvrz'], 99)

# list of delivery numbers corrsponding to the change of innings
innings_changovers = get_innings_changes(df)
