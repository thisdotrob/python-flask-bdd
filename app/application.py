from flask import Flask

app = Flask(__name__)

@app.route("/decks/<author>")
def decks(author):
    return "OK"
