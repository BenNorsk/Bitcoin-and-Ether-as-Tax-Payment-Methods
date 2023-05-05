import pandas as pd
import os
from bs4 import BeautifulSoup 

def get_companies_list(path):
    with open(path, 'r') as f:
        data = f.read()

    df = pd.DataFrame(columns=['name', 'zefix_link', 'cantonal_excerpt', 'uid', 'legal_form', 'hq', 'canton', 'deleted'])

    # Parse the file
    soup = BeautifulSoup(data, 'html.parser')

    # Get the table
    table = soup.find('tbody', attrs={'role': 'rowgroup'})

    # Get the rows
    rows = table.find_all('tr')

    # Read the rows
    for row in rows:
        # Get the columns
        data_row = {}
        # get the first child of the td element

        company_name_cell = row.find('td', attrs={'class': 'companyNameCell'})
        data_row["name"] = company_name_cell.find('a').text
        data_row["zefix_link"] = company_name_cell.find('a').get("href")
        cantonal_excerpt_cell = row.find('td', attrs={'class': 'companyExcerptCell'})
        try:
            data_row["cantonal_excerpt"] = cantonal_excerpt_cell.find('a').get("href")
        except:
            data_row["cantonal_excerpt"] = None
        uid_cell = row.find('td', attrs={'class': 'companyUidCell'})
        try:
            data_row["uid"] = uid_cell.find('a').text
        except:
            data_row["uid"] = None
        data_row["legal_form"] = row.find('td', attrs={'class': 'companyLegalFormCell'}).text
        data_row["hq"] = row.find('td', attrs={'class': 'cdk-column-legalSeat'}).text
        data_row["canton"] = row.find('td', attrs={'class': 'companyRegOfficeCell'}).text

        # If the company name cell contains the class "deletedFirm", then set data_row["deleted"] to True
        if "deletedFirm" in company_name_cell.get("class"):
            data_row["deleted"] = True
        else:
            data_row["deleted"] = False
        # Concatenate the row to the df
        df = df.append(data_row, ignore_index=True)
    return df

def get_paths_from_keyword(keyword):
    paths = []
    for root, dirs, files in os.walk(keyword):
        for file in files:
            if file.endswith(".html"):
                paths.append(os.path.join(root, file))
    return paths


def get_all_companies():
    # Path to the file
    paths = []
    # Get all paths to all files in the folders: Web3, NFT, Crypto, Blockchain and Bitcoin
    
    paths.extend(get_paths_from_keyword("Web3"))
    paths.extend(get_paths_from_keyword("NFT"))
    paths.extend(get_paths_from_keyword("Crypto"))
    paths.extend(get_paths_from_keyword("Blockchain"))
    paths.extend(get_paths_from_keyword("Bitcoin"))


    # New df
    df = pd.DataFrame(columns=['name', 'zefix_link', 'cantonal_excerpt', 'uid', 'legal_form', 'hq', 'canton', 'deleted'])
    for path in paths:
        df = df.append(get_companies_list(path), ignore_index=True)
    return df

def main():
    df = get_all_companies()
    print(df)
    df.to_pickle('zefix_companies.pkl')
    df.to_csv('zefix_companies.csv')

if __name__ == "__main__":
    main()


