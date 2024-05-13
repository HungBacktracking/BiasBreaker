from flask import Flask, jsonify
from routes.articles import article_blueprint

app = Flask(__name__)
app.register_blueprint(article_blueprint)


@app.route("/")
@app.route("/index")
def index():
    return jsonify({"message": "Hello World!"}), 200


if __name__ == "__main__":
    app.run()
