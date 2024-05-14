from flask import Blueprint
from controllers.users import get_user

user = Blueprint("user", __name__)


@user.route("/users/<user_id>", methods=["GET"])
def get_user_route(article_id):
    return get_user(article_id)
