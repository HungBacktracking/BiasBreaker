from database import db
from pymongo import MongoClient
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime, timedelta

Article = db["articles"]

articles = list(Article.find())


def get_yesterday(date_str):
    date = datetime.strptime(date_str, "%d-%m-%Y")
    yesterday = date - timedelta(days=1)
    # Format the date back to string
    return yesterday.strftime("%d-%m-%Y")


def find_related_articles(
    article_list, target_index, num_related_articles=5
):  # finding top 5 relative of articles[target_index], base on the current date and yesterday
    date = article_list[target_index]["datetime"]  # get date
    date_articles_list = list(
        Article.find({"$or": [{"datetime": get_yesterday(date)}, {"datetime": date}]})
    )
    # Extract titles and contents
    titles = [article["title"] for article in date_articles_list]
    contents = [article["content"] for article in date_articles_list]

    # Combine titles and contents for better similarity computation
    combined_texts = [title + " " + content for title, content in zip(titles, contents)]

    # Vectorize the combined texts using TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(combined_texts)

    # Calculate cosine similarity between target article and all articles
    similarities = cosine_similarity(tfidf_matrix[target_index], tfidf_matrix)

    # Get indices of top related articles
    related_indices = similarities.argsort()[0][-num_related_articles - 1 : -1][::-1]

    # Return related articles
    related_articles = [articles[i]["_id"] for i in related_indices]

    return related_articles


# Assuming you want to find related articles for the first article
target_index = 1
related_articles = find_related_articles(articles, target_index)
print(related_articles)
print(articles[target_index])
print("relatvies:")
for relative in related_articles:
    result = Article.find_one(relative)
    print(result)
