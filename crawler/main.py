from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

import threading
import schedule
import time
import NYTimes
import database
from constant import *


def crawlNYTimes():
    NYTimes.crawl(driver[0], dataset, start_date, end_date)


def pushDataToDatabase(dataset):
    database.insert_articles(dataset)


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
    pushDataToDatabase(dataset)
    end = time.time()   
    print("TOTAL TIME: ", end - start)




#-----------------------------MAIN PROGRAM-----------------------------------


# Create threads
t = ['' for _ in range(NUMBER_OF_THREADS)]
t[0] = threading.Thread(target = crawlNYTimes)


dataset = []
driver = []
for i in range(NUMBER_OF_THREADS):
    driver.append(webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options))

#-----------------------------SCHEDULING-------------------------------------
schedule.every(1).day.do(UPDATE)
UPDATE()
while True:
    schedule.run_pending()
    time.sleep(1)