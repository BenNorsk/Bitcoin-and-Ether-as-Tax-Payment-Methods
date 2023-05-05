import pandas as pd

# Read the data from the pickle
df = pd.read_pickle('smart_industry_data.pkl')
print(df.columns)

# Select only the name and the industry columns
df = df[['month', 'canton', "companies", 'share of financial sector','share of IT sector']]

# reset the index
df = df.reset_index(drop=True)

# New method
middle = len(df) // 2
middle_df = df.iloc[(middle - 2):(middle +2)]
new_df = pd.concat([df.head(1), middle_df, df.tail(1)])

# round to 2 decimals
new_df = new_df.round(2)

# Write the top5 to latex
new_df.to_latex('new_df.tex')

# create a df consisting of the data of the first company and the last 2 companies
top5 = df.head(3)
print(top5)
last2 = df.tail(2)
print(last2)

# 


# Write the top5 to latex
top5.to_latex('top3.tex')
last2.to_latex('last2.tex')

# Create a summary statistics table 
