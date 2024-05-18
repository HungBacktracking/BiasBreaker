from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

import threading
import schedule
import time
import datetime
import NYTimes
import USATODAY
import VNEXPRESS
import TuoiTre
import database
from constant import *
from model.model import TextSummarizer, Predictor, KeywordExtractor

def crawlNYTimes():
    NYTimes.crawl(driver[0], dataset, start_date, end_date)

def crawUSAToday():
    USATODAY.crawl(dataset, start_date, end_date)

def crawlVNExpress():
    VNEXPRESS.crawl(dataset, start_date, end_date)

def crawlTuoiTre():
    TuoiTre.crawl(driver[0], dataset, start_date, end_date)

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

def pushKeywordsToDatabase():
    """_summary_
    """
    # Query articles from database with datetime = today
    articles = database.get_articles_by_date(datetime.datetime.now().date().strftime('%d-%m-%Y'))
    # Get the text from the articles
    texts = [article['content'] for article in articles]
    # Get the keywords from the text
    kw_extractor = KeywordExtractor()
    keywords = kw_extractor.extract_keywords(texts)
    # Match each keyword with the article
    for i, article in enumerate(articles):
        article['keywords'] = keywords[i]
    data = [{'_id': article['_id'], 'keywords': article['keywords']} for article in articles]
    # Push data to database
    database.insert_keywords(data)
    
    

# Crawl and update all the database
def UPDATE():
    start = time.time()
    CRAWL()
    pushDataToDatabase(dataset)
    # pushKeywordsToDatabase()
    end = time.time()   
    print("TOTAL TIME: ", end - start)




#-----------------------------MAIN PROGRAM-----------------------------------


# Create threads
t = ['' for _ in range(NUMBER_OF_THREADS)]
t[0] = threading.Thread(target = crawlTuoiTre)
t[1] = threading.Thread(target = crawlVNExpress)


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