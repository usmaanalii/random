# import os; os.chdir('/Applications/XAMPP/xamppfiles/htdocs/xampp/repos/random/seaborn_to_dash_conversion/solution')
import pandas as pd
import numpy as np
import statsmodels.api as sm
import math
import datetime
from sql import matches, match_data
from utilities import changeovers

#############
# Bounce data
#############

# Data
bounce_data_df = pd.DataFrame(match_data)

# Add count of delivery number
bounce_data_df['deliv'] = [n + 1 for n in range(len(bounce_data_df))]

# Change the format of the date column
#   TODO: Is this the most optimal solution?
bounce_data_df.date = bounce_data_df.date.apply(lambda x: x.date().strftime('%d-%m-%y'))

# Drop null bounces
bounce_data_df = bounce_data_df.dropna(subset=['bvrz']).copy()

# bvrz values
pace_bvrz_values = bounce_data_df.bvrz[bounce_data_df.pace == 1]
spin_bvrz_values = bounce_data_df.bvrz[bounce_data_df.pace == 0]

# deliv number counts
pace_deliv_values = bounce_data_df.deliv[bounce_data_df.pace == 1]
spin_deliv_values = bounce_data_df.deliv[bounce_data_df.pace == 0]

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
delivery_number_min = int(round(bounce_data_df.deliv.min(), -2))
delivery_number_max = int(round(bounce_data_df.deliv.max(), -2))

# y axis (bvrz) limits
bvrz_min = np.percentile(bounce_data_df['bvrz'], 1)
bvrz_max = np.percentile(bounce_data_df['bvrz'], 99)

# list of delivery numbers corrsponding to the change of innings
innings_changovers = changeovers(bounce_data_df.inn)

# list of delivery numbers corrsponding to the change of day
day_changeovers = changeovers(bounce_data_df.date)

#############
# Match data
#############

# Data
matches_df = pd.DataFrame(matches)
match_ids = matches_df.id
