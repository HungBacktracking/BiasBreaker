import requests
from bs4 import BeautifulSoup
import validators
from datetime import datetime


url = "https://www.usatoday.com"


def get_links_to_category():
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    elems = soup.find("nav", class_="gnt_n_mn")
    links = []
    elems = elems.find_all(
        "a", class_=["gnt_n_mn_l gnt_n_mn_ce", "gnt_n_mn_l gnt_n_mn_l__fi gnt_n_mn_ce"]
    )
    for elem in elems:
        links.append(url + elem.get("href"))
    return links


def links_to_papers_(link_to_a_category):
    links_to_papers = []
    res = requests.get(link_to_a_category)
    soup_of_a_paper = BeautifulSoup(res.text, "html.parser")
    elems = soup_of_a_paper.find_all(
        "div", class_=["gnt_m_ht", "gnt_m gnt_m_flm", "gnt_m_th"]
    )
    for elem in elems:
        tag_a = elem.find_all("a")
        for tag in tag_a:
            try:
                paper_link = url + tag.get("href")
                links_to_papers.append(paper_link)
            except Exception as e:
                print(f"Error occurred while appending link: {e} {tag}")
    return links_to_papers


def get_title(soup_of_a_paper):
    elem_title = soup_of_a_paper.find("h1", class_="gnt_ar_hl")
    title = ""
    if elem_title is not None:
        title = elem_title.text
        return title
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


def get_authors(soup_of_a_paper):
    elem_author = soup_of_a_paper.find("div", class_="gnt_ar_by")
    if elem_author is not None:
        author_elem = elem_author.find_all("a")
        authors = [author.text for author in author_elem]
        return authors
    else:
        return []


def get_images(soup_of_a_paper):
    images = []
    elem_images = soup_of_a_paper.find_all("img", class_="gnt_em_img_i")
    for image in elem_images:
        img_des = image.get("alt")
        img_src = image.get("data-gl-srcset")
        if img_des is not None and img_src is not None:
            images.append((img_src, img_des))
    return images


def convert_to_datetime(date_str):

    format_str = "%I:%M %p %B %d %Y"  # Adjust for different formats if needed

    try:
        # Parse the string using datetime.strptime
        datetime_obj = datetime.strptime(date_str, format_str)
        return datetime_obj
    except ValueError:
        print(f"Invalid date format: {date_str}")
        return None


def get_date(soup_of_a_paper):
    elems_date = soup_of_a_paper.find("div", class_="gnt_ar_dt")
    if elems_date is not None:
        date_str = elems_date.get("aria-label")
        if date_str is not None:
            str_original = date_str.split(" Updated")[0]
            modified_str = (
                str_original.replace("Published ", "")
                .replace("a.m. ", "am")
                .replace("p.m. ", "pm")
                .replace("ET", "")
                .replace(",", "")
                .replace("Published: ", "")
            )
            datetime_obj = convert_to_datetime(modified_str)
        return datetime_obj
    return None


def CRAWL():
    links = get_links_to_category()
    data = []
    for link_to_a_category in links:
        links_to_papers = links_to_papers_(link_to_a_category)
        for link_to_a_paper in links_to_papers:
            try:
                if not validators.url(link_to_a_paper):  # Optional URL validation
                    print(f"{link_to_a_paper} is not a valid URL. Skipping...")
                    continue  # Move to the next iteration

                res = requests.get(link_to_a_paper)
                soup_of_a_paper = BeautifulSoup(res.text, "html.parser")
                elem_title = soup_of_a_paper.find("h1", class_="gnt_ar_hl")
                title = get_title(soup_of_a_paper)
                text = get_text(soup_of_a_paper)
                elem_author = soup_of_a_paper.find("div", class_="gnt_ar_by")
                authors = get_authors(soup_of_a_paper)
                images = get_images(soup_of_a_paper)
                date = get_date(soup_of_a_paper)
                # print(datetime_obj)
                data_dict = {
                    "Title": title,
                    "Text": text,
                    "Authors": authors,
                    "Images": images,
                    "Time": date,
                }
                if data_dict["Text"] != "" and data_dict["Title"] != "":
                    data.append(data_dict)

            except requests.exceptions.InvalidURL as e:
                print(f"Invalid URL: {link_to_a_paper} ({e})")
            except requests.exceptions.RequestException as e:
                print(f"Error fetching {link_to_a_paper}: {e}")

    return data


data = CRAWL()
print(len(data))
print(data)
