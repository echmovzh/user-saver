from flask import Flask
from flask import request

from pymongo import MongoClient
from pprint import pprint

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/json-example", methods=["POST"])
def json_example():
    content = request.get_json(silent=True)
    return content


# save_user handles POST on /user and save user JSON to MongoDB
@app.route("/user", methods=["POST"])
def save_user():
    content = request.get_json(silent=True)
    client = MongoClient("mongodb://localhost:27017")
    db = client.users
    result = db.users.insert_one(content)
    return f"User {result.inserted_id} is created"


if __name__ == "__main__":
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
