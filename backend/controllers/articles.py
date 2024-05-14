from flask import jsonify
from models.article import Article


def get_article(article_id):
    article = Article.find_one(article_id)
    if article:
        article["_id"] = str(article["_id"])  # avoiding cannot jsonify
        return jsonify(article)
    else:
        return jsonify({"error": "Article not found"}), 404


def get_all_article():
    articles = Article.find_all()
    return jsonify({"articles": articles})


def get_all_article_by_category(category):
    articles = Article.find_all_by_category(category)
    return jsonify({"articles": articles})
