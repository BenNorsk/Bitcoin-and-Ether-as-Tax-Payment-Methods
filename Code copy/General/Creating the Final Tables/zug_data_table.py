import pandas as pd
from tables import save_df_as_ltablex_booktabs
import re

def rename_variable(variable_name):
    pattern = r"A_{(\d+)}\((\\bar\{(\w+)})"
    match = re.search(pattern, variable_name)
    y_or_x = match.group(3)
    cutoff = match.group(1)
    if y_or_x == "x":
        pattern = r"_\{(\w+)_{2020\}"
        match = re.search(pattern, variable_name)
        print(match)
        print(match.group(1))
        variable = match.group(1)
        formatted_string = f'Avg. {variable} in 2020, A 3.{cutoff}'
    else:
        formatted_string = f'Avg. Y in 2020, A 3.{cutoff}'
    return formatted_string



df = pd.read_csv("robustness_matrix_goodness_of_fit.csv")
# Do remove the index column

print(df)
# name the variables column ""
df = df.rename(columns={"": "variables", 'synth. ZG ($C_{0}$)': "Synthetic ZG, Case 0", 'synth. ZG ($C_{1}$)': "Synthetic ZG, Case 1", 'synth. ZG ($C_{2}$)': "Synthetic ZG, Case 2", 'synth. ZG ($C_{3}$)': "Synthetic ZG, Case 3", 'synth. ZG ($C_{4}$)': "Synthetic ZG, Case 4"})

print(df)
for index, row in df.iterrows():
    df.at[index, "variables"] = rename_variable(row["variables"])

df.to_csv("Goodness of Fit for all Cases in the Robustness Matrix.csv", index=False)

print(df)
# round the numbers to 2 decimal places
save_df_as_ltablex_booktabs(df.round(2), "robustness_matrix_goodness_of_fit.tex", "Goodness of Fit for all Cases in the Robustness Matrix", "tab: robustness_matrix_goodness_of_fit")


