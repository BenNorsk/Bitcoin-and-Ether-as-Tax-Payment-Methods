import pandas as pd

# Read the data from the pickle
df = pd.read_pickle('aggregated_industry_data.pkl')
print(df.columns)

# Select only the name and the industry columns
df = df[['month', 'canton', "companies", 'working_population', 'taxes', 'share of financial sector','share of IT sector', "treatment"]]
# share of financial sector	share of IT sector taxes	working_population canton	companies month
# Rename the industry column as "sector"
df = df.reset_index(drop=True)

# Make a new df, with the first 1 row, the three middle rows and the last 1 row
middle = len(df) // 2
middle_df = df.iloc[(middle + 804):(middle + 810)]
new_df = pd.concat([df.head(1), middle_df, df.tail(1)])

# round to 2 decimals
new_df = new_df.round(2)

# Write the top5 to latex
new_df.to_latex('new_df.tex')
