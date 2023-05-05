import pandas as pd

# Read the data from the pickle
df = pd.read_csv('summary_statistics_control_variables.csv')
print(df.columns)

# Select the row where the canton is "ZG"
zg = df.loc[df['canton'] == 'ZG']
zh = df.loc[df['canton'] == 'ZH']
ge = df.loc[df['canton'] == 'GE']
ti = df.loc[df['canton'] == 'TI']
vd = df.loc[df['canton'] == 'VD']
others = df.loc[df['canton'] == 'avg. other canton']

# concat the rows
df = pd.concat([zg, zh, ge, ti, vd, others])


# Make only 2 decimals
df = df.round(2)

# Write the top5 to latex
df.to_latex('summary_statistics_companies_control.tex', index=False)


