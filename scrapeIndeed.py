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

def extract_job_title_from_result(soup):
  jobs = []
  for h2 in soup.find_all(name="h2", attrs={"class":"title"}):
      for a in h2.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
          jobs.append(a["title"])
  return(jobs)

print(extract_job_title_from_result(soup))