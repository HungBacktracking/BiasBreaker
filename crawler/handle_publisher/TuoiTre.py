from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
from random import randint
from datetime import datetime, timedelta
import time

category_list = ["thế giới", "thể thao", "kinh doanh", "giải trí", "du lịch", "công nghệ", "chính trị"]

def crawl(driver, articles, start_date, end_date): # Tuoi Tre dont have a way to get articles by date 
    time_begin = time.time()
    prev_len = len(articles)

    # Parse the start and end date strings into datetime objects
    start = datetime.strptime(start_date, "%d-%m-%Y")
    end = datetime.strptime(end_date, "%d-%m-%Y")
    
    url = "https://tuoitre.vn/tin-moi-nhat.htm"
    processing(driver, articles, url, start)

    time_end = time.time()
    print("{} {}. {}".format("TuoiTre", len(articles) - prev_len, type, time_end - time_begin))

def processing(driver, articles, url, start_date):
    # Get the web page
    driver.get(url)

    time.sleep(2.1)
    SCROLL_PAUSE_TIME = 3.5
    last_height = driver.execute_script("return document.body.scrollHeight")
    for i in range(20):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        
        try:
            button = driver.find_element(By.CSS_SELECTOR, "a.view-more")
            button.click()
            s = randint(1, 2)
            time.sleep(s)
        except:
            break
    driver.implicitly_wait(2)

    # page_source is a variable created by Selenium - it holds all the HTML
    src = driver.page_source
    soup = BeautifulSoup(src, "html.parser")
    tiles = soup.select(".box-category-item")

    for tile in tiles:
        title = tile.find('h3').get_text().strip()
        info_link = "https://tuoitre.vn" + tile.find('h3').find('a').get("href")
    
        driver.get(info_link)
        src_detail = driver.page_source
        soup = BeautifulSoup(src_detail, "html.parser")

        try:
            img_link = soup.select_one("img.lightbox-content").get("src")
            image_caption = soup.select_one(".PhotoCMS_Caption p").get_text().strip()
            paragraphs = soup.select(".detail-content.afcbc-body > p")
            date = soup.select_one("div.detail-time div").get_text().strip().split(" ")[0].replace("/", "-")
            category = soup.select_one(".detail-cate a").get_text().strip()

            content = ""
            for paragraph in paragraphs:
                content += paragraph.get_text().strip() + "\n\n"
        except:
            driver.implicitly_wait(2) 
        if len(content) < 215 or category.lower() not in category_list:
            continue
        current = datetime.strptime(date, "%d-%m-%Y")
        if current < start_date:
            break
        
        article = {
                    "publisher": "Tuổi trẻ",
                    "title": title, 
                    "info_link": info_link, 
                    "image": {
                        "url_link": img_link,
                        "description": image_caption
                    },
                    "category": category.lower(),
                    "content": content,
                    "datetime": date,
        }
        articles.append(article)
