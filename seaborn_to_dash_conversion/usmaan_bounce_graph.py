import pymysql
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

%matplotlib inline  

bg_col = '#F4F4EC'
grey_col = '#404040'
col_list = ['#37B36C', '#FBAA40', '#D9437D', '#367D9F']

sns.set_style('whitegrid')
plt.rcParams['axes.titlesize'] = 20
plt.rcParams['axes.labelsize'] = 18
plt.rcParams['legend.fontsize'] = 14
plt.rcParams['axes.titleweight'] = 'bold'
sns.set_palette(col_list + [grey_col])

################################
# NOTE: pysql_code.py goes here.
################################

df = pd.read_csv('usmaan_test_data.csv')

# add count of delivery number
df['deliv'] = [n + 1 for n in range(len(df))]

# drop null bounces
df = df.dropna(subset=['bvrz']).copy()

# draw something
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_facecolor(bg_col)
bvr_min = None
bvr_max = None

# NOTE: First run caused the following error
#   - ModuleNotFoundError: No module named 'statsmodels'
for p in (1, 0):
    df2 = df[df.pace == p]
    sns.regplot(
        x='deliv',
        y='bvrz',
        data=df2,
        scatter=True,
        lowess=True,
        scatter_kws={'color': col_list[3 - p], 'alpha': 0.1},
        line_kws={'color': col_list[3 - p], 'lw': 4, 'alpha': 0.9},
        label=['pace' if p == 1 else 'spin'][0]
    )

    if bvr_max is None or np.percentile(df2['bvrz'], 99) > bvr_max:
        bvr_max = np.percentile(df2['bvrz'], 99)

    if bvr_min is None or np.percentile(df2['bvrz'], 1) < bvr_min:
        bvr_min = np.percentile(df2['bvrz'], 1)

leg = ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

for lh in leg.legendHandles:
    lh.set_alpha(1)

ax.set(
    xlabel='Match delivery',
    ylabel='Bounce velocity ratio'
)

ax.set_ylim([bvr_min, bvr_max])

# add a vertical line to represent the change of innings
for i in range(2, 1 + len(df.inn.unique())):
    istart = df[df.inn == i]['deliv'].idxmin()
    ax.axvline(x=istart - 0.5, zorder=1, lw=2, alpha=0.5, color=grey_col)

plt.savefig('%s_bounce_ratio' %
            match_id, facecolor=bg_col, bbox_inches='tight')

plt.close()

# Exploration

# There are
#   - 9 null values in speed
#   - 9 null values in bvrz
df.isnull().sum()

# Dataframe consisting of
#   - All rows with a null value in either column
null_entries = df[df.isnull().any(axis=1)]