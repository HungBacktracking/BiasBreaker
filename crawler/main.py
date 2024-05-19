from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

import threading
import schedule
import time
import datetime
from handle_publisher import NYTimes, USATODAY, VNEXPRESS, TuoiTre, THANHNIEN
import database
from constant import *
from model.model import TextSummarizer, Predictor, KeywordExtractor
from LLM_Processing import Keyword, Summary, Predict

def crawlNYTimes():
    NYTimes.crawl(driver[0], dataset, start_date, end_date)

def crawUSAToday():
    USATODAY.crawl(dataset, start_date, end_date)

def crawlVNExpress():
    VNEXPRESS.crawl(dataset, start_date, end_date)

def crawlTuoiTre():
    TuoiTre.crawl(driver[0], dataset, start_date, end_date)

def crawlThanhNien():
    THANHNIEN.crawl(driver[1], dataset, start_date, end_date)

def insert_keywords(dataset):
    Keyword.insert_keywords(dataset)

def insert_summaries(dataset):
    Summary.insert_summaries(dataset)

def insert_predict(dataset):
    Predict.insert_predict(dataset)

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
    insert_summaries(dataset)
    insert_predict(dataset)
    pushDataToDatabase(dataset)
    end = time.time()   
    print("TOTAL TIME: ", end - start)




#-----------------------------MAIN PROGRAM-----------------------------------


# Create threads
t = ['' for _ in range(NUMBER_OF_THREADS)]
t[0] = threading.Thread(target = crawlTuoiTre)
t[1] = threading.Thread(target = crawlVNExpress)
t[2] = threading.Thread(target = crawlThanhNien)


dataset = []
driver = []
for i in range(NUMBER_OF_THREADS):
    driver.append(webdriver.Chrome(service=Service(ChromeDriverManager().install())))

#-----------------------------SCHEDULING-------------------------------------
schedule.every(1).day.do(UPDATE)
UPDATE()
while True:
    schedule.run_pending()
    time.sleep(1)