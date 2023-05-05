import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

# Load the data
df = pd.read_pickle('smart_industry_data.pkl')
taxes = pd.read_pickle('taxes.pkl')
working_population = pd.read_pickle('working_population.pkl')

# Merge the data
for index, row in df.iterrows():
    year = row['month'].year
    print(year)
    tax_year = None
    pop_year = None
    if year <= 2021:
        # Get the tax year
        canton_row = taxes.loc[taxes['canton'] == row['canton']]
        tax_year = canton_row[year].values[0]
        # Get the working population
        pop_row = working_population.loc[working_population['canton'] == row['canton']]
        print(pop_row)
        pop_year = pop_row[str(year)].values[0]
    # Insert the tax value into the df
    df.at[index, 'taxes'] = tax_year
    df.at[index, 'working_population'] = pop_year
    # Add the "treatment"
    if row['canton'] == 'ZG' and row["days"] >= 1827:
        df.at[index, 'treatment'] = 1
    else:
        df.at[index, 'treatment'] = 0

print(df.head())
print(df.tail())
print(df)

# Save the data without the index
df.to_pickle('aggregated_industry_data.pkl')
df.to_csv('aggregated_industry_data.csv', index=False)



