from aloe import before, step, world
from nose.tools import assert_equals
from codecards.application import app
from codecards.db import db
from codecards.models.Author import Author
from codecards.models.Deck import Deck
from codecards.models.Card import Card
import json

@before.all
def before_all():
    db.drop_all()
    db.create_all()
    world.app = app.test_client()

@step(r'there are decks in the datastore')
def given_there_are_decks_in_the_datastore(self):
    author = Author(name='user01')
    deck_a = Deck(name='Python Fundamentals', author=author)
    deck_b = Deck(name='JavaScript Fundamentals', author=author)
    db.session.add(author)
    db.session.add(deck_a)
    db.session.add(deck_b)
    db.session.commit()

@step(r'I retrieve the decks by \'(.*)\'')
def when_i_retrieve_the_decks_by_author(self, author_name):
    world.response = world.app.get('/decks/{}'.format(author_name))

@step(r'I should get a \'(.*)\' response')
def then_i_should_get_a_status_code_response(self, expected_status_code):
    assert_equals(world.response.status_code, int(expected_status_code))

@step(r'I should get the following data')
def then_i_should_get_the_following_data(self):
    for data, expected in zip(json.loads(world.response.data), self.hashes):
        assert_equals(data, expected)
