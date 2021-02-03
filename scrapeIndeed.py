import requests
import bs4
from bs4 import BeautifulSoup

import pandas as pd
import time

# The URL can be adjusted to change the query for jobs

# If comparing in browser, make sure to clear cookies.
# URL = "https://www.indeed.com/q-data-analyst-l-Omaha,-NE-jobs.html"
URL = "https://www.indeed.com/jobs?q=receptionist&l=Omaha%2C+NE"

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
print(len(extract_job_title_from_result(soup)))
print(extract_job_title_from_result(soup))

# Extract company name from the page
def extract_company_from_result(soup):
    companies = []
    for div in soup.find_all(name="div", attrs={"class":"sjcl"}):
        company = div.find_all(name="span", attrs={"class":"company"})
        for b in company:
            companies.append(b.text.strip())
    return(companies)

# print("Companies:")
# print(len(extract_company_from_result(soup)))
# print(extract_company_from_result(soup))

# Extract location from the page
def extract_location_from_result(soup):
    locations = []
    for div in soup.find_all(name="div", attrs={"class":"sjcl"}):

        try:
            locations.append(div.find(name="div", attrs={"class":"location"}).text)
            #print("no exception")
        except Exception as e:
            #print(str(e))
            locations.append(div.find(name="span", attrs={"class":"location"}).text)
    return(locations)

# print("Locations:")
# print(len(extract_location_from_result(soup)))
# print(extract_location_from_result(soup))

# Extract salary from the page
def extract_salary_from_result(soup):
    salaries = []
    for div in soup.find_all(name="div", attrs={"class":"row"}):
        try:
            salaries.append(div.find(name="span", attrs={"class":"salaryText"}).text)
        except:
            salaries.append("NA")
    return(salaries)

# print("Salaries:")
# print(len(extract_salary_from_result(soup)))
# print(extract_salary_from_result(soup))

# Extract summary snippet from the page
# This is more complex:
#   'li' in a 'ul' under summary <div> tag
#   how to include multiple bullet points in single list value (String cat?)

def extract_summary_from_result(soup):
    summaries = []
    for div in soup.find_all("div", attrs={"class": "row"}):
        try:
            
        except Exception as e:
            print(str(e))
            #summaries.append("NA")
    return(summaries)

print("Summaries:")
print(len(extract_summary_from_result(soup)))
print(extract_summary_from_result(soup))