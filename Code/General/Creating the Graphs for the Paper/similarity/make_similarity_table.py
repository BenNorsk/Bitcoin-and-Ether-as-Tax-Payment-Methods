import pandas as pd




# add value
def add_value(name, df, weights):
    value = 0
    for index, row in weights.iterrows():
        abbr = row['canton']
        # Get the value in the df in the column "name" and the row where the canton is abbr
        weight = 0 if pd.isna(row["weights"]) else row["weights"]
        cantonal_value = 0 if pd.isna(df[df['canton'] == abbr][name].values[0]) else df[df['canton'] == abbr][name].values[0]
        value += cantonal_value * weight
        
    # Add the value to the df in the "name" column where canton = synth_ZG
    df.loc[df['canton'] == 'synth_ZG', name] = value
    return df

def make_comparison_for_one_case(synth_file, weights_file):
    # Read in the data
    df = pd.read_csv(synth_file)
    weights = pd.read_csv(weights_file)
    # Remove row where the canton is na
    # 2020-12-31,1796
    # 2020-01-31,1461
    # Reduce the df to only contain rows where days >= 1461 and days <= 1796
    df = df[(df['days'] >= 1461) & (df['days'] <= 1796)]
    df = add_value("taxes", df, weights)
    df = add_value("working_population", df, weights)
    df = add_value("share of financial sector", df, weights)
    df = add_value("share of IT sector", df, weights)
    print(df)
    # Now give me in each column just the mean value, but while maintaining the current shape and the canton column
    df = df.groupby(['canton']).mean()
    # Now make the canton column a normal column
    df.reset_index(inplace=True)
    print(df)

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
    return df_pivoted

agg_df = pd.DataFrame()

for i in range(0, 5):
    df = make_comparison_for_one_case(f'0_synth_ZG_case_{i}.csv', f'0_weights_case_{i}.csv')
    # Add the synth_ZG column to the df
    df['case_{}'.format(i)] = df['synth_ZG']
    
    # Append the df to the aggregated dataframe
    agg_df = pd.concat([agg_df, df], axis=1)

# Delete columns with the name "synth_ZG"
agg_df = agg_df.loc[:,~agg_df.columns.duplicated()]

# Delete colunn with the name "synth_ZG"
agg_df = agg_df.drop(columns=['synth_ZG'])

print(agg_df)

# Save it to csv
agg_df.to_csv("similarity_table.csv", index=False)
# Save it to latex
agg_df.to_latex("similarity_table.tex", index=False, float_format="%.2f")


