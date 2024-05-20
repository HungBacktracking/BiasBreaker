from flask import jsonify
from models.article_model import Article


def get_article(article_id):
    article = Article.find_one(article_id)
    if article:
        return jsonify(article)
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
    articles = Article.find_top_latest_articles(category, 3)
    return jsonify({"articles": articles})


def get_latest_and_related():
    articles = Article.find_top_latest_and_top_related(3)
    return jsonify({"articles": articles})
