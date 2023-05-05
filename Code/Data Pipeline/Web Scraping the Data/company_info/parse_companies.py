import pandas as pd
import os
from bs4 import BeautifulSoup 
from helpers import *


def parse_one_company(html_file):
    soup = BeautifulSoup(html_file, "html.parser")
    row = {
        "employees_link": get_employees_link(soup),
        "website_link": get_website_link(soup),
        "industry": get_industry(soup),
        "followers": get_followers(soup),
        "long_description": get_long_description(soup),
        "employees_on_linkedin": get_employees_on_linkedin(soup),
        "employees_total": get_employees_total(soup),
        "founded": get_founded(soup),
        "specialties": get_specialties(soup)
    }
    return row

def main():
    df = pd.DataFrame(columns=['name', 'employees_link', 'website_link', 'industry', 'followers', 'long_description', 'employees_on_linkedin', 'employees_total', 'founded', 'specialties'])
    os.chdir('companies')
    for file_name in os.listdir('.'):
        # The index is the first part of the file name
        i = file_name.split('_')[0]
        # The name is the second part of the file name
        name = file_name.split('_')[1].split('.html')[0].strip()
        if not file_name.endswith('.html'):
            continue
        with open(file_name, 'r') as f:
            row = parse_one_company(f)
            row['name'] = name
            # insert the row into the dataframe at index i
            df.loc[i] = row
    os.chdir('..')
    df.to_csv("master+about.csv")
    df.to_pickle("master+about.pkl")
if __name__ == "__main__":
    main()


