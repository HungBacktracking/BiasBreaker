from flask import jsonify
from bson import ObjectId
from models.article_model import Article
from models.users_model import User
from LLM_Models.model import Predictor, TextSummarizer
from recommender.main import Recommender, HybridRecommender


def get_article(article_id):
    article = Article.find_one(article_id)
    if article:
        return jsonify({"articles": article})
    else:
        return jsonify({"error": "Article not found"}), 404


def get_all_article():
    articles = Article.find_all()
    return jsonify({"articles": articles})


def get_all_article_by_category(category):
    articles = Article.find_all_by_category(category)
    return jsonify({"articles": articles})


def get_all_article_by_publisher(publisher):
    articles = Article.find_all_article_by_publisher(publisher)
    return jsonify({"articles": articles})


def get_recommendation(request):
    user_email = request.get("email")
    user = User.find_one(user_email)

    if not user:
        return jsonify({"error": "Article not found"}), 404

    recommender = Recommender()
    recommendations = recommender.get_recommendations_for_user(ObjectId(user["_id"]))

    ans = []
    for i in range(len(recommendations)):
        recommendations[i] = Article.find_one(recommendations[i])
        ans.append(recommendations[i])

    return jsonify({"articles": ans})


def get_recommendation_related(request):
    user_email = request.get("email")
    user = User.find_one(user_email)

    if not user:
        return jsonify({"error": "Article not found"}), 404

    recommender = HybridRecommender()
    recommendations = recommender.get_recommendations_for_user(ObjectId(user["_id"]))

    ans = []
    for i in range(len(recommendations)):
        recommendations[i] = Article.find_one(recommendations[i])
        related = Article.find_top_related_articles(recommendations[i]["_id"], 3)
        recommendations[i]["related"] = related
        ans.append(recommendations[i])

    return jsonify({"articles": ans})


def get_prediction(request):
    article_id = request.get("id")
    article = Article.find_one(article_id)

    if not article:
        return jsonify({"error": "Article not found"}), 404
    if "prediction" in article:
        return jsonify({"prediction": article["prediction"]}), 200

    predictor = Predictor()
    prediction = predictor.predict_from_article(article["content"])
    article["prediction"] = prediction
    Article.update_article(article_id, article)

    return jsonify({"message": "Prediction generated", "prediction": prediction})


def get_summary(request):
    article_id = request.get("id")
    article = Article.find_one(article_id)

    if not article:
        return jsonify({"error": "Article not found"}), 404
    if "summary" in article:
        return jsonify({"summary": article["summary"]}), 200

    summarizer = TextSummarizer()
    summary = summarizer.summarize(article["content"])
    article["summary"] = summary
    Article.update_article(article_id, article)

    return jsonify({"message": "Summary generated", "summary": summary})


def get_all_article_by_publisher_category(publisher, category):
    articles = Article.find_all_article_by_publisher_category(publisher, category)
    return jsonify({"articles": articles})


def add_article(article):
    _id = Article.push_article(article)
    if _id is not None:
        return jsonify({"message": "Added"})
    else:
        return jsonify({"error": "Cannot add"}), 404


def delete_article(article_id):
    if Article.pop_article(article_id):
        return jsonify({"message": "Deleted"})
    else:
        return jsonify({"error": "Cannot delete"}), 404


def update_article_by_id(article_id, update_article):
    if Article.update_article(article_id, update_article):
        return jsonify({"message": "Update"})
    else:
        return jsonify({"error": "Cannot update"}), 404


def get_article_from_to_date(startdate, enddate, category, publisher):
    articles = Article.find_article_from_to_date(
        startdate, enddate, category, publisher
    )
    return jsonify({"articles": articles})


def get_article_by_keywords_in_title(startdate, enddate, keyword, category, publisher):
    articles = Article.find_by_keywords_in_title(
        startdate, enddate, keyword, category, publisher
    )
    return jsonify({"articles": articles})


def get_related_articles(id):
    articles = Article.find_top_related_articles(id, 3)
    return jsonify({"articles": articles})


def get_latest_article(category):
    articles = Article.find_top_latest_articles(category)
    return jsonify({"articles": articles})


def get_latest_and_related():
    articles = Article.find_top_latest_and_top_related(3)
    return jsonify({"articles": articles})


def get_latest_and_related_with_category(category):
    articles = Article.find_top_latest_and_top_related_with_category(category)
    return jsonify({"articles": articles})


def get_by_keyword_list(startdate, enddate, keyword, category, publisher):
    articles = Article.find_by_keywords_in_list(
        startdate, enddate, keyword, category, publisher
    )
    return jsonify({"articles": articles})


def count_keywords(startdate, enddate, publisher):
    keywords = Article.count_keywords(startdate, enddate, publisher)
    return jsonify({"keywords_count": keywords})


def get_latest_by_category_and_limit(category, limit):
    articles = Article.find_latest_by_category_and_limit(category, limit)
    return jsonify({"articles": articles})


def get_top_keywords_and_articles(startdate, enddate, limit):
    data = Article.find_top_keywords_and_articles(startdate, enddate, limit)
    return jsonify({"keywords": data})


def get_latest_paper_by_keywords(keywords, limit):
    articles = Article.find_latest_paper_by_keywords(keywords, limit)
    return jsonify({"articles": articles})


def get_latest_top_keywords_of_nearest_day(limit, numbers_of_day):
    keywords = Article.find_latest_top_keywords_of_nearest_day(limit, numbers_of_day)
    return jsonify({"keywords": keywords})


def get_predict_by_keywords_and_date(date, limit):
    predict = Article.find_predict_by_keywords_and_date(date, limit)
    return jsonify({"Predictions": predict})
