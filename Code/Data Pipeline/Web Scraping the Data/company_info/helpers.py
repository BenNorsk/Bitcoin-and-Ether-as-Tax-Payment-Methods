import pandas as pd
import re
import os
from bs4 import BeautifulSoup 

def get_employees_link(soup):
    element = None
    employees_link = None
    # Find the element containing the text: "employees on LinkedIn"
    element = soup.find(lambda tag: tag.name == "span" and (("employees on LinkedIn" in tag.text) or ("employee on LinkedIn" in tag.text)))
    # employees_link = soup.find("a", {"class": "ember-view org-top-card-secondary-content__see-all-link"}).get("href").strip()
    # Find the span element which follows the pattern "\d* employees"
    if element is None:
        pattern = r"\d* employees"
        element = soup.find("span", text=re.compile(pattern))
    if element is not None:
        # Get the parent element
        parent = element.parent
        # Get the link element
        employees_link = parent.get("href")
    return employees_link

def get_employees_on_linkedin(soup):
    element = None
    employees_on_linkedin = 0
    # Find the element containing the text: "employees on LinkedIn"
    element = soup.find(lambda tag: tag.name == "span" and (("employees on LinkedIn" in tag.text) or ("employee on LinkedIn" in tag.text)))
    # employees_link = soup.find("a", {"class": "ember-view org-top-card-secondary-content__see-all-link"}).get("href").strip()
    # Find the span element which follows the pattern "\d* employees"
    if element is None:
        pattern = r"\d* employees"
        element = soup.find("span", text=re.compile(pattern))
    if element is not None:
        # Get the parent element
        parent = element.parent
        # Get the link element
        raw_employees_on_linkedin = parent.text.strip()
        # Get the number of employees
        employees_on_linkedin = int(re.findall(r"\d+", raw_employees_on_linkedin)[0])
    return employees_on_linkedin

def get_employees_total(soup):
    employees_total = None
    # Find the element containing exactly the text: "Industry"
    element = soup.find(lambda tag: tag.name == "dt" and ("Company size" in tag.text))
    # Find its sibling element which is a dd element and just below the dt element
    if element is not None:
        # Get the sibling element
        sibling = element.find_next_sibling("dd")
        # Get the link element
        employees_total = sibling.text.strip()
    return employees_total

def get_website_link(soup):
    website_link = None
    # Find the element containing the text: "Visit Website"
    element = soup.find(lambda tag: tag.name == "span" and ("visit website" in tag.text.lower() or "learn more" in tag.text.lower() or "register" in tag.text.lower() or "sign up" in tag.text.lower()))
    if element is not None:
        # Get the parent element
        parent = element.parent
        # Get the link element
        website_link = parent.get("href")
    if website_link is None:
        # Find the dt element equal to "Website"
        element = soup.find(lambda tag: tag.name == "dt" and (tag.text == "Website"))
        if element is not None:
            # Get the sibling element
            sibling = element.find_next_sibling("dd")
            # Get the link element
            son = sibling.find("a")
            website_link = son.get("href")
    return website_link

def get_industry(soup):
    industry = None
    # Find the element containing exactly the text: "Industry"
    element = soup.find(lambda tag: tag.name == "dt" and ("Industry" in tag.text))
    # Find its sibling element which is a dd element and just below the dt element
    if element is not None:
        # Get the sibling element
        sibling = element.find_next_sibling("dd")
        # Get the link element
        industry = sibling.text.strip()
    return industry

def get_followers(soup):
    followers = 0
    # Find the element whose text matches the pattern "/^\d{1,3}(,\d{3})* follower(s)?$"
    element = soup.find(lambda tag: tag.name == "div" and (tag.text.strip().endswith("followers") or tag.text.strip().endswith("follower")))
    if element is not None:
        raw_followers = element.text.strip()
        # Select only the digits from followers
        followers = int(''.join([i for i in raw_followers if i.isdigit()]))
    return followers

def get_long_description(soup):
    long_description = None
    # Find the element containing the text: "Overview"
    element = soup.find(lambda tag: tag.name == "h2" and ("Overview" in tag.text))
    # Find its sibling element which is a p element and just below the dt element
    if element is not None:
        # Get the sibling element
        sibling = element.find_next_sibling("p")
        # Get the link element
        if sibling is not None:
            long_description = sibling.text.strip()
    return long_description

def get_founded(soup):
    founded = None
    # Find the element containing the text: "Overview"
    element = soup.find(lambda tag: tag.name == "dt" and ("Founded" in tag.text))
    # Find its sibling element which is a p element and just below the dt element
    if element is not None:
        # Get the sibling element
        sibling = element.find_next_sibling("dd")
        # Get the link element
        if sibling is not None:
            founded = int(sibling.text.strip())
    return founded

def get_specialties(soup):
    specialties = None
    # Find the element containing the text: "Overview"
    element = soup.find(lambda tag: tag.name == "dt" and ("Specialties" in tag.text))
    # Find its sibling element which is a p element and just below the dt element
    if element is not None:
        # Get the sibling element
        sibling = element.find_next_sibling("dd")
        # Get the link element
        if sibling is not None:
            specialties = sibling.text.strip()
    return specialties