import pandas as pd
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium_login import login
import time
import random

df = pd.read_pickle('master.pkl')
username = 'hanslublich@gmx.ch'
pw = 'hjbihhbJHHb23983'
driver = login(username, pw)
time.sleep((6 + random.random()))

about_urls = []
# iterate through the rows of the df

for index, row in df.iterrows():
    if index > 1004:
        # get the url
        url = row['linkedin_url']
        # Name
        name = row['name']
        # add about to the url
        about_url = url + 'about/'
        # Get the page
        driver.get(about_url)
        driver.implicitly_wait((5 + random.random()))
        time.sleep((2 + random.random()))
        # wait for 3 seconds
        time.sleep((2 + random.random()))
        # Get the page source
        page_source = driver.page_source
        # Save the page as an html file
        with open(f'companies/{index}_{name}.html', 'w') as f:
            f.write(page_source)

