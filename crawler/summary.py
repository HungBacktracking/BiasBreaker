from model.model import Predictor, TextSummarizer
from database import db
from rich.markdown import Markdown
from rich.console import Console

console = Console()
Articles = db["articles"]

articles = list(Articles.find())

summarizer = TextSummarizer()


def summary(target_index, date="10-05-2024"):
    date_articles_list = list(Articles.find({"datetime": date}))
    summary_ = summarizer.get_result(date_articles_list[target_index]["content"])
    return summary_


print(articles[0]["content"])
print(articles[1]["info_link"])


for i in range(10):
    print(i)
    print(articles[i]["title"])
    print(articles[i]["content"])
    print(summary(i, "10-05-2024"))
