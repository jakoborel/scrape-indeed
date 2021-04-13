import requests
from bs4 import BeautifulSoup
import html5lib
import dryscrape
from selenium import webdriver
from selenium.webdriver.common.by import By

import pandas as pd
import time

# There is no #vjs-container div tag. It is not pulling it in between the jobsearch rows.

# Extract qualifications for extended job details pane
def extract_qualifications_from_result(url):
    qualifications = []
    url = url + "&vjk="
    s = requests.Session()
    page = s.get(url)
    time.sleep(1)
    soup = BeautifulSoup(page.text, "html.parser")
    i=0
    rows = soup.find_all(name="div", attrs={"class":"row"})
    url_extensions = []
    for row in rows:
        url_extensions.append(row["data-jk"])


    for url_extension in url_extensions:
        url = url + str(url_extension)
        print(url)
        page = s.get(url)
        time.sleep(1)
        soup = BeautifulSoup(page.text, "html.parser")

        try:
            # The body has nothing in it but it should have the body of the clicked card???
            # body = soup.find_all(name="iframe", attrs={"id":"vjs-container-iframe"})
            # print(len(body))
            # for li in body[i].find_all(name="li", attrs={"class":"icl-u-xs-p--none jobsearch-ReqAndQualSection-item"}):

            # iframe has to be loaded in separate request. 
            # Not finding iframe???
            # or iframe in soup.find_all(name="iframe", attrs={"id":"vjs-container-iframe"}):
            for div in soup.find("div", {"id":"vjs-container"}):
                iframe_url = div.find("iframe").attrs['src']
                iframe_page = s.get(iframe_url)
                time.sleep(1)
                soup = BeautifulSoup(iframe_page.text, "html.parser")
                print("test")
            # for li in soup.find_all(name="li", attrs={"class":"jobsearch-ReqAndQualSection-item"}):
            #     if (len(qualifications)<=i):
            #         qualifications.append(str(li.find(name="p").text))
            #     elif(len(qualifications)>i):
            #         qualifications[i] = qualifications[i] + " " + str(li.find(name="p").text)
            #     print("test2")


                # for p in li.find_all(name="p", attrs={"class":"icl-u-xs-my--none"}):
                #     print(p.text)
                #     print("Hello?")


                # Qualifications HTML

                # <ul class="jobsearch-ReqAndQualSection-item--wrapper" style="padding: 0px;">
                # <li class="icl-u-xs-block jobsearch-ReqAndQualSection-item--title">
                # <span class="icl-u-textBold"></span>
                # <ul class="icl-u-xs-my--none jobsearch-ReqAndQualSection-item--closedBullets">
                # <li class="icl-u-xs-p--none jobsearch-ReqAndQualSection-item"><p class="icl-u-xs-my--none">Bachelor's (Preferred)</p></li>
                # <li class="icl-u-xs-p--none jobsearch-ReqAndQualSection-item"><p class="icl-u-xs-my--none">Laboratory Experience: 4 years (Preferred)</p></li>
                # </ul>
                # </li></ul>
                
                #print(li.find(name="p", attrs={"class":"icl-u-xs-my--none"}).text)
               # print(li.text)
                # if (len(qualifications)<=i):
                #     qualifications.append(str(li.text))
                # elif(len(qualifications)>i):
                #     qualifications[i] = qualifications[i] + " " + str(li.text)
        except Exception as e:
            print(e)
            qualifications.append("NA")

        i+=1
        url = url[:-16]

    return(qualifications)


def parseTesting(url):
    # qualifications = []
    # url = url + "&vjk="
    s = requests.Session()
    # page = s.get(url)
    # time.sleep(1)
    # soup = BeautifulSoup(page.text, "html.parser")
    # i=0
    # rows = soup.find_all(name="div", attrs={"class":"row"})
    # url_extensions = []
    # for row in rows:
    #     url_extensions.append(row["data-jk"])


    
    # url = url + str(url_extensions[0])
    # print(url)
    page = s.get(url)
    time.sleep(1)
    soup = BeautifulSoup(page.text, "html.parser")
    print(soup)


# Cant install dryscrape correctly. 
def parseTesting2(url):
    qualifications = []
    url = url + "&vjk="
    session = dryscrape.Session()
    session.visit(url)
    response = session.body()
    time.sleep(1)
    soup = BeautifulSoup(page.text, "html.parser")
    print(soup.prettify())

# test to see if it can be done in selenium as it supports JS
def seleniumTesting(url):
    qualifications = []
    url = url + "&vjk="
    s = requests.Session()
    page = s.get(url)
    time.sleep(1)
    soup = BeautifulSoup(page.text, "html.parser")
    # Use bs4 to find all the urls extensions to loop through
    rows = soup.find_all(name="div", attrs={"class":"row"})
    url_extensions = []
    for row in rows:
        url_extensions.append(row["data-jk"])

    # Set up selenium driver to use for JS section
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    for url_extension in url_extensions:
        url = url + str(url_extension)
        driver.get(url)

        try:  
            qualSection = driver.find_element_by_class_name("jobsearch-ReqAndQualSection-item--wrapper")
            qualifications.append(qualSection.text)
        except Exception as e:
            qualifications.append("NA")

        # Reset url
        url = url[:-16]

    driver.quit()
    print(len(qualifications))
    return(qualifications)



url = "https://www.indeed.com/jobs?q=receptionist&l=Omaha%2C+NE"
#print(extract_qualifications_from_result(url))
# parseTesting(url)
# parseTesting2(url)
print(seleniumTesting(url))