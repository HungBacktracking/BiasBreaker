import requests
from bs4 import BeautifulSoup
import validators
from datetime import datetime


def get_title(soup_of_a_paper):
    elem_title = soup_of_a_paper.find("h1", class_="gnt_ar_hl")
    title = ""
    if elem_title is not None:
        title = elem_title.text
        return title
    return None


def get_category(url):
    if "/nation/" in url:
        return "world"
    if "/politics/" in url:
        return "politics"
    if "/sports/" in url:
        return "sports"
    if "/tech/" in url:
        return "techonology"
    if "/entertainment/" in url:
        return "entertainment"
    if "/money/" in url:
        return "business"
    if "/travel/" in url:
        return "travel"
    return None


def get_text(soup_of_a_paper):
    elem_text = soup_of_a_paper.find("div", class_="gnt_ar_b")
    text = ""
    if elem_text is not None:
        for child in elem_text.children:
            if (child.name == "p" and "gnt_ar_b_p" in child.get("class", [])) or (
                child.name == "h2" and "gnt_ar_b_h2" in child.get("class", [])
            ):
                text += child.text.strip()
                text += "\n"
    return text


def get_image(soup_of_a_paper):
    elems = soup_of_a_paper.find_all("img", class_="gnt_em_img_i")
    for elem in elems:
        img_src = elem.get("data-gl-src")
        img_des = elem.get("alt")
        if img_src is not None and img_des is not None:
            img_src = "https://www.usatoday.com" + img_src
            image = {"url_link": img_src, "description": img_des}
            return image
    return None


def numeric_to_month(numeric_month):
    months = {
        1: "january",
        2: "february",
        3: "march",
        4: "april",
        5: "may",
        6: "june",
        7: "july",
        8: "august",
        9: "september",
        10: "october",
        11: "november",
        12: "december",
    }

    return months.get(numeric_month)


def processing(url):
    data = []
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    elems_link = soup.find_all("li", class_="sitemap-list-item")
    for elem in elems_link:
        elem_link = elem.find("a")
        if elem is not None:
            try:
                link_to_a_paper = elem_link.get("href")
                try:
                    if (
                        not validators.url(link_to_a_paper)
                        or "/video/" in link_to_a_paper
                        or "/life/" in link_to_a_paper
                        or "/opinion/" in link_to_a_paper
                        or "/reviewed.usatoday.com/" in link_to_a_paper
                    ):  # Optional URL validation
                        print(f"{link_to_a_paper} is not a valid URL. Skipping...")
                        continue  # Move to the next iteration
                    res = requests.get(link_to_a_paper)
                    soup_of_a_paper = BeautifulSoup(res.text, "html.parser")
                    title = get_title(soup_of_a_paper)
                    text = get_text(soup_of_a_paper)
                    image = get_image(soup_of_a_paper)
                    category = get_category(link_to_a_paper)
                    if category is None or image is None:
                        continue

                    data_dict = {
                        "publisher": "USA Today",
                        "title": title,
                        "info_link": link_to_a_paper,
                        "content": text,
                        "image": image,
                        "category": category,
                        "datetime": "",
                    }
                    data.append(data_dict)

                except requests.exceptions.InvalidURL as e:
                    print(f"Invalid URL: {link_to_a_paper} ({e})")
                except requests.exceptions.RequestException as e:
                    print(f"Error fetching {link_to_a_paper}: {e}")
            except Exception as e:
                print("An error occurred:", e)
    return data


from datetime import datetime, timedelta
import time


def crawl(datas_, start_date, end_date):
    start = datetime.strptime(start_date, "%d-%m-%Y")
    end = datetime.strptime(end_date, "%d-%m-%Y")
    # Initialize the current date to the start date
    current = start
    # Loop through each date from start to end
    while current <= end:
        url = f"https://www.usatoday.com/sitemap/{current.year}/{numeric_to_month(current.month)}/{current.day:01}/"
        datas = processing(url)
        for data in datas:
            print(data)
            data["datetime"] = f"{current.day:02}-{current.month:02}-{current.year}"
            datas_.append(data)
        current += timedelta(days=1)
