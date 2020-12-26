import requests
import bs4
from bs4 import BeautifulSoup

import pandas as pd
import time

URL = "https://www.indeed.com/jobs?q=data%20analyst&l=Omaha%2C%20NE&vjk=32a6ca0100d10ed7"

# request the URL
page = requests.get(URL)

soup = BeautifulSoup(page.text, "html.parser")

# print out the pretty html
#print(soup.prettify())

# Extract all job titles from the page
def extract_job_title_from_result(soup):
    jobs = []
    for h2 in soup.find_all(name="h2", attrs={"class":"title"}):
        for a in h2.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
            jobs.append(a["title"])
    return(jobs)
print("Jobs:")
print(extract_job_title_from_result(soup))

# Extract company name from the page
def extract_company_from_result(soup):
    companies = []
    for div in soup.find_all(name="div", attrs={"class":"sjcl"}):
        company = div.find_all(name="span", attrs={"class":"company"})
        for b in company:
            companies.append(b.text.strip())
    return(companies)
print("Companies:")
print(extract_company_from_result(soup))

# gets all locations but in wrong order
# TO-DO: add if/else so that it is added in the right order.
def extract_location_from_result(soup):
    locations = []
    for div in soup.find_all(name="div", attrs={"class":"location"}):
        locations.append(div.text)
    for span in soup.find_all(name="span", attrs={"class":"location"}):
        locations.append(span.text)
    return(locations)

print("Locations:")
print(extract_location_from_result(soup))
