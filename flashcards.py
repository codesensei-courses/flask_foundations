from flask import Flask, render_template, abort

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
        cards=db
    )


@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html",
                               card=card,
                               index=index,
                               max_index=len(db)-1)
    except IndexError:
        abort(404)

