from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/lena")
def lena():
    return "<h1>I am Lena</h1>"


@app.route("/json-example", methods=["POST"])
def json_example():
    content = request.get_json(silent=True)
    return content


if __name__ == "__main__":
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
