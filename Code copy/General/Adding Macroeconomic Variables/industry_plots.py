import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read in the data
df = pd.read_pickle('industry_data.pkl')
df_zug = df[df['canton'] == 'ZG']

# Select the cantons of GE, ZH, VD, TI
df_zurich = df[df['canton'] == 'ZH']
df_vaud = df[df['canton'] == 'VD']
df_ticino = df[df['canton'] == 'TI']

# Make a time series plot where you plot the companies column against the month column, grouped by canton
df.groupby(['month', 'canton'])['companies'].sum().unstack().plot()
# Save the plot
plt.savefig('companies_per_month.png')