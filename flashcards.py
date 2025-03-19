from datetime import datetime

from flask import Flask

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to my Flash Cards application!"


@app.route("/time")
def time():
    return f"This page was shown at {datetime.now().time()}"
