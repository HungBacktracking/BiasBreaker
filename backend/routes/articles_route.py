from flask import Blueprint
from flask import request
from controllers.articles_controller import (
    get_article,
    get_all_article,
    get_summary,
    get_prediction,
    get_recommendation,
    get_all_article_by_category,
    get_all_article_by_publisher,
    get_all_article_by_publisher_category,
    add_article,
    delete_article,
    update_article_by_id,
    get_article_from_to_date,
    get_article_by_keywords_in_title,
    get_related_articles,
    get_latest_article,
    get_latest_and_related,
    get_by_keyword_list,
    count_keywords,
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


@article.route("/get_summary", methods=["POST"])
def get_summary_route():
    return get_summary(request.json)


@article.route("/get_prediction", methods=["POST"])
def get_prediction_route():
    return get_prediction(request.json)

@article.route("/get_recommendation", methods=["POST"])
def get_recommendation_route():
    return get_recommendation(request.json)


@article.route(
    "/articles/publisher/<publisher_name>/category/<category>", methods=["GET"]
)
def get_all_article_by_publisher_category_route(publisher_name, category):
    return get_all_article_by_publisher_category(publisher_name, category)


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


@article.route(
    "/articles/from/<date1>/to/<date2>/category/<category>/publisher/<publisher>"
)
def get_article_from_to_date_route(date1, date2, category, publisher):
    return get_article_from_to_date(date1, date2, category, publisher)


@article.route(
    "/articles/from/<date1>/to/<date2>/keywords/<keywords>/title/category/<category>/publisher/<publisher>",
    methods=["GET"],
)
def get_article_by_keywords_in_title_route(date1, date2, keywords, category, publisher):
    return get_article_by_keywords_in_title(date1, date2, keywords, category, publisher)


@article.route("/articles/latest/category/<category>", methods=["GET"])
def get_latest_article_route(category):
    return get_latest_article(category)


@article.route("/articles/date-latest/latest-realated/", methods=["GET"])
def get_latest_and_relate():
    return get_latest_and_related()


@article.route("/articles/related/<id>")
def get_top_relate_articles(id):
    return get_related_articles(id)


@article.route(
    "/articles/from/<date1>/to/<date2>/keywords-list/<keywords>/category/<category>/publisher/<publisher>",
    methods=["GET"],
)
def get_by_key_word_route(date1, date2, keywords, category, publisher):
    return get_by_keyword_list(date1, date2, keywords, category, publisher)


@article.route(
    "/articles/from/<date1>/to/<date2>/statitic-keywords/publisher/<publisher>",
    methods=["GET"],
)  # count for statitic
def get_static_keywords(date1, date2, publisher):
    return count_keywords(date1, date2, publisher)
