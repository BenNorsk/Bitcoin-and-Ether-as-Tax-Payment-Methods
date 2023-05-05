import pandas as pd


# Read in the data
df = pd.read_csv('0_synth_ZG.csv')
weights = pd.read_csv('0_weights.csv')
print(weights)

# add value
def add_value(name, df, weights):
    value = 0
    for index, row in weights.iterrows():
        abbr = row['canton']
        # Get the value in the df in the column "name" and the row where the canton is abbr
        weight = 0 if pd.isna(row["weights"]) else row["weights"]
        cantonal_value = 0 if pd.isna(df[df['canton'] == abbr][name].values[0]) else df[df['canton'] == abbr][name].values[0]
        value += cantonal_value * weight
        print(abbr)
        print(value)
        
    # Add the value to the df in the "name" column where canton = synth_ZG
    df.loc[df['canton'] == 'synth_ZG', name] = value
    return df


# Limit the data to the day == 1796
df = df[df['days'] == 1796]

df = add_value("taxes", df, weights)
df = add_value("working_population", df, weights)
df = add_value("share of financial sector", df, weights)
df = add_value("share of IT sector", df, weights)

# Round all values to 2 decimal places
df = df.round(2)

# Only select the rows, where the canton is ZG or synth_ZG
df = df[df['canton'].isin(['ZG', 'synth_ZG'])]

# Only select the columns, where the name is "canton", "companies", "taxes", "working_population", "share of financial sector", "share of IT sector"
df = df[['canton', 'companies', "taxes", "working_population", "share of financial sector", "share of IT sector"]]

# Use the melt function to create a long format of the DataFrame
df_melted = df.melt(id_vars=['canton'], var_name='variables', value_name='value')

# Use the pivot function to reshape the melted DataFrame into the desired format
df_pivoted = df_melted.pivot(index='variables', columns='canton', values='value')

# Remove the index
df_pivoted.reset_index(inplace=True)


print(df_pivoted)

# save as csv
df_pivoted.to_csv('formatted_table.csv', index=False)

df_pivoted.to_latex('comparison_table.tex', index=False)