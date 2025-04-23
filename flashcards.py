from flask import Flask, render_template, abort, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length

app = Flask(__name__)
# The secret key should be unique for every application you create.
# It should be secret so you should NOT commit it to version control
# You can generate it using:
# python -c 'import secrets; print(secrets.token_hex())'
app.secret_key = "42e48357939870ca2663ebc3800477b40c9f417a3ec5d3e2bf8f34b41e01620b"

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


class AddCardForm(FlaskForm):
    question = StringField("Question", validators=[InputRequired(), Length(max=25)])
    answer = StringField("Answer", validators=[InputRequired()])


@app.route('/add_card', methods=['GET', 'POST'])
def add_card():
    form = AddCardForm(request.form)
    if form.validate_on_submit():
        db.append(
            {"question": form.question.data,
             "answer": form.answer.data}

        )
        return redirect(url_for("card_view", index=len(db) - 1))
    else:
        return render_template("add_card.html", form=form)


@app.route('/remove_card/<int:index>', methods=['GET', 'POST'])
def remove_card(index):
    try:
        if request.method == 'POST':
            del db[index]
            return redirect(url_for('welcome'))
        else:
            return render_template("remove_card.html", card=db[index])
    except IndexError:
        abort(404)
