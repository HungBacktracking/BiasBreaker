from database import db
from bson import ObjectId

articles = db["articles"]


class Article:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    @staticmethod
    def find_one(id):
        article = articles.find_one({"_id": ObjectId(id)})
        return article

    @staticmethod
    def find_all():
        articles_list = articles.find()
        serialized_articles = []
        for article in articles_list:
            article["_id"] = str(article["_id"])
            serialized_articles.append(article)
        return serialized_articles

    @staticmethod
    def find_all_by_category(category):
        articles_list = articles.find({"category": category})
        serialized_articles = []
        for article in articles_list:
            article["_id"] = str(article["_id"])
            serialized_articles.append(article)
        return serialized_articles
