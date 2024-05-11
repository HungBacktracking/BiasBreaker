from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

import threading
import schedule
import time
import NYTimes

def crawlNYTimes():
    NYTimes.crawl(driver[0], dataset, start_date, end_date)


def pushDataToDatabase(dataset):
    i = 1


# For scraping data
def CRAWL():
    # Run threads
    for i in range(NUMBER_OF_THREADS):
        t[i].start()
    # Wait until all threads finish
    for i in range(NUMBER_OF_THREADS):
        t[i].join()
    # Quit the drivers
    for i in range(NUMBER_OF_THREADS):
        driver[i].quit()

    

# Crawl and update all the database
def UPDATE():
    start = time.time()
    CRAWL()
    # pushDataToDatabase(dataset)
    end = time.time()   
    print("TOTAL TIME: ", end - start)




#-----------------------------MAIN PROGRAM-----------------------------------


NUMBER_OF_THREADS = 1
start_date = "10-05-2024"
end_date = "11-05-2024"

# Create threads
t = ['' for _ in range(NUMBER_OF_THREADS)]
t[0] = threading.Thread(target = crawlNYTimes)


# Path to your Chrome user profile
options = webdriver.ChromeOptions()
profile_path = r"C:\Users\DELLL\AppData\Local\Google\Chrome\User Data\Default"
options.add_argument(f"user-data-dir={profile_path}")
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')

driver = []
for i in range(NUMBER_OF_THREADS):
    driver.append(webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options))

dataset = set([])


#-----------------------------SCHEDULING-------------------------------------
schedule.every(1).day.do(UPDATE)
UPDATE()
while True:
    schedule.run_pending()
    time.sleep(1)