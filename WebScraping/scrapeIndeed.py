import requests
import bs4
from bs4 import BeautifulSoup

import pandas as pd
import time

# If comparing in browser, make sure to clear cookies.
# URL = "https://www.indeed.com/jobs?q=receptionist&l=Omaha%2C+NE"

# request the URL
# page = requests.get(URL)

# soup = BeautifulSoup(page.text, "html.parser")

# Extract all job titles from the page
def extract_job_title_from_result(soup):
    jobs = []
    for h2 in soup.find_all(name="h2", attrs={"class":"title"}):
        for a in h2.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
            jobs.append(a["title"])
    return(jobs)


# Extract company name from the page
def extract_company_from_result(soup):
    companies = []
    for div in soup.find_all(name="div", attrs={"class":"sjcl"}):
        company = div.find_all(name="span", attrs={"class":"company"})
        for b in company:
            companies.append(b.text.strip())
    return(companies)


# Extract location from the page
def extract_location_from_result(soup):
    locations = []
    for div in soup.find_all(name="div", attrs={"class":"sjcl"}):
        try:
            locations.append(div.find(name="div", attrs={"class":"location"}).text)
        except Exception as e:
            locations.append(div.find(name="span", attrs={"class":"location"}).text)
    return(locations)


# Extract salary from the page
def extract_salary_from_result(soup):
    salaries = []
    for div in soup.find_all(name="div", attrs={"class":"row"}):
        try:
            salaries.append(div.find(name="span", attrs={"class":"salaryText"}).text)
        except:
            salaries.append("NA")
    return(salaries)


# Extract summary bullet points from page
def extract_summary_from_result(soup):
    summaries = []
    i=0
    for div in soup.find_all("div", attrs={"class": "row"}):
        for summary in div.find_all("div", attrs={"class":"summary"}):
            for li in summary.find_all("li"):
                if (len(summaries)<=i):
                    summaries.append(str(li.text))
                elif(len(summaries)>i):
                    summaries[i] = summaries[i] + " " + str(li.text)
        i+=1
    return(summaries)


# Build url with a search query and optional arguments for location, salary, and page start filters
def build_url(query, location="", salary="", start=""):
    return "http://www.indeed.com/jobs?q=" + "+".join(str(query).split()) + "+" + str(salary) + "&l=" + str(location)


# Build pandas DataFrame that contains the job post information.
def build_df(url):
    job_titles = []
    companies = []
    locations = []
    salaries = []
    summaries = []
    # Loop through first 5 pages of job postings and add data
    for start in range(0, 50, 10):
        if (start==0):
            url = url + "&start="
        elif (start==10):
            url = url + "10"
        else:
            url = url[:-2] + str(start)

        page = requests.get(url)
        time.sleep(1)
        soup = BeautifulSoup(page.text, "html.parser")
        job_titles.extend(extract_job_title_from_result(soup))
        companies.extend(extract_company_from_result(soup))
        locations.extend(extract_location_from_result(soup))
        salaries.extend(extract_salary_from_result(soup))
        summaries.extend(extract_summary_from_result(soup))

        # Check if next button exists, if not break out of next page loop.
        next_button = soup.find("a", attrs={"aria-label": "Next"})
        if next_button is None:
            break

    # dictionary of lists for column names
    columns = {'title' : job_titles, 'company' : companies, 'location' : locations, 'salary' : salaries, 'summary' : summaries}
    return pd.DataFrame(columns)


# max_results_per_city = 100
# city_set = ['New+York','Chicago','San+Francisco', 'Austin', 'Seattle', 'Los+Angeles', 'Philadelphia', 'Atlanta', 'Dallas', 'Pittsburgh', 'Portland', 'Phoenix', 'Denver', 'Houston', 'Miami', 'Washington+DC', 'Boulder']
# columns = ["city", "job_title", "company_name", "location", "summary", "salary"]
# sample_df = pd.DataFrame(columns = columns)
#scraping code:
# for city in city_set:
#     for start in range(0, max_results_per_city, 10):
#         page = requests.get('http://www.indeed.com/jobs?q=data+scientist+%2420%2C000&l=' + str(city) + '&start=' + str(start))
#         time.sleep(1)  #ensuring at least 1 second between page grabs
#         soup = BeautifulSoup(page.text, "lxml", from_encoding="utf-8")
#         #specifying row num for index of job posting in dataframe
#         num = (len(sample_df) + 1) 
#         #creating an empty list to hold the data for each posting
#         job_post = [] 
#         #append city name
#         job_post.append(city) 
#         extract each 
#         #appending list of job post info to dataframe at index num
#         sample_df.loc[num] = job_post