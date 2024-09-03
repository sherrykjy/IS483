from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from .event import Event

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/card'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Card(db.Model):
    __tablename__ = 'card'
    
    card_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    card_type = db.Column(db.String(64), nullable=False)
    points_required = db.Column(db.Integer, nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'), nullable=True)

    def __init__(self, title, card_type, points_required, event_id=None):
        self.title = title
        self.card_type = card_type
        self.points_required = points_required
        self.event_id = event_id

    def json(self):
        return {
            "card_id": self.card_id,
            "title": self.title,
            "card_type": self.card_type,
            "points_required": self.points_required,
            "event_id": self.event_id
        }

# Make sure to initialize the database and create tables
with app.app_context():
    db.create_all()
