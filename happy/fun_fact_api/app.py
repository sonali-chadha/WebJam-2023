from flask import Flask, render_template
import random
import requests
import json


app = Flask(__name__)
facts = [
   "A group of flamingos is called a flamboyance.",
   "The longest English word is 189,819 letters long and takes more than 3 hours to pronounce.",
   "The shortest war in history was between Britain and Zanzibar in 1896. Zanzibar surrendered after just 38 minutes.",
   "There are more possible iterations of a game of chess than there are atoms in the known universe.",
   "The first webcam was created to check the coffee pot at Cambridge University.",
   "Bananas are berries, but strawberries are not."
]
# test to see if this runs
# will revise the facts variable to take facts from API


@app.route("/") # polar bear
def home():
   fact = random.choice(facts)
   return render_template("index.html", fact=fact)
if __name__ == "__main__":
   app.run(debug=True)

#@app.route("/") # red wolf 

#@app.route("/") # snow leopard


# make request
url = 'https://jsonplaceholder.typicode.com/users'            # test link
response = requests.get(url)
temp_list = []
if response.status_code == 200:
   data = response.json()
   #temp_data = json.load(response)
   #print(data)                                              # this runs but it prints
   print(f"Name:{['name']}")
   for user in data:
      print(f"Name:{user['name']}")                         # confused why this isn't working 
      
else:
   print(f"ERROR: {response.status_code}")

# handle API? 

# extracted_json = json.loads(data)

""" headers = {
   'Authorization':'Bearer API-KEY'
   'Content-Type':'application/json'
}

response = requests.get('link',headers=headers)
 """
