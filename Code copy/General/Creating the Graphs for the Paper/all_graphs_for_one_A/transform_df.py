import pandas as pd

# Read the CSV file
data = pd.read_csv('master_df_0.csv')

# Create an empty DataFrame for the transformed data
transformed_data = pd.DataFrame(columns=['month', 'diff', 'value', 'unit_category'])

# Loop through the columns in the data
print(data.columns[2:])
for col in data.columns[2:]:
    # Get the canton name
    canton = col[-2:]
    if col == f'Y_star_{canton}':
        continue

    # Calculate the difference between Y and Y_star values
    print(canton)
    print(col)
    diff = data[col] - data['Y_star' + col[1:]]

    # Create a temporary DataFrame with the transformed data for the current canton
    temp_df = pd.DataFrame({
        'month': data['month'],
        'diff': diff,
        'value': diff,
        'unit_category': canton
    })

    # Append the temporary DataFrame to the transformed_data DataFrame
    transformed_data = transformed_data.append(temp_df, ignore_index=True)

# Sort the transformed data by month
transformed_data = transformed_data.sort_values(by='month').reset_index(drop=True)

# Save the transformed data to a CSV file
transformed_data.to_csv('transformed_data.csv', index=False)
