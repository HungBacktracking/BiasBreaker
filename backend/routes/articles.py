from flask import Blueprint
from controllers.articles import get_article

article = Blueprint("article", __name__)


@article.route("/articles/<article_id>", methods=["GET"])
def get_article_route(article_id):
    return get_article(article_id)
