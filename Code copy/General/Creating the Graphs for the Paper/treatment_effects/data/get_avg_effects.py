import pandas as pd


treatment_effects_df = pd.read_csv('treatment_df.csv')
p_values_df = pd.read_csv('p_values.csv')

# Remove the minimal p-value from the p_values_df
p_values_df = p_values_df[p_values_df['case'] != "min_p_value"]

# add a case in the case column called "case_avg", which is the average of all cases
avg_effects = pd.DataFrame(columns=['case', 'avg_effect', 'low-95-bound', 'high-95-bound', 'lowest p-value', 'highest p-value'])

import numpy as np

# Ensure the 'case' columns have the same data type
treatment_effects_df['case'] = treatment_effects_df['case'].astype(int)
p_values_df['case'] = p_values_df['case'].astype(int)

# Group data by 'case' and calculate mean, standard deviation, and count for treatment_effect
grouped_treatment = treatment_effects_df.groupby('case')['treatment_effect'].agg(['mean', 'std', 'count'])

# Calculate standard error
grouped_treatment['std_error'] = grouped_treatment['std'] / np.sqrt(grouped_treatment['count'])

# Calculate 95% confidence interval
grouped_treatment['low-95-bound'] = grouped_treatment['mean'] - 1.96 * grouped_treatment['std_error']
grouped_treatment['high-95-bound'] = grouped_treatment['mean'] + 1.96 * grouped_treatment['std_error']

# Group data by 'case' and calculate the lowest and highest p_value
grouped_p_values = p_values_df.groupby('case')['p_value'].agg(['min', 'max'])
grouped_p_values.columns = ['lowest p-value', 'highest p-value']

# Merge the two dataframes on 'case'
avg_effects = pd.merge(grouped_treatment, grouped_p_values, on='case').reset_index()

# Rename and drop unnecessary columns
avg_effects = avg_effects[['case', 'mean', 'std', 'low-95-bound', 'high-95-bound', 'lowest p-value', 'highest p-value']]
avg_effects.columns = ['case', 'avg_effect', 'sd_effect', 'low-95-bound', 'high-95-bound', 'lowest p-value', 'highest p-value']

# Calculate mean, standard deviation, and count for all treatment_effects without grouping by case
all_treatment = treatment_effects_df['treatment_effect'].agg(['mean', 'std', 'count'])

# Calculate standard error for the "all" case
all_treatment['std_error'] = all_treatment['std'] / np.sqrt(all_treatment['count'])

# Calculate 95% confidence interval for the "all" case
all_treatment['low-95-bound'] = all_treatment['mean'] - 1.96 * all_treatment['std_error']
all_treatment['high-95-bound'] = all_treatment['mean'] + 1.96 * all_treatment['std_error']

# Calculate the lowest and highest p_value for the "all" case
all_p_values = p_values_df['p_value'].agg(['min', 'max'])
all_p_values.columns = ['lowest p-value', 'highest p-value']

# Combine the "all" case statistics into a single row DataFrame
all_case = pd.DataFrame({'case': 'all',
                         'avg_effect': all_treatment['mean'],
                         'sd_effect': all_treatment['std'],
                         'low-95-bound': all_treatment['low-95-bound'],
                         'high-95-bound': all_treatment['high-95-bound'],
                         'lowest p-value': all_p_values['min'],
                         'highest p-value': all_p_values['max']}, index=[0])

# Append the "all" case to the avg_effects DataFrame
avg_effects = avg_effects.append(all_case, ignore_index=True)

# Round the values in the DataFrame to 2 decimal places
avg_effects = avg_effects.round(2)

print(avg_effects)
avg_effects.to_csv('avg_effects.csv', index=False)
avg_effects.to_latex('avg_effects.tex', index=False)


