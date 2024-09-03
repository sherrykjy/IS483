from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from .user import User
from .card import Card  

from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/usercard'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS' ] = False

db = SQLAlchemy()

class UserCard(db.Model):
    __tablename__ = 'user_card'
    
    user_card_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey('card.card_id'), nullable=False)
    earned_date = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __init__(self, user_id, card_id, earned_date=None):
        self.user_id = user_id
        self.card_id = card_id
        self.earned_date = datetime.now()

    def json(self):
        return {
            "user_card_id": self.user_card_id,
            "user_id": self.user_id,
            "card_id": self.card_id,
            "earned_date": self.earned_date.isoformat()
        }

if __name__ == '__main__':
    app.run(port=5000, debug=True)