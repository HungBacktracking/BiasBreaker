from flask import Blueprint
from flask import request
from ..controllers.articles_controller import (
    get_article,
    get_all_article,
    get_all_article_by_category,
    get_all_article_by_publisher,
    get_all_article_by_publisher_category,
    get_all_article_by_date,
    get_all_article_by_date_publisher,
    get_all_article_by_date_category,
    get_all_article_by_date_publisher_category,
    add_article,
    delete_article,
    update_article_by_id,
    get_summary_article_by_id,
    get_relevant_article,
)

article = Blueprint("article", __name__)


@article.route("/articles/<article_id>", methods=["GET"])
def get_article_route(article_id):
    return get_article(article_id)


@article.route("/articles", methods=["GET"])
def get_all_article_route():
    return get_all_article()


@article.route("/articles/category/<category>", methods=["GET"])
def get_all_article_by_category_route(category):
    return get_all_article_by_category(category)


@article.route("/articles/publisher/<publisher_name>", methods=["GET"])
def get_all_article_by_publisher_route(publisher_name):
    return get_all_article_by_publisher(publisher_name)


@article.route(
    "/articles/publisher/<publisher_name>/category/<category>", methods=["GET"]
)
def get_all_article_by_publisher_category_route(publisher_name, category):
    return get_all_article_by_publisher_category(publisher_name, category)


@article.route("/articles/<date>/<month>/<year>", methods=["GET"])
def get_all_article_by_date_route(date, month, year):
    return get_all_article_by_date(f"{date}-{month}-{year}")


@article.route(
    "/articles/<date>/<month>/<year>/publish/<publisher_name>", methods=["GET"]
)
def get_all_article_by_date_publisher_route(date, month, year, publisher_name):
    return get_all_article_by_date_publisher(f"{date}-{month}-{year}", publisher_name)


@article.route("/articles/<date>/<month>/<year>/category/<category>", methods=["GET"])
def get_all_article_by_date_category_route(date, month, year, category):
    return get_all_article_by_date_category(f"{date}-{month}-{year}", category)


@article.route(
    "/articles/<date>/<month>/<year>/publish/<publisher_name>/category/<category>",
    methods=["GET"],
)
def get_all_article_by_date_publisher_category_route(
    date, month, year, publisher_name, category
):
    return get_all_article_by_date_publisher_category(
        f"{date}-{month}-{year}", publisher_name, category
    )


@article.route("/articles/addarticle", methods=["POST"])
def add_article_route():
    article_post = request.get_json()
    return add_article(article)


@article.route("/articles/deletearrticle/<id>", methods=["DELETE"])
def delete_article_route(id):
    return delete_article(id)


@article.route("/articles/updatearticle/<id>", methods=["PUT"])
def update_article_route(id):
    article_update = request.get_json()
    return update_article_by_id(id, article_update)


@article.route("/articles/<id>/summary", methods=["GET"])
def get_summary_article_by_id_route(id):
    return get_summary_article_by_id(id)


@article.route("/articles/<id>/relevant", methods=["GET"])
def get_relevant_article_route(id):
    return get_relevant_article(id)
