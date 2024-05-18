# from model.model import Predictor, TextSummarizer
# from database import db
# from rich.markdown import Markdown
# from rich.console import Console
# import time


# console = Console()
# Articles = db["articles"]
# Summary = db["summaries"]

# articles = list(Articles.find())

# summarizer = TextSummarizer()

# date_article_list = list(Articles.find({"datetime": "10-05-2024"}))
# print(len(date_article_list))


# def summary_by_date(date="10-05-2024"):
#     date_article_list = list(Articles.find({"datetime": date}))
#     for article in date_article_list:
#         data = {}
#         data["article_id"] = article["_id"]
#         summary_content = summarizer.get_result(article["content"])
#         data["summary"] = summary_content
#         result = Summary.insert_one(data)
#         if result.inserted_id:
#             print("inserted successful")
#         else:
#             print("Failed")
#         time.sleep(30)
#         # print(data)


# # summary_by_date("10-05-2024") #adding summary of article to database


from model.model import TextSummarizer
import time

summarizer = TextSummarizer()


def insert_summaries(dataset):
    for data in dataset:
        content = data["content"]
        summary_content = summarizer.get_result(content)
        data["summaries"] = summary_content
        time.sleep(30)
