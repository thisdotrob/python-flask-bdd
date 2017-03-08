from flask import Flask

app = Flask(__name__)

@app.route("/decks/<author>")
def view_decks(author):
    return "OK"
