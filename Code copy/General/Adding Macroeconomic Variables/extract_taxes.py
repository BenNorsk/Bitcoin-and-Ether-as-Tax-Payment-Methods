import pandas as pd

# Main df
main_df = pd.DataFrame()
# files
files = ["taxes_2016.xlsx", "taxes_2017.xlsx", "taxes_2018.xlsx", "taxes_2019.xlsx", "taxes_2020.xlsx", "taxes_2021.xlsx"]

year = 2016
for file in files:
    # Read in the Excel file
    xls = pd.ExcelFile(f'taxes/{file}')

    if year <= 2018:
        # Read in the relevant sheet
        df = pd.read_excel(xls, sheet_name='Seite 62-63', usecols='A,E', skiprows=40)
    else:
        # Read in the relevant sheet
        df = pd.read_excel(xls, sheet_name='Seiten 2-3', usecols='A,E', skiprows=40)
    # Rename the columns to be more descriptive
    df.columns = ['Province', year]

    # Join the dataframes
    main_df = pd.concat([main_df, df], axis=1)

    # Print the resulting dataframe
    print(df)
    year += 1

# Remove duplicate columns
main_df = main_df.loc[:,~main_df.columns.duplicated()]
print(main_df.head())

# Translation dictionary
translation_dict = {
    "Zürich": 'ZH',
    'Bern': 'BE',
    'Luzern': 'LU',
    'Altdorf': 'UR',
    'Schwyz': 'SZ',
    'Sarnen': 'OW',
    'Stans': 'NW',
    'Glarus': 'GL',
    'Zug': 'ZG',
    'Freiburg': 'FR',
    'Solothurn': 'SO',
    'Basel': 'BS',
    "Liestal": 'BL',
    'Schaffhausen': 'SH',
    "Herisau": 'AR',
    "Appenzell": 'AI',
    'St. Gallen': 'SG',
    'Chur': 'GR',
    'Aarau': 'AG',
    'Frauenfeld': 'TG',
    'Bellinzona': 'TI',
    'Lausanne': 'VD',
    'Sitten': 'VS',
    'Neuenburg': 'NE',
    'Genf  4)': 'GE',
    'Delsberg': 'JU'
}

cleaned_df = pd.DataFrame()

# Translate the province names
for index, row in main_df.iterrows():
    province = row['Province']
    try:
        print("province: ", province.strip())
        canton = translation_dict[province.strip()]
        print(canton)
    except:
        canton = None
    if canton is not None:
        # Add the row to the new dataframe
        row['canton'] = canton
        # Drop the province column
        row = row.drop('Province')
        cleaned_df = cleaned_df.append(row)
        


# Drop the province column
print(cleaned_df.head())
print(cleaned_df)

# Save the cleaned data to a CSV file
cleaned_df.to_csv('taxes.csv', index=False)
cleaned_df.to_pickle('taxes.pkl')

