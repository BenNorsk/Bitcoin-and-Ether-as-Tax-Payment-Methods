import pandas as pd
from bs4 import BeautifulSoup
import sys
import os


def extract_valuable_fields_from_html(soup):
    # class = reusable-search__entity-result-list
    companies = [] 
    listings = soup.find_all('li', {'class': 'reusable-search__result-container'})
    for listing in listings:
        # Save the listing as html file
        with open('example.html', 'w') as f:
            f.write(listing.prettify())

        name = listing.find_all("a", {"class": "app-aware-link"})[1].text
        location_and_industry = listing.find("div", {"class": "entity-result__primary-subtitle"}).text
        # Split into two by "•"
        try:
            location = location_and_industry.split("•")[1]
            industry = location_and_industry.split("•")[0]
        except IndexError:
            industry = location_and_industry
            location = location_and_industry
        try:
            description = listing.find("p", {"class": "entity-result__summary--2-lines"}).text
        except:
            description = ""
        followers = listing.find("div", {"class": "entity-result__secondary-subtitle t-14 t-normal"}).text
        # Get the href from the element with the class = app-aware-link  scale-down 
        linkedin_url = listing.find("a", {"class": "app-aware-link"}).get('href')
        company = {
            "name": name.strip(),
            "location": location.strip(),
            "industry": industry.strip(),
            "description": description.strip(),
            "followers": followers.strip(),
            "linkedin_url": linkedin_url
        }
        companies.append(company)
    return companies


def read_in_html(path):
    soup = None
    with open(path, 'r') as f:
        soup = BeautifulSoup(f, "html.parser")
    return soup

def execute_for_keyword(keyword):
    df = pd.DataFrame()
    path = f'./{keyword}/'
    for file_name in os.listdir(path):
        if not file_name.endswith('.html'):
            continue
        file_path = path + file_name
        print(file_path)
        soup = read_in_html(file_path)
        companies = extract_valuable_fields_from_html(soup)
        indiv_df = pd.DataFrame(companies)
        print(indiv_df)
        df = pd.concat([df, indiv_df], ignore_index=True)
    # Save the df as pkl and csv to the path
    print(df)
    df.to_csv(f'./{keyword}/companies.csv', index=False)
    df.to_pickle(f'./{keyword}/companies.pkl')


def main():
    keywords = [
        "Bitcoin",
        "Crypto",
        "Smart Contract",
        "Web3",
        "NFT",
        "Blockchain"
    ]
    for keyword in keywords:
        execute_for_keyword(keyword)
    # CODE IS FLAWED!!
    # for keyword in keywords:
    #     df = pd.DataFrame()
    #     try:
    #         execute_for_keyword()
    #     except FileNotFoundError:
    #         print("Folder " + keyword + " not found")
    #         continue
        


if __name__ == '__main__':
    # main()
    print("Not executed.")
