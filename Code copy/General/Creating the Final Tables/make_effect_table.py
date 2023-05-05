import pandas as pd
from tables import *

def get_new_name(case, cutoff):
    name = f'Case {str(int(case))} (A 3.{str(int(cutoff))})'
    return name

treatment = pd.read_csv("treatment_df.csv")
# Make cutoff an integer
treatment['cutoff'] = treatment['cutoff'].astype(int)
treatment['case'] = treatment['case'].astype(int)
p_values = pd.read_csv("p_values.csv")
# Make cutoff an integer
p_values = p_values[p_values['case'] != "min_p_value"]
p_values['cutoff'] = p_values['cutoff'].astype(int)
p_values['case'] = p_values['case'].astype(int)
# Remove the rows where case == "min_p_value



print(treatment)
print(p_values)

merged_df = treatment.merge(p_values, on=['cutoff', 'case'])

# Define a new column called "$e \in \mathbf{RM}$" which defined as follows:
# 
merged_df['$e \in \mathbf{RM}$'] = merged_df.apply(lambda row: get_new_name(row['case'], row['cutoff']), axis=1)


# Remove the columns "case" and "cutoff"
merged_df = merged_df.drop(columns=['case', 'cutoff'])

# Reorder the columns
merged_df = merged_df[['$e \in \mathbf{RM}$',  'treatment_effect', 'p_value']]

# Rename the columns
merged_df = merged_df.rename(columns={'$e \in \mathbf{RM}$': "Case in Robustness Matrix", "treatment_effect": "Treatment Effect", "p_value": "P-Value"})

merged_df.to_csv("Effects and P-Values for the entire Robustness Matrix.csv", index=False)
save_df_as_ltablex_booktabs(merged_df, "effect_table.tex", caption='Effects and P-Values for the entire Robustness Matrix', label='tab:Effects and P-Values for the entire Robustness Matrix')

