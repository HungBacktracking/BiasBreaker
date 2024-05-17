from model.model import Predictor
from database import db
from rich.markdown import Markdown
from rich.console import Console
import time

console = Console()
Articles = db["articles"]

articles = list(Articles.find())

predictor = Predictor()


def prediction(target_index, date="10-05-2024"):
    date_articles_list = list(Articles.find({"datetime": date}))
    prediction_ = predictor.predict(date_articles_list[target_index]["content"])
    return prediction_


for i in range(16):
    print(i)
    print(articles[i]["title"])
    print(prediction(i, "10-05-2024"))
    time.sleep(10)
