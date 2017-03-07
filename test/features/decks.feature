Feature: Retrieving decks of flashcards

Scenario: Retrieve a list of a user's flashcard decks
  Given there are decks in the datastore
  When I retrieve the decks by 'user01'
  Then I should get a '200' response
  And I should get the following data:
    |name                     | id |
    |Python Fundamentals      | 1  |
    |JavaScript Fundamentals  | 2  |
