import pandas as pd
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium_login import login
import time
import random


def start_driver():
    username = 'hanslublich@gmx.ch'
    pw = 'hjbihhbJHHb23983'
    driver = login(username, pw)
    time.sleep((6 + random.random()))
    return driver

def scrape_page(driver, url):
    driver.get(url)
    driver.implicitly_wait((5 + random.random()))
    time.sleep((10 + random.random()))
    # wait for 3 seconds
    time.sleep((7 + random.random()))
    # Get the page source
    page_source = driver.page_source
    return page_source, driver

def main():
    df = pd.read_pickle('master+about+location.pkl')
    # login to linkedin
    driver = start_driver()
    for index, row in df.iterrows():
        if (row['employees_link'] is None) or index < 914:
            continue
        url = "https://linkedin.com" + row['employees_link']
        name = row['name']
        employees_on_linkedin = row['employees_on_linkedin']
        # If there are less than 10 but more than 0 employees, we can just scrape the page
        if (employees_on_linkedin > 0) and (employees_on_linkedin <= 10):
            page, driver = scrape_page(driver, url)
            # save the page as an html file
            with open(f'employee_lists/{index}_1_{name}.html', 'w') as f:
                f.write(page)
                print(f'Finished with company {name} at index {index}.')
        # If there are more than 10 employees, we need to iterate through the pages
        elif (employees_on_linkedin > 10):
            amount_of_pages = (employees_on_linkedin // 10) + 1
            for j in range(1, amount_of_pages + 1):
                # Add "&page={j}" to the url
                url = "https://linkedin.com" + row['employees_link'] + f'?page={j}'
                page, driver = scrape_page(driver, url)
                # save the page as an html file
                with open(f'employee_lists/{index}_{j}_{name}.html', 'w') as f:
                    f.write(page)
                    print(f'Finished with company {name} at index {index} and page {j}.')
            time.sleep((1 + random.random()))
        time.sleep((1 + random.random()))
        # Show progress in percentage
        print(f'Finished with company {name} at index {index}.')


if __name__ == "__main__":
    main()

