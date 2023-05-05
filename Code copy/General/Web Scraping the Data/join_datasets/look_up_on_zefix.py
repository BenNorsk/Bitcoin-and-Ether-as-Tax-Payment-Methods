import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


def scrape_page(driver, name):
    url = "https://www.zefix.ch/de/search/entity/welcome"
    driver.get(url)
    driver.implicitly_wait((2 + random.random()))
    time.sleep((3 + random.random()))
    # Get the input field where formcontrolname="mainSearch" and id=mat-input-0
    input_field = driver.find_element("css selector", "input#mat-input-0")
    print(input_field)
    # Fill the input with the name of the company
    input_field.send_keys(name)
    # If suggestions appear, click on the first one
    time.sleep((2 + 0.5 * random.random()))
    try:
        suggestion = driver.find_element("css selector", "mat-option[role='option']:first-child")
        suggestion.click()
    except:
        pass
    # Wait for 2 seconds
    time.sleep((3 + random.random()))
    # Click on the search button of type="submit" and color="primary"
    search_button = driver.find_element("css selector", "button[type='submit']")
    print(search_button)
    search_button.click()
    # Wait for 2 seconds
    time.sleep((4 + random.random()))
    # Get the page source
    page_source = driver.page_source
    return page_source, driver

def main():
    df = pd.read_pickle('master+about+location.pkl')
    driver = webdriver.Safari()
    for index, row in df.iterrows():
        name = row['name']
        id = row['id']
        if id > 1004:
            page, driver = scrape_page(driver, name)
            with open(f'looked_up_companies/{id}_{name}.html', 'w') as f:
                    f.write(page)
                    print(f'Finished with company {name} with id {id}.')
            time.sleep((1 + random.random()))
    driver.quit()

if __name__ == "__main__":
    main()

