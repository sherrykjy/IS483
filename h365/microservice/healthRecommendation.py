from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from .user import User

from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/healthrecommendation'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS' ] = False

db = SQLAlchemy()

class HealthRecommendation(db.Model):
    __tablename__ = 'health_recommendation'
    
    recommendation_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    health_goal = db.Column(db.String(64), nullable=False)
    recommendation_text = db.Column(db.String(64), nullable=False)
    generated_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    progress = db.Column(db.String(64), nullable=False)

    def __init__(self, user_id, health_goal, recommendation_text, progress):
        self.user_id = user_id
        self.health_goal = health_goal
        self.recommendation_text = recommendation_text
        self.generated_date = datetime.utcnow()
        self.progress = progress

    def json(self):
        return {
            "recommendation_id": self.recommendation_id,
            "user_id": self.user_id,
            "health_goal": self.health_goal,
            "recommendation_text": self.recommendation_text,
            "generated_date": self.generated_date.isoformat(),
            "progress": self.progress
        }

if __name__ == '__main__':
    app.run(port=5000, debug=True)