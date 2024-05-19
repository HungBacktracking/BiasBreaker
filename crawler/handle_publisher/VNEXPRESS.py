import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, timezone

category_id = {
    "world": "1001002",
    "business": "1003159",
    "polictics": "1001005",
    "sport": "1002565",
    "technology": "1002592",
    "entertainment": "1002691",
    "travel": "1003231",
}


def get_category_from_id(url):
    category_id = {
        "thế giới": "1001002",
        "kinh doanh": "1003159",
        "chính trị": "1001005",
        "thể thao": "1002565",
        "công nghệ": "1002592",
        "giải trí": "1002691",
        "du lịch": "1003231",
    }
    for category, id in category_id.items():
        if id in url:
            return category
    return None


def convert_to_00_UNIX(date):  # convert to UNIX in vetname timezone
    tz_vn = timezone(timedelta(hours=7))
    dt = datetime.strptime(date, "%d-%m-%Y").replace(tzinfo=tz_vn)
    unix_time = dt.timestamp()
    return int(unix_time)


def get_title(soup_of_a_paper):
    title_element = soup_of_a_paper.find("h1", class_="title-detail")
    if title_element:
        try:
            title = title_element.text
            return title
        except:
            return None


def get_content(soup_of_a_paper):
    elems_content = soup_of_a_paper.find_all("p", class_=["description", "Normal"])
    content = ""
    for elem in elems_content:
        try:
            text = elem.text
            content += text
            content += "\n"
        except:
            return None
    return content


def get_image(soup_of_a_paper):
    img_dict = {}
    all_img_tags = soup_of_a_paper.find_all("img", itemprop="contentUrl")
    for elem_image in all_img_tags:
        url_img = elem_image.get("data-src")
        des_img = elem_image.get("alt")
        if url_img and des_img:
            img_dict["url_link"] = url_img
            img_dict["description"] = des_img
            return img_dict
    return None


def get_key_words(soup_of_a_paper):
    elem = soup_of_a_paper.find("meta", attrs={"name": "keywords"})
    try:
        keywords = elem["content"].split(",")
        return keywords
    except:
        return None


def get_info(url_to_paper):
    article = {}
    res = requests.get(url_to_paper)
    soup_of_a_paper = BeautifulSoup(res.text, "html.parser")
    title = get_title(soup_of_a_paper)
    content = get_content(soup_of_a_paper)
    image = get_image(soup_of_a_paper)
    keywords = get_key_words(soup_of_a_paper)
    if title and content and image and keywords:
        article["publisher"] = "VN Express"
        article["title"] = title
        article["info_link"] = url_to_paper
        article["content"] = content
        article["image"] = image
        article["keywords"] = keywords
        return article
    return None


def processing(
    url,
):  # url to list of paper base on date, return list of article of a date
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    category = get_category_from_id(url)
    article_data = []
    if category == "polictics":
        elements = soup.find_all("article", class_="item-news item-news-common")
        for elem in elements:
            url_to_paper = ""
            h3_tag = elem.find("h3", class_="title-news")
            if h3_tag is not None:
                a_tag = h3_tag.find("a")
                if a_tag is not None:
                    url_to_paper = a_tag.get("href")

            if url_to_paper:
                check_politics_element = elem.find("p", class_="meta-news")
                if check_politics_element:
                    is_politics_element = check_politics_element.find("a", class_="cat")
                    if is_politics_element:
                        type = is_politics_element.get("title")
                        if type == "Chính trị":  # Ensure exact match
                            article = get_info(url_to_paper)
                            if article:
                                article["category"] = category
                                article_data.append(article)
    else:
        elements = soup.find_all("article", class_="item-news item-news-common")
        for elem in elements:
            url_to_paper = ""
            h3_tag = elem.find("h3", class_="title-news")
            if h3_tag is not None:
                a_tag = h3_tag.find("a")
                if a_tag is not None:
                    url_to_paper = a_tag.get("href")

            if url_to_paper:
                article = get_info(url_to_paper)
                if article:
                    article["category"] = category
                    article_data.append(article)
    return article_data


def crawl(datas, start_date, end_date):  # crawl from start date to end date
    start = datetime.strptime(start_date, "%d-%m-%Y")
    end = datetime.strptime(end_date, "%d-%m-%Y")
    current = start

    # Loop through each date from start to end

    while current <= end:

        UNIX_current = convert_to_00_UNIX(
            f"{current.day:02}-{current.month:02}-{current.year}"
        )

        for category, id in category_id.items():

            url = f"https://vnexpress.net/category/day/cateid/{id}/fromdate/{UNIX_current}/todate/{UNIX_current}"
            articles = processing(url)
            for article in articles:
                if article:
                    article["datetime"] = (
                        f"{current.day:02}-{current.month:02}-{current.year}"
                    )
                    datas.append(article)

        current += timedelta(days=1)


# uncomment for testing
# dataset = []
# crawl(dataset, "17-05-2024", "18-05-2024")
# print(len(dataset))
# print(dataset[0]["title"])
# print(dataset[0]["content"])
# print(dataset[0]["image"])
# print(dataset[0]["datetime"])
# print(dataset[0]["keywords"])
# print(dataset[0]["publisher"])
