from database import db
from pymongo import MongoClient
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime, timedelta

Article = db["articles"]
Relative = db["relatives"]

articles = list(Article.find())


def get_yesterday(date_str):
    date = datetime.strptime(date_str, "%d-%m-%Y")
    yesterday = date - timedelta(days=1)
    # Format the date back to string
    return yesterday.strftime("%d-%m-%Y")


# def find_related_articles(
#     article_list, target_index, num_related_articles=5
# ):  # finding top 5 relative of articles[target_index], base on the current date and yesterday
#     date = article_list[target_index]["datetime"]  # get date
#     date_articles_list = list(
#         Article.find({"$or": [{"datetime": get_yesterday(date)}, {"datetime": date}]})
#     )
#     # Extract titles and contents
#     titles = [article["title"] for article in date_articles_list]
#     contents = [article["content"] for article in date_articles_list]

#     # Combine titles and contents for better similarity computation
#     combined_texts = [title + " " + content for title, content in zip(titles, contents)]

#     # Vectorize the combined texts using TF-IDF
#     vectorizer = TfidfVectorizer()
#     tfidf_matrix = vectorizer.fit_transform(combined_texts)

#     # Calculate cosine similarity between target article and all articles
#     similarities = cosine_similarity(tfidf_matrix[target_index], tfidf_matrix)

#     # Get indices of top related articles
#     related_indices = similarities.argsort()[0][-num_related_articles - 1 : -1][::-1]

#     # Return related articles
#     related_articles = [articles[i]["_id"] for i in related_indices]

#     return related_articles


def relative_by_date(
    date="10-05-2024", num_related_articles=5
):  # finding relative article by date
    articles_by_date = list(
        Article.find({"$or": [{"datetime": get_yesterday(date)}, {"datetime": date}]})
    )
    relative_list_article_checking = list(
        Article.find({"$or": [{"datetime": get_yesterday(date)}, {"datetime": date}]})
    )  # finding all relative in this list
    titles = [article["title"] for article in relative_list_article_checking]
    contents = [article["content"] for article in relative_list_article_checking]
    combined_texts = [title + " " + content for title, content in zip(titles, contents)]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(combined_texts)
    for article in articles_by_date:
        article_vector = tfidf_matrix[
            combined_texts.index(article["title"] + " " + article["content"])
        ]
        similarities = cosine_similarity(article_vector, tfidf_matrix)
        related_indices = similarities.argsort()[0][-num_related_articles - 1 : -1][
            ::-1
        ]
        related_articles = [articles[i]["_id"] for i in related_indices]
        data = {}
        data["article_id"] = article["_id"]
        data["relation"] = related_articles
        Relative.insert_one(data)

    # return related_articles


# relative_by_date()  # push all article to database
