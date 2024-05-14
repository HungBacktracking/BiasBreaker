from flask import Blueprint
from controllers.users_controller import get_user

user = Blueprint("user", __name__)


@user.route("/users/<user_id>", methods=["GET"])
def get_user_route(article_id):
    return get_user(article_id)
