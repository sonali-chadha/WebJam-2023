from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from openai import OpenAI
#import random
#import requests
from animal_wiki import test_wiki, red_wolf_wiki, snow_leopard_wiki, polar_bear_wiki

client = OpenAI(
    # Defaults to os.environ.get("OPENAI_API_KEY")
   api_key="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"
)

# this is just to test --> connects to html and displays 1 fact at at time
app = Flask(__name__)

# start of to-dos --------------------------------------------------------------------------------------------
# this is just to test --> connects to html and displays 1 fact at at time
app = Flask(__name__)

# start of to-dos --------------------------------------------------------------------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

@app.route("/")
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

# end of to-do -----------------------------------------------------------------------------------------------------

# generate age is a mini test run
# each animal has their respective page
# will run 1 time to get facts from openai API and will display the same facts ran 
# so less monies spent el oh el

facts_holder=[]
RW_facts_holder=[]
SL_facts_holder=[]
PB_facts_holder=[]

@app.route("/generate")  # generate animal fun facts
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
    with app.app_context():
        db.create_all()
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
