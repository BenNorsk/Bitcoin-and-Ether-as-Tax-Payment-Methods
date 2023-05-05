import pandas as pd

# Create a list of years to loop through
years = ['2021', '2020', '2019', '2018', '2017', '2016']

# Create an empty dataframe to store the results
pop_df = pd.DataFrame()

# Loop through each year and add the population data to the dataframe
for year in years:
    # Read in the population data for the current year
    df = pd.read_excel('population.xlsx', sheet_name=year, usecols='A,D', skiprows=5)
    
    # Rename the columns to be more descriptive
    df.columns = ['Province', year]
    
    # Append the current year's data to the main dataframe
    pop_df = pd.concat([pop_df, df], axis=1)

# Translation dictionary
translation_dict = {
    'Zürich': 'ZH',
    'Bern': 'BE',
    'Luzern': 'LU',
    'Uri': 'UR',
    'Schwyz': 'SZ',
    'Obwalden': 'OW',
    'Nidwalden': 'NW',
    'Glarus': 'GL',
    'Zug': 'ZG',
    'Freiburg': 'FR',
    'Solothurn': 'SO',
    'Basel-Stadt': 'BS',
    'Basel-Landschaft': 'BL',
    'Schaffhausen': 'SH',
    'Appenzell A. Rh.': 'AR',
    'Appenzell I. Rh.': 'AI',
    'St. Gallen': 'SG',
    'Graubünden': 'GR',
    'Aargau': 'AG',
    'Thurgau': 'TG',
    'Tessin': 'TI',
    'Waadt': 'VD',
    'Wallis': 'VS',
    'Neuenburg': 'NE',
    'Genf': 'GE',
    'Jura': 'JU'
}

cleaned_df = pd.DataFrame()

# Translate the province names
for index, row in pop_df.iterrows():
    province = row['Province'][0]
    print(province)
    try:
        canton = translation_dict[province]
    except KeyError:
        canton = None
    if canton is not None:
        # Add the row to the new dataframe
        row['canton'] = canton
        # Drop the province column
        row = row.drop('Province')
        cleaned_df = cleaned_df.append(row)

# Save the cleaned data to a CSV file
cleaned_df.to_csv('working_population.csv', index=False)
cleaned_df.to_pickle('working_population.pkl')
