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

    @staticmethod
    def find_all_article_by_publisher(publisher):
        articles_list = articles.find({"publisher": publisher})
        serialized_articles = []
        for article in articles_list:
            article["_id"] = str(article["_id"])
            serialized_articles.append(article)
        return serialized_articles

    @staticmethod
    def find_all_article_by_publisher_category(publisher, category):
        articles_list = articles.find({"publisher": publisher, "category": category})
        serialized_articles = []
        for article in articles_list:
            article["_id"] = str(article["_id"])
            serialized_articles.append(article)
        return serialized_articles

    @staticmethod
    def find_all_article_by_date(date):
        articles_list = articles.find({"datetime": date})
        serialized_articles = []
        for article in articles_list:
            article["_id"] = str(article["_id"])
            serialized_articles.append(article)
        return serialized_articles

    @staticmethod
    def find_all_article_by_date_publisher(date, publisher):
        articles_list = articles.find({"datetime": date, "publisher": publisher})
        serialized_articles = []
        for article in articles_list:
            article["_id"] = str(article["_id"])
            serialized_articles.append(article)
        return serialized_articles

    @staticmethod
    def find_all_article_by_date_category(date, category):
        articles_list = articles.find({"datetime": date, "category": category})
        serialized_articles = []
        for article in articles_list:
            article["_id"] = str(article["_id"])
            serialized_articles.append(article)
        return serialized_articles

    @staticmethod
    def find_all_article_by_date_publsiher_category(date, publisher, category):
        articles_list = articles.find(
            {"datetime": date, "publisher": publisher, "category": category}
        )
        serialized_articles = []
        for article in articles_list:
            article["_id"] = str(article["_id"])
            serialized_articles.append(article)
        return serialized_articles

    @staticmethod
    def push_article(article):
        try:
            result = articles.insert_one(article)
            return result.inserted_id
        except:
            return None

    @staticmethod
    def pop_article(id):
        delete_result = articles.delete_one({"_id": ObjectId(id)})
        if delete_result.deleted_count == 1:
            return True
        else:
            return False

    @staticmethod
    def update_article(id, update_article):
        update_result = articles.update_one(
            {"_id": ObjectId(id)}, {"$set": update_article}
        )

        if update_result.matched_count == 1:
            return True
        else:
            return False
