# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

%matplotlib inline

df = pd.read_csv('usmaan_test_data.csv')

df.head()

y_pace_vals = df.bvrz[df.pace == 0].dropna(how='any')
y_spin_vals = df.bvrz[df.pace == 1].dropna(how='any')

x_pace_vals = y_pace_vals.index
x_spin_vals = y_spin_vals.index

pace_slope, pace_intercept, pace_r_value, pace_p_value, pace_std_err = stats.linregress(
    x_pace_vals, y_pace_vals)

spin_slope, spin_intercept, spin_r_value, spin_p_value, spin_std_err = stats.linregress(x_spin_vals, y_spin_vals)

plt.plot(x_pace_vals, y_pace_vals, 'o', label='pace')
plt.plot(x_pace_vals, pace_intercept + pace_slope * x_pace_vals, 'r')
plt.legend()
plt.show()

plt.plot(x_spin_vals, y_spin_vals, 'o', label='spin')
plt.plot(x_spin_vals, spin_intercept + spin_slope * x_spin_vals, 'r')
plt.legend()
plt.show()
