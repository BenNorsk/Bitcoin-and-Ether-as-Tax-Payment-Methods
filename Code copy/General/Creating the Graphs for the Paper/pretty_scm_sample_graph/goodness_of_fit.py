import pandas as pd
import numpy as np

# ONLY NEEDED TO ADD THE CONTROL VARIABLES
# df = pd.read_csv('example_scm.csv')
# df.head()

# # Add a fake control_variable called CV equal to 1 with some simulated noise
# df['CV'] = 1 + 0.5 * np.random.randn(df.shape[0])
# df['CV_1'] = 1.2 * df['CV'] + 0.1 * np.random.randn(df.shape[0])

# # Save the new dataframe
# df.to_csv('example_scm_with_control_variable.csv', index=False)

df = pd.read_csv('example_scm_with_control_variable.csv')
# Get the df for t > 10 and t <= 20
df = df[(df['t'] > 10) & (df['t'] <= 20)]
# Get the mean
print(df.mean().round(2))

#