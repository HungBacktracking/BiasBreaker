from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
from random import randint
from datetime import datetime, timedelta
import time

from config import *

def crawl(driver, articles, start_date, end_date):
    time_begin = time.time()
    prev_len = len(articles)

    # Parse the start and end date strings into datetime objects
    start = datetime.strptime(start_date, "%d-%m-%Y")
    end = datetime.strptime(end_date, "%d-%m-%Y")
    
    # Initialize the current date to the start date
    current = start
    
    # Loop through each date from start to end
    while current <= end:
        url = f"https://www.nytimes.com/sitemap/{current.year}/{current.month:02}/{current.day:02}/"
        processing(driver, articles, url)

        current += timedelta(days = 1)

    time_end = time.time()
    print("{} {}. {}".format("NYTimes", len(articles) - prev_len, type, time_end - time_begin))

def processing(driver, articles, url):
    # Get the web page
    driver.get(url)

    # page_source is a variable created by Selenium - it holds all the HTML
    src = driver.page_source
    soup = BeautifulSoup(src, "html.parser")
    tiles = soup.select(".css-ach7ou > .css-cmbicj > li > a")

    # Login to NYTimes
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".css-ni9it0").click()
    time.sleep(3.5)
    driver.find_element(By.ID, "email").send_keys(f"{email}")
    time.sleep(2.3)
    driver.find_element(By.CSS_SELECTOR, ".css-1i3jzoq-buttonBox-buttonBox-primaryButton-primaryButton-Button").click()
    time.sleep(2.3)
    driver.find_element(By.ID, "password").send_keys(f"{password}")
    time.sleep(2.3)
    driver.find_element(By.CSS_SELECTOR, ".css-1i3jzoq-buttonBox-buttonBox-primaryButton-primaryButton-Button").click()


    time.sleep(4.1)
    SCROLL_PAUSE_TIME = 1.5
    last_height = driver.execute_script("return document.body.scrollHeight")
    for i in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    driver.implicitly_wait(2)

    for tile in tiles:
        title = tile.get_text().strip()
        info_link = tile.get("href")
    
        
        driver.get(info_link)
        # src_detail = driver.page_source
        # soup = BeautifulSoup(src_detail, "html.parser")

        last_height = driver.execute_script("return document.body.scrollHeight")
        for i in range(1):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(SCROLL_PAUSE_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        src_detail = driver.page_source
        soup = BeautifulSoup(src_detail, "html.parser")

        try:
            img_link = soup.select_one("picture > img").get("src")
            paragraphs = soup.select(".StoryBodyCompanionColumn .css-at9mc1")

            content = ""
            for paragraph in paragraphs:
                content += paragraph.get_text().strip() + "\n"
        except:
            driver.implicitly_wait(2) 
        
        article = {
                    "title": title, 
                    "info_link": info_link, 
                    "img_link": img_link, 
                    "content": content
        }

        print()
        print(article)


        article_tmp = tuple(article.values())
        articles.add(article_tmp)
