from flask import Blueprint, request
from controllers.users_controller import get_user, delete_user, update_user

user = Blueprint("user", __name__)


@user.route("/users/<user_id>", methods=["GET"])
def get_user_route(article_id):
    return get_user(article_id)

@user.route("/users/delete/<user_id>", methods=["DELETE"])
def delete_user_route(user_id):
    return delete_user(user_id)


@user.route("/users/update/<user_id>", methods=["PUT"])
def update_user_route(user_id):
    return update_user(user_id, request.json)

