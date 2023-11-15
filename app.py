# going thru ryan's tutorial to get used to flask

from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({"message":'hey, everything works!'})


if(__name__ == "__main__"):
    app.run()


