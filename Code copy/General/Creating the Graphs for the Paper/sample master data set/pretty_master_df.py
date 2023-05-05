import pandas as pd

df = pd.read_pickle('aggregated_industry_data.pkl')

# Select only these columns: share of financial sector  share of IT sector      taxes  working_population  treatment companies month
df = df[['month', 'days', 'canton', "companies", 'share of financial sector','share of IT sector', 'working_population', 'taxes', "treatment"]]
print(df)

# Cantons to summarise
# Select all cantons, whose highest company count < 5
cantons_to_summarise = df.groupby('canton')['companies'].max()
print(cantons_to_summarise)
# Select all cantons, whose highest company count < 5
selected_cantons = cantons_to_summarise[cantons_to_summarise < 10]
print(selected_cantons)

# Iterate over all months 
for month in df['month'].unique():
    sub_df = df[df['month'] == month]
    # Create a new row called "all other cantons"
    # Select all rows, where the canton is in the selected cantons
    rows = sub_df[sub_df['canton'].isin(selected_cantons.index)]
    # Sum all rows, where the canton is in the selected cantons
    new_row = rows.mean()
    # Set the month to the current month
    new_row['month'] = month
    # Set the canton to "all other cantons"
    new_row['canton'] = 'avg. other canton'
    print(new_row)
    # Add the new row to the df
    df = df.append(new_row, ignore_index=True)
print(df.tail(40))

# Delete all rows, where the canton is in the selected cantons
df = df[~df['canton'].isin(selected_cantons.index)]

# Save as CSV and pickle as pretty_master_data
df.to_csv('pretty_master_data.csv')
df.to_pickle('pretty_master_data.pkl')
