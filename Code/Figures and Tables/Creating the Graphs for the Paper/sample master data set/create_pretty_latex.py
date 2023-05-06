import pandas as pd

# Read the data from the pickle
df = pd.read_csv('summary_statistics_companies.csv')
print(df.columns)

# Order by "max_companies" and reset the index
df = df.sort_values(by=['max_companies'], ascending=False)
df = df.reset_index(drop=True)


# Reorder the columns, to canton, max_companies, min_companies, mean_companies, sd_companies, p25_companies,	p50_companies,	p75_companies
df = df[['canton', 'max_companies', 'min_companies', 'mean_companies', 'sd_companies', 'p25_companies', 'p50_companies', 'p75_companies']]

# Make only 2 decimals
df = df.round(2)

# Write the top5 to latex
df.to_latex('summary_statistics_companies.tex', index=False)


