import pandas as pd
import matplotlib.pyplot as plt

# Read in the data
df = pd.read_pickle('industry_data.pkl')

print(df.sum())

# Rank the df.sum() by the values
# Reduce it to the numeric columns
df_numeric = df.select_dtypes(include=['float64', 'int64'])
ranked = df_numeric.sum().sort_values(ascending=False)
# Divide all values by 7 * 12 to get the average monthly value
print(ranked)