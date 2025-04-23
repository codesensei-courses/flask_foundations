from flask import Flask, render_template

app = Flask(__name__)

db = [
    {"question": "Capital of Angola", "answer": "Luanda"},
    {"question": "Capital of Haïti", "answer": "Port-au-Prince"},
    {"question": "Capital of Kyrgyzstan", "answer": "Bishkek"},
    {"question": "Capital of the Philippines", "answer": "Manila"},
    {"question": "Capital of Uruguay", "answer": "Montevideo"},
]


@app.route("/")
def welcome():
    return render_template(
        "welcome.html",
        message="Data sent from view to template",
        x=42
    )


@app.route("/card")
def card_view():
    card = db[0]
    return render_template("card.html", card=card)
