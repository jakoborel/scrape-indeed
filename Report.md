# Final Report

## Purpose
I wanted to provide a tool to see what type of jobs are out in the world. Lots of individuals entering the job market may have an idea of what type of job they would like, but may not know what the average salary of these positions may be. They may also be interested in seeing what locations in the country provide the best opportunities. They may also be interested in seeing the top qualifications or requirements for the majority of these jobs to see what skills they should acquire. They can easily search online job postings to look for and apply to individual jobs, but they may be interested in seeing overall statistics of the job market. 

## Goals
There were three main goals in this project. 

### Web Scraping
I wanted to use Python to scrape data from the internet in order to collect real and usable data that is relevant. This is a great learning experience and several programming techniques were used to loop through the URL's and get data.

### Data Analysis
I wanted to use the Pandas library in Python to further analyze the job data for useful statistics and visualizations that can provide quick and powerful information to the user.

### Web Application
I wanted to create an application that would allow a user to enter certain criteria and then scrape, clean, and analyze the data on the fly. 

## Accomplishments
This project used many new tools and libraries that I did not have experience with prior. The majority of the project was spent on scraping the data using BeautifulSoup and Selenium. These were interesting to work with. Selenium works as a web driver itself and it took some work to get setup and functioning properly. I also learned how different parts of a URL work to identify the target I was looking for. I have some previous knowledge of R, but using Pandas was a nice touch as well. It was also nice to learn to work with matplotlib for visualizations. I was also surprised to find a library named Spyre that could be used to create Python web apps very similar to R Shiny apps. This made the application creation relatively straightforward. Throughout the project, I also utilized Git for version control. In order to see if my project was useful, I created a prototype of what they application may look like in order to show current students at my college campus. They were then able to provide feedback on the design of the app and what would be useful to an individual who is searching for a job.

## Challenges
I faced many challenges in this project. There are 2 examples that were prominent. I wanted to collect data on the qualifications of a job, but they are embedded in the card details of each job posting. Each job post had to be clicked on to get more data. This took some time to figure out how to loop through the different urls for each job. This data was contained in an iframe. I found that the iframe element had to be read in a separate request. After much work, I still was not able to get the data. I eventually found out that the requests library that I was using does not support Javascript and the data was not being pulled out in the HTML. To work around this, I decided to use Selenium as it supports Javascript just like a web browser. The downside was that Selenium is very slow and the time to scrape all the data increased. Another challenge I faced was getting past the captcha on Indeed. After some time of working, I began getting a Captcha code on any URL that I would enter for Indeed. This completely prevented me from scraping job postings off the website. I could not workaround this because they were intentionally blocking me from scraping or using Selenium to navigate the website. This is because they want to prevent fake job applications. 

## Future Work
After several challenges, there is likely little work to be done further. I was hoping to be able to be able to do more work with visualizations and data analysis, but the Captcha code prevents gathering the data. I have learned many new techniques and have practiced several new concepts throughout this project. I would like to see about using Indeed's API in order to get more reliable data without scraping. This would likely be faster as well. This form of data collection would then allow further data analysis. 