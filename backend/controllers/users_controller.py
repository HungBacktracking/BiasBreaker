from flask import jsonify
from ..models.users_model import User


def get_user(id):
    user = User.find_one_by_id(id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404
    
def update_user(id, request):
    password = request.get('password')
    User.update_by_id(id, password)
    return jsonify({"message": "User updated"}), 200

def delete_user(id):
    User.delete_by_id(id)
    return jsonify({"message": "User deleted"}), 200
