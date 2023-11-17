from flask import Flask, render_template
import random
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


@app.route("/")
def home():
   fact = random.choice(facts)
   return render_template("index.html", fact=fact)
if __name__ == "__main__":
   app.run(debug=True)

if(__name__ == "__main__"):
    app.run(debug=True)

