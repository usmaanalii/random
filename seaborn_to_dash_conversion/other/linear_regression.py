# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

%matplotlib inline

df = pd.read_csv('usmaan_test_data.csv')

df.head()

# add count of delivery number
df['deliv'] = [n + 1 for n in range(len(df))]

# drop null bounces
df = df.dropna(subset=['bvrz']).copy()
df.head()

# bvrz values
pace_bvrz_values = df.bvrz[df.pace == 1]
pace_bvrz_values.head(2)
spin_bvrz_values = df.bvrz[df.pace == 0]
spin_bvrz_values.head(2)

# value counts
pace_deliv_values = df.deliv[df.pace == 1]
spin_deliv_values = df.deliv[df.pace == 0]

pace_slope, pace_intercept, pace_r_value, pace_p_value, pace_std_err = stats.linregress(
    pace_deliv_values, pace_bvrz_values)

spin_slope, spin_intercept, spin_r_value, spin_p_value, spin_std_err = stats.linregress(
    spin_deliv_values, spin_bvrz_values)

plt.plot(pace_deliv_values, pace_bvrz_values, 'o', label='pace')
plt.plot(pace_deliv_values, pace_intercept + pace_slope * pace_deliv_values, 'r')
plt.legend()
plt.show()

plt.plot(spin_deliv_values, spin_bvrz_values, 'o', label='spin')
plt.plot(spin_deliv_values, spin_intercept + spin_slope * spin_deliv_values, 'r')
plt.legend()
plt.show()
