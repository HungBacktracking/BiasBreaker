from database.database import db
from bson import ObjectId
from datetime import datetime, timedelta
from bson.regex import Regex

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

    @staticmethod
    def find_article_from_to_date(startdate, enddate, category, publisher):
        articles_list = []
        if startdate == "00-00-00" and enddate == "00-00-00":  # cho tất cả
            if category == "all" and publisher == "all":
                return Article.find_all()
            else:
                if publisher == "all":
                    return Article.find_all_by_category(category)
                elif category == "all":
                    return Article.find_all_article_by_publisher(publisher)
                else:
                    return Article.find_all_article_by_publisher_category(
                        publisher, category
                    )
        else:
            if category == "all":
                category = Regex(".*")
            if publisher == "all":
                publisher = Regex(".*")
            artilces_list_byday = articles.find(
                {
                    "datetime": {
                        "$gte": datetime.strptime(startdate, "%d-%m-%Y"),
                        "$lte": datetime.strptime(enddate, "%d-%m-%Y"),
                    },
                    "publisher": publisher,
                    "category": category,
                }
            )
            for article in artilces_list_byday:
                article["_id"] = str(article["_id"])
                articles_list.append(article)
            return articles_list

    @staticmethod
    def find_by_keywords_in_title(startdate, enddate, keyword, category, publisher):
        if startdate == "00-00-00" and enddate == "00-00-00":
            startdate = datetime.strptime("01-05-2024", "%d-%m-%Y")
            enddate = datetime.now() + timedelta(days=1)
        else:
            startdate = datetime.strptime(startdate, "%d-%m-%Y")
            enddate = datetime.strptime(enddate, "%d-%m-%Y")
        if category == "all":
            category = Regex(".*")
        if publisher == "all":
            publisher = Regex(".*")
        keyword_pattern = ".*" + ".*".join(keyword.split()) + ".*"
        print(keyword_pattern)
        print(startdate, enddate)
        query = {
            "datetime": {"$gte": startdate, "$lte": enddate},
            "publisher": publisher,
            "category": category,
            "title": {
                "$regex": keyword_pattern,
                "$options": "i",
            },  # Case-insensitive regex
        }
        articles_list = list(articles.find(query))
        for article in articles_list:
            article["_id"] = str(article["_id"])
        return articles_list
