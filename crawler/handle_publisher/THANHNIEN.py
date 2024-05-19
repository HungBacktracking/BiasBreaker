from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from bs4 import BeautifulSoup
from random import randint
import requests
import time
from datetime import datetime


def get_info(soup_of_a_paper):
    try:
        text_ = soup_of_a_paper.find("h2", class_="detail-sapo").text.strip()
        text_ += "\n"
        text_body_elem = soup_of_a_paper.find("div", class_="detail-content afcbc-body")
        for child in text_body_elem.children:
            if child.name == "p" or child.name == "h2":
                text_ += child.text.strip()
                text_ += "\n"

        img = {}
        img_tag = text_body_elem.find("img")
        img_url = img_tag.get("data-original")
        img_des = img_tag.get("alt")
        img["url_link"] = img_url
        img["description"] = img_des
        meta_tag = soup_of_a_paper.find("meta", attrs={"name": "keywords"})
        keywords = meta_tag["content"].split(",")
        for i in range(len(keywords)):
            keywords[i] = keywords[i].strip()
        return text_, img, keywords
    except:
        return None


def crawl_article_by_date(start_date, end_date, links_elems, dataset):
    date1 = datetime.strptime(start_date, "%d-%m-%Y")
    date2 = datetime.strptime(end_date, "%d-%m-%Y")
    category_list = [
        "thế giới",
        "thể thao",
        "kinh doanh",
        "giải trí",
        "du lịch",
        "công nghệ",
        "chính trị",
    ]
    for elem in links_elems:
        try:
            info_link = elem.find(
                "a", class_="box-category-link-with-avatar img-resize"
            ).get("href")
            title = elem.find(
                "a", class_="box-category-link-with-avatar img-resize"
            ).get("title")
            category = (
                elem.find("a", class_="box-category-category").get("title").lower()
            )
            if (
                category in category_list
                or category == "kinh tế"
                or "bóng đá" in category
                or "du lịch" in category
                or "công nghệ" in category
            ):
                if category == "kinh tế":
                    category = "kinh doanh"
                if "bóng đá" in category:
                    category = "thể thao"
                if "du lịch" in category:
                    category = "du lịch"
                if "công nghệ" in category:
                    category = "công nghệ"
                if not info_link.startswith("https://thanhnien.vn"):
                    info_link = "https://thanhnien.vn" + info_link
                div_tag = elem.find("div", class_="box-time time-ago")
                date_time = div_tag["title"]
                # Extract the date part
                date = date_time.split(", ")[1].replace("/", "-")
                date_time = datetime.strptime(date, "%d-%m-%Y")
                if date_time > date1 or date_time < date2:
                    continue
                res = requests.get(info_link)
                soup_of_a_paper = BeautifulSoup(res.text, "html.parser")
                if get_info(soup_of_a_paper) is None:
                    continue
                else:
                    text, img, keywords = get_info(soup_of_a_paper)
                    data = {}
                    data["content"] = text
                    data["image"] = img
                    data["keywords"] = keywords
                    data["title"] = title
                    data["info_link"] = info_link
                    data["datetime"] = date_time
                    data["category"] = category
                    data["publisher_logo"] = (
                        "https://lh3.googleusercontent.com/1lUP5eLpU5Mo0hLUEhgegmjBU4IO1p-xmAB-IqtrjsGZx1Hyd6GfItHHwIBwCbdz0Ir-DEatWg=s0-h24-rw?fbclid=IwAR1ZIeiSIq_70dBPUtU818zKqYqpMruu9okYrmIPFF5j7miCIsASHvFnfKU"
                    )
                    data["publisher"] = "THANH NIEN"
                    dataset.append(data)

        except:
            print("continue")
            continue


def crawl(drvier, dataset, date1, date2):  # date1 > date2
    driver.get("https://thanhnien.vn/tin-moi.htm")
    time.sleep(10.1)
    SCROLL_PAUSE_TIME = 3.5
    last_height = driver.execute_script("return document.body.scrollHeight")
    for i in range(10):  # change this for deeper
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)

        try:
            button = driver.find_element(By.CSS_SELECTOR, "a.view-more.btn-viewmore")
            button.click()
            print("button clicked")
            s = randint(1, 2)
            time.sleep(s)
        except:
            print("no button")
    driver.implicitly_wait(2)
    src = driver.page_source
    soup = BeautifulSoup(src, "html.parser")
    links_elems = soup.find_all("div", class_="box-category-item")
    crawl_article_by_date(date1, date2, links_elems, dataset)


# uncomment for testing
# driver = webdriver.Chrome()
# dataset = []
# crawl(driver, dataset, "20-05-2024", "20-05-2024")


# print(len(dataset))
# print(dataset[0]["title"])
# print(dataset[0]["content"])
# print(dataset[0]["image"])
# print(dataset[0]["datetime"])
# print(dataset[0]["info_link"])
# print(dataset[0]["keywords"])
# print(dataset[0]["publisher"])
