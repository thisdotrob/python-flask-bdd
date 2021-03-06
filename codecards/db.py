from flask_sqlalchemy import SQLAlchemy

from codecards.application import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/codecards'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
