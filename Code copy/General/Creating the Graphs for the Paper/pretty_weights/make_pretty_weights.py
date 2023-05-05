import pandas as pd

# Read the data from the CSV file using pandas
data = pd.read_csv('0_weights.csv')

# Round the weights column to 2 decimal places
data['weights'] = data['weights'].round(2)

# Create the LaTeX table
table = data.to_latex(index=False, header=['Canton', 'Weight'], column_format='|c|c|')

# Print the LaTeX table
print(table)

# Save the LaTeX table to a file
with open('0_weights.tex', 'w') as f:
    f.write(table)
