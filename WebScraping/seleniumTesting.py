from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.indeed.com/q-receptionist-l-Omaha,-NE-jobs.html')

# Navigates through the first 5 pages of job postings
for i in range(4):
	try:
	    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@aria-label='Next']")))
	    element.click()
	    print("Navigating to Next Page")
	except Exception as e:
		print("Exception thrown: ", e)
		driver.quit()
