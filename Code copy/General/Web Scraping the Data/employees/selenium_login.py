from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import random

# Log In to LinkedIn

def wait_2_seconds():
    # get a random number between 1 and 3
    wait_time = 0.8 + random.random()
    time.sleep(wait_time)
    return

def login(username, pw):
    driver = webdriver.Safari()
    driver.get("https://www.linkedin.com")
    element_user = driver.find_element("name", "session_key")
    element_user.send_keys(username)
    element_pw = driver.find_element("name","session_password")
    element_pw.send_keys(pw)
    # wait for 3 seconds
    wait_2_seconds()
    element_pw.submit()
    print("logged in")
    return driver

def main():
    driver = login()
    return driver


if __name__ == '__main__':
    main()


