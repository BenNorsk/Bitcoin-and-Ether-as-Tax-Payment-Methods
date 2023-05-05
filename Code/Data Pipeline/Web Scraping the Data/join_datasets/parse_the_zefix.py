# Import beautifulsoup4
from bs4 import BeautifulSoup
import pandas as pd
import re
import os

def get_one_table_data_pair(table, main_text):
    try:
        # Get the th who reads "Adresse"
        th = table.find('th', text=main_text)
        # Get the next table data
        td_text = th.find_next('td').text
        return td_text
    except:
        return None

def get_the_purpose(soup):
    # Find the th element which reads "Zweck"
    try:
        purpose = soup.find('th', text='Zweck').parent.find_next('tr').find('td').text
        return purpose
    except:
        return None

def get_the_registry_date(soup):
    try:
        # Find all "zfx-shab-publication" elements
        all_shab_publications = soup.find_all('zfx-shab-publication')
        # Get the last one
        last_shab_publication = all_shab_publications[-1]
        # Find the td which with the title "SHAB Publ."
        date_raw =  last_shab_publication.find('td', title='SHAB Publ.').text
        # Extract the date using regex
        registry_date = re.findall(r'\d{2}\.\d{2}\.\d{4}', date_raw)[0]
        return registry_date
    except:
        return None

def get_company_name(soup):
    try:
        name = soup.find('h3', {'class': 'companyName'}).text
        return name
    except:
        return None

def get_data_row(file_path):
    # Open the file
    with open(file_path, 'r') as f:
        # Read the file
        page = f.read()
    # Parse the file
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find('table', {'class': 'companyInfoTable'})
    # Get the table data
    row = {
        'name': get_company_name(soup),
        'address': get_one_table_data_pair(table, 'Adresse'),
        'plz_city': get_one_table_data_pair(table, 'PLZ / Ort'),
        'legal_form': get_one_table_data_pair(table, 'Rechtsform'),
        'seat': get_one_table_data_pair(table, 'Sitz'),
        'status': get_one_table_data_pair(table, 'Status'),
        'uid': get_one_table_data_pair(table, 'UID'),
        'ch_id': get_one_table_data_pair(table, 'CH-ID'),
        'ehra_id': get_one_table_data_pair(table, 'EHRA-ID'),
        'auditor': get_one_table_data_pair(table, 'Revisionsstelle/n'),
        'purpose': get_the_purpose(soup),
        'registry_date': get_the_registry_date(soup)
    }
    return row

def main():
    df = pd.DataFrame(columns=['id','name', 'address', 'plz_city', 'legal_form', 'seat', 'status', 'uid', 'ch_id', 'ehra_id', 'auditor', 'purpose', 'registry_date'])
    df2 = pd.read_pickle('master+about+location.pkl')
    for file in os.listdir('looked_up_companies'):
        id = int(file.split('_')[0])
        row = {}
        try:
            row = get_data_row(f'looked_up_companies/{file}')
            row["id"] = id
        except:
            row["id"] = id
        df = df.append(row, ignore_index=True)
    # Outer join the two dataframes
    df3 = pd.merge(df2, df, on='id', how='outer')
    df3.to_pickle('master+about+location+co_entry.pkl')
    df3.to_csv('master+about+location+co_entry.csv')
    # print summary statistics
    print(df3.describe())

if __name__ == '__main__':
    main()