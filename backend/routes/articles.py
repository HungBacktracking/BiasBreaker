from flask import Blueprint
from controllers.articles import get_article
from controllers.articles import get_all_article
from controllers.articles import get_all_article_by_category

article_blueprint = Blueprint("article", __name__)


@article_blueprint.route("/articles/<article_id>", methods=["GET"])
def get_article_route(article_id):
    return get_article(article_id)


@article_blueprint.route("/articles", methods=["GET"])
def get_all_article_route():
    return get_all_article()


@article_blueprint.route("/articles/category/<category>", methods=["GET"])
def get_all_by_category(category):
    return get_all_article_by_category(category)
