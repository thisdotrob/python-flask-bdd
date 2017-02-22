from flask_sqlalchemy import SQLAlchemy
from app.application import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/codecards'
db = SQLAlchemy(app)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

class Deck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship('Author', backref='decks')

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String)
    answer = db.Column(db.String)
    deck_id = db.Column(db.Integer, db.ForeignKey('deck.id'))
    deck = db.relationship('Deck', backref='cards')
