from database.database import db
from bson import ObjectId
from datetime import datetime, timedelta
from bson.regex import Regex
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

articles = db["articles"]


class Article:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    @staticmethod
    def find_one(id):
        article = articles.find_one({"_id": ObjectId(id)})
        if article:
            article["_id"] = str(article["_id"])
            return article
        else:
            return None

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

    @staticmethod
    def find_top_related_articles(id, limit=3):
        given_article = articles.find_one({"_id": ObjectId(id)})
        related_article_list = list(
            articles.find(
                {
                    "category": given_article["category"],
                    "datetime": {
                        "$gte": given_article["datetime"] - timedelta(days=3),
                        "$lt": given_article["datetime"] + timedelta(days=1),
                    },
                }
            )
        )
        title_and_contetnt = [
            data_["title"] + " " + data_["content"] for data_ in related_article_list
        ]
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform(title_and_contetnt)

        # Compute cosine similarity matrix
        similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

        # Find top 5 similar articles for each article
        given_article_index = next(
            (
                i
                for i, article in enumerate(related_article_list)
                if article["_id"] == given_article["_id"]
            ),
            None,
        )

        if given_article_index is None:
            return []

        # Exclude self-similarity
        similarities = similarity_matrix[given_article_index].copy()
        similarities[given_article_index] = -1

        # Get indices of top 3 similar articles
        top_indices = similarities.argsort()[-limit:][::-1]
        top_related_articles = []
        for i in top_indices:
            article = related_article_list[i]
            article["_id"] = str(article["_id"])
            top_related_articles.append(article)
        return top_related_articles

    @staticmethod
    def find_top_latest_articles(category, limit=3):
        latest_articles = list(
            articles.find({"category": category}).sort("datetime", -1).limit(limit)
        )
        for article in latest_articles:
            article["_id"] = str(article["_id"])
        return latest_articles

    @staticmethod
    def find_top_latest_and_top_related(limit=3):
        latest_articles = list(articles.find().sort("datetime", -1).limit(limit))
        for article in latest_articles:
            article["related"] = Article.find_top_related_articles(article["_id"])
            article["_id"] = str(article["_id"])
        return latest_articles
    
    @staticmethod
    def find_top_latest_and_top_related_with_category(category, limit=20):
        latest_articles = list(articles.find({"category": category}).sort("datetime", -1).limit(limit))
        for article in latest_articles:
            article["related"] = Article.find_top_related_articles(article["_id"])
            article["_id"] = str(article["_id"])
        return latest_articles

    @staticmethod
    def find_by_keywords_in_list(startdate, enddate, keyword, category, publisher):
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

        query = {
            "datetime": {"$gte": startdate, "$lte": enddate},
            "publisher": publisher,
            "category": category,
            "keywords": {"$regex": keyword, "$options": "i"},
        }
        articles_list = list(articles.find(query))
        for article in articles_list:
            article["_id"] = str(article["_id"])
        return articles_list

    @staticmethod
    def count_keywords(startdate, enddate, publisher):
        if startdate == "00-00-00" and enddate == "00-00-00":
            startdate = datetime.strptime("01-05-2024", "%d-%m-%Y")
            enddate = datetime.now() + timedelta(days=1)
        else:
            startdate = datetime.strptime(startdate, "%d-%m-%Y")
            enddate = datetime.strptime(enddate, "%d-%m-%Y")
        if publisher == "all":
            publisher = Regex(".*")

        pipeline = [
            {
                "$match": {
                    "datetime": {"$gte": startdate, "$lt": enddate + timedelta(days=1)},
                    "publisher": publisher,
                }
            },
            {"$unwind": "$keywords"},  # nested keywords
            {
                "$group": {
                    "_id": "$keywords",  # Group by the keywords field
                    "count": {"$sum": 1},  # Count occurrences for each keyword
                }
            },
        ]
        result = list(articles.aggregate(pipeline))
        dict_count = {}
        for key in result:
            dict_count[key["_id"]] = key["count"]
        return dict_count

    @staticmethod
    def find_latest_by_category_and_limit(category, limit):
        latest_articles = list(
            articles.find({"category": category}).sort("datetime", -1).limit(limit)
        )
        for article in latest_articles:
            article["_id"] = str(article["_id"])
        return latest_articles

    @staticmethod
    def find_top_keywords_and_articles(startdate, enddate, limit):
        publisher = "all"
        category = "all"
        date1 = datetime.strptime(startdate, "%d-%m-%Y")
        date2 = datetime.strptime(enddate, "%d-%m-%Y")
        data = []
        while date1 <= date2:
            data_date = {}
            data_date["datetime"] = date1
            data_date["keywords"] = []
            formatted_date = date1.strftime("%d-%m-%Y")
            dict_key = Article.count_keywords(formatted_date, formatted_date, publisher)
            sorted_dict = dict(sorted(dict_key.items(), key=lambda item: item[1]))
            i = 0
            for key, val in reversed(sorted_dict.items()):
                if i == 0:
                    i += 1
                    continue

                article = articles.find_one(
                    {
                        "datetime": date1,
                        "keywords": {"$regex": key, "$options": "i"},
                    }
                )
                article["_id"] = str(article["_id"])

                data_date["keywords"].append(
                    {
                        "keyword": key,
                        "article": article,
                        "frequency": val,
                    }
                )
                data.append(data_date)
                i += 1
                if i == limit + 1:
                    break
            date1 += timedelta(days=1)
        return data

    @staticmethod
    def find_latest_paper_by_keywords(keywords, limit):
        latest_articles = list(
            articles.find({"keywords": {"$regex": keywords, "$options": "i"}})
            .sort("datetime", -1)
            .limit(limit)
        )
        for article in latest_articles:
            article["_id"] = str(article["_id"])
        return latest_articles

    @staticmethod
    def find_latest_top_keywords_of_nearest_day(limit, numbers_of_day):
        latest_day = list(articles.find().sort("datetime", -1).limit(limit))[0][
            "datetime"
        ]
        format_time = latest_day.strftime("%d-%m-%Y")
        old_date = (latest_day - timedelta(days=numbers_of_day)).strftime("%d-%m-%Y")
        return Article.find_top_keywords_and_articles(old_date, format_time, limit)
