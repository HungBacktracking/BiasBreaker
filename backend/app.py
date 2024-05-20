from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from routes.articles_route import article
from routes.users_route import user
from routes.auth_route import auth
import config

app = Flask(__name__)

CORS(app)
app.config["JWT_SECRET_KEY"] = config.JWT_SECRECT_KEY
jwt = JWTManager(app)

app.register_blueprint(article)
app.register_blueprint(user)
app.register_blueprint(auth)


@app.route("/")
@app.route("/index")
def index():
    return jsonify({"message": "Hello World!"}), 200


if __name__ == "__main__":
    app.run()
