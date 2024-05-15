# auth_controller.py
from flask import jsonify
from flask_jwt_extended import create_access_token
from ..models.users_model import User


def signup_controller(request):
    email = request.get('email')
    password = request.get('password')

    if User.checkExists(email):
        return jsonify({"message": "User already exists"}), 400
    else:
        User.create(email, password)
        return jsonify({"message": "User created"}), 201

def login_controller(request):
    email = request.get('email')
    password = request.get('password')

    if User.validate(email, password):
        access_token = create_access_token(identity = email)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Wrong username or password"}), 401
    
def logout_controller():
    # JWT tokens are stateless, so logout is typically handled on the client side by deleting the token
    return jsonify({'message': 'Logout successful'}), 200
