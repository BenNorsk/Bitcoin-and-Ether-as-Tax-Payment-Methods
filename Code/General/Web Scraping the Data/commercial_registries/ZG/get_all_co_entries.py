import pandas as pd


df = pd.read_pickle('../master+about+location.pkl')
df_zg = df[df['canton'] == 'ZG']

print(df_zg)