from flask import Blueprint, jsonify, request
from controllers.auth_controller import login_controller, signup_controller, logout_controller
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["POST"])
def register():
    return signup_controller(request.json)

@auth.route("/login", methods=["POST"])
def login():
    return login_controller(request.json)

@auth.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    return logout_controller()
