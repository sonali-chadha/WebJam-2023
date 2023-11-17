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

# use ngrok to tunnel server to internet
# didn't get that far :c



# if europe: #antartica
#   go to polar bear page
# elif russia_asia: #asia
#   go to snow leopard page
# elif amurica: #nort murica
#   go to red fox page
# else: 
#   still under works, select different location , ty <3


# 
