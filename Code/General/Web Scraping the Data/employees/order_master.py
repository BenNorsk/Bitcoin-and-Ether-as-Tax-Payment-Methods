import pandas as pd


df = pd.read_pickle("master+about.pkl")
# Conver index to int
df.index = df.index.astype(int)
# Sort the index
df = df.sort_index()
# Save the dataframe
df.to_pickle("master+about.pkl")
print(df)