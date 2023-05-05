import pandas as pd

df = pd.read_csv('automatise/aggregated_industry_data.csv')
# These are the columns
# month,days,canton,companies,employees,followers,other legal forms,AG's,GmbH's,share of AG's,share of GmbH's,financial sector,IT sector,other sectors,share of financial sector,share of IT sector,taxes,working_population,treatment
# Keep and rename: Month, Canton, Companies (Y), Tax Burden (TX), Working Population (WP), Share of financial Sector (f), Share of IT Sector (it)
df = df[['month', 'canton', 'companies', 'taxes', 'working_population', 'share of financial sector', 'share of IT sector', 'treatment']]
df.columns = ['Month', 'Canton', 'Companies (Y)', 'Tax Burden (TX)', 'Working Population (WP)', 'Share of financial Sector (f)', 'Share of IT Sector (it)', 'Treatment (t)']
print(df)

# Save as csv
df.to_csv('Master Sample Data Set.csv', index=False)