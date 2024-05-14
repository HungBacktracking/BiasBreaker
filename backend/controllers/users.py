from flask import jsonify
from models.users import User


def get_user(email):
    user = User.find_one(email)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404
