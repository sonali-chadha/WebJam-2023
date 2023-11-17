from flask import Flask, render_template, jsonify
from openai import OpenAI
import random
import requests

client = OpenAI(
    # Defaults to os.environ.get("OPENAI_API_KEY")
    # Otherwise use: api_key="Your_API_Key",
)


app = Flask(__name__)
facts = [
    "A group of flamingos is called a flamboyance.",
    "The longest English word is 189,819 letters long and takes more than 3 hours to pronounce.",
    "The shortest war in history was between Britain and Zanzibar in 1896. Zanzibar surrendered after just 38 minutes.",
    "There are more possible iterations of a game of chess than there are atoms in the known universe.",
    "The first webcam was created to check the coffee pot at Cambridge University.",
    "Bananas are berries, but strawberries are not.",
]
# test to see if this runs
# will revise the facts variable to take facts from API


@app.route("/a")  # polar bear
def home():
    fact = random.choice(facts)
    return render_template("index.html", fact=fact)


# @app.route("/") # red wolf


@app.route("/generate")  # snow leopard
def generate():
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        temperature=1,
        max_tokens=512,
        frequency_penalty=0.1,
        presence_penalty=0.2,
        messages=[
            {
                "role": "system",
                "content": "You are helping raise awareness for an endangered animal. You'll be given the Wikipedia article about the animal. Respond with 10 fun facts about interesting quirks of the specified animal. Write at a 5th grade level. Each fun fact should be 2-3 sentences long. Put a new line between each fun fact. Do not include any introduction, bullet points, or numbers.",
            },
            {
                "role": "user",
                "content": "Red wolf\nThe red wolf (Canis rufus)[2][6][7] is a canine native to the\nsoutheastern United States. Its size is intermediate between the\ncoyote (Canis latrans) and gray wolf (Canis lupus).\n[8]\nThe red wolf's taxonomic classification as being a separate\nspecies has been contentious for nearly a century, being\nclassified either as a subspecies of the gray wolf Canis lupus\nrufus,\n[9]",
            },
        ],
    )

    animal_string = chat_completion.choices[0].message.content
    animal_facts = animal_string.split("\n")
    while ("" in animal_facts):
        animal_facts.remove("")
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
