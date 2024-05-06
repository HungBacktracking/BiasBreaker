from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return jsonify({'message': 'Hello World!'}), 200

if __name__ == '__main__':
    app.run()