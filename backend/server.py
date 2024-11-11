from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/hello')
def hello():
    return "hello, how are you"


if __name__ == "__main__":
    print("starting python flask server for grocery app")
    app.run(port=5000)