from flask import jsonify
from models.article_model import Article


def get_article(article_id):
    article = Article.find_one(article_id)
    if article:
        article["_id"] = str(article["_id"])  # avoiding cannot jsonify
        return jsonify(article)
    else:
        return jsonify({"error": "Article not found"}), 404
