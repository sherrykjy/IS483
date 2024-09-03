from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from .user import User

from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/healthpoints'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS' ] = False

db = SQLAlchemy()

class HealthPoints(db.Model):
    __tablename__ = 'health_points'
    
    points_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    points_earned = db.Column(db.Integer, nullable=False)
    earned_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    source = db.Column(db.String(64), nullable=False)

    def __init__(self, user_id, points_earned, source, earned_date=None):
        self.user_id = user_id
        self.points_earned = points_earned
        self.earned_date = datetime.now()
        self.source = source

    def json(self):
        return {
            "points_id": self.points_id,
            "user_id": self.user_id,
            "points_earned": self.points_earned,
            "earned_date": self.earned_date.isoformat(),
            "source": self.source
        }

if __name__ == '__main__':
    app.run(port=5000, debug=True)