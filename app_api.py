from flask import Flask, render_template, jsonify, redirect #, request
from flask_sqlalchemy import SQLAlchemy
from openai import OpenAI
from flask_cors import CORS
import random
#import requests
from animal_wiki import test_wiki, red_wolf_wiki, snow_leopard_wiki, polar_bear_wiki

client = OpenAI(
    # Defaults to os.environ.get("OPENAI_API_KEY")
    # Otherwise use: api_key="Your_API_Key",
)

app = Flask(__name__)
cors = CORS(app)

facts = [
    "A group of flamingos is called a flamboyance.",
    "The longest English word is 189,819 letters long and takes more than 3 hours to pronounce.",
    "The shortest war in history was between Britain and Zanzibar in 1896. Zanzibar surrendered after just 38 minutes.",
    "There are more possible iterations of a game of chess than there are atoms in the known universe.",
    "The first webcam was created to check the coffee pot at Cambridge University.",
    "Bananas are berries, but strawberries are not.",
]

@app.route("/")  
def home():
    fact = random.choice(facts)
    return render_template("temp_index.html", fact=fact)



# ----------------------------------------------------------------------------------------

#def save_to_json()


# ----------------------------------------------------------------------------------------

# generate age is a mini test run
# each animal has their respective page
# will run 1 time to get facts from openai API and will display the same facts ran 
# so less monies spent el oh el

facts_holder=[]
@app.route("/generate")  # generate fun facts for tests
def generate():
    global facts_holder 
    if len(facts_holder)>0:
        return jsonify({"message": facts_holder})
        
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106", #"gpt-4.0-preview-1106"
        temperature=1,
        max_tokens=512,
        frequency_penalty=0.1,
        presence_penalty=0.2,
        messages=test_wiki              # from animal_wiki file
    )
    animal_string = chat_completion.choices[0].message.content
    animal_facts = animal_string.split("\n")
    while ("" in animal_facts):
        animal_facts.remove("")
    facts_holder = animal_facts
    return jsonify({"message": animal_facts})

RW_facts_holder=[]
@app.route("/red_wolf")  # red_wolf
def generate_rw():
    global RW_facts_holder 
    if len(RW_facts_holder)>0:
        return jsonify({"message": RW_facts_holder})
        
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        temperature=1,
        max_tokens=512,
        frequency_penalty=0.1,
        presence_penalty=0.2,
        messages=red_wolf_wiki              # from animal_wiki file
    )
    animal_string = chat_completion.choices[0].message.content
    animal_facts = animal_string.split("\n")
    while ("" in animal_facts):
        animal_facts.remove("")
    RW_facts_holder = animal_facts
    return jsonify({"message": animal_facts})

PB_facts_holder=[]
@app.route("/polar_bear")  # polar bear
def generate_pb():
    global PB_facts_holder 
    if len(PB_facts_holder)>0:
        return jsonify({"message": PB_facts_holder})
        
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        temperature=1,
        max_tokens=512,
        frequency_penalty=0.1,
        presence_penalty=0.2,
        messages=polar_bear_wiki              # from animal_wiki file
    )
    animal_string = chat_completion.choices[0].message.content
    animal_facts = animal_string.split("\n")
    while ("" in animal_facts):
        animal_facts.remove("")
    PB_facts_holder = animal_facts
    return jsonify({"message": animal_facts})

SL_facts_holder=[]
@app.route("/snow_leopard")  # polar bear
def generate_sl():
    global SL_facts_holder 
    if len(SL_facts_holder)>0:
        return jsonify({"message": SL_facts_holder})
        
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        temperature=1,
        max_tokens=512,
        frequency_penalty=0.1,
        presence_penalty=0.2,
        messages=snow_leopard_wiki              # from animal_wiki file
    )
    animal_string = chat_completion.choices[0].message.content
    animal_facts = animal_string.split("\n")
    while ("" in animal_facts):
        animal_facts.remove("")
    SL_facts_holder = animal_facts
    return jsonify({"message": animal_facts})

if __name__ == "__main__":
    app.run(debug=True)

# make request
# url = "https://jsonplaceholder.typicode.com/users"  # test link
# response = requests.get(url)
# temp_list = []
# if response.status_code == 200:
#     data = response.json()
#     # temp_data = json.load(response)
#     # print(data)                                              # this runs but it prints
#     print(f"Name:{['name']}")
#     for user in data:
#         print(f"Name:{user['name']}")  # confused why this isn't working

# else:
#     print(f"ERROR: {response.status_code}")

# handle API?

# extracted_json = json.loads(data)

""" headers = {
   'Authorization':'Bearer API-KEY'
   'Content-Type':'application/json'
}

response = requests.get('link',headers=headers)
 """
