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

# Create a new HealthRecommendation entry
@app.route('/healthrecommendation', methods=['POST'])
def create_health_recommendation():
    data = request.json
    new_recommendation = HealthRecommendation(
        user_id=data.get('user_id'),
        health_goal=data.get('health_goal'),
        recommendation_text=data.get('recommendation_text'),
        progress=data.get('progress')
    )
    try:
        db.session.add(new_recommendation)
        db.session.commit()
        return jsonify(new_recommendation.json()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Get all HealthRecommendation entries
@app.route('/healthrecommendation', methods=['GET'])
def get_health_recommendations():
    recommendations_list = HealthRecommendation.query.all()
    return jsonify([rec.json() for rec in recommendations_list]), 200

# Get a HealthRecommendation entry by ID
@app.route('/healthrecommendation/<int:recommendation_id>', methods=['GET'])
def get_health_recommendation_by_id(recommendation_id):
    recommendation = HealthRecommendation.query.get(recommendation_id)
    if recommendation:
        return jsonify(recommendation.json()), 200
    return jsonify({"error": "HealthRecommendation entry not found"}), 404

# Update a HealthRecommendation entry by ID
@app.route('/healthrecommendation/<int:recommendation_id>', methods=['PUT'])
def update_health_recommendation(recommendation_id):
    recommendation = HealthRecommendation.query.get(recommendation_id)
    if recommendation:
        data = request.json
        recommendation.user_id = data.get('user_id', recommendation.user_id)
        recommendation.health_goal = data.get('health_goal', recommendation.health_goal)
        recommendation.recommendation_text = data.get('recommendation_text', recommendation.recommendation_text)
        recommendation.generated_date = data.get('generated_date', recommendation.generated_date)
        recommendation.progress = data.get('progress', recommendation.progress)
        
        try:
            db.session.commit()
            return jsonify(recommendation.json()), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    return jsonify({"error": "HealthRecommendation entry not found"}), 404

# Delete a HealthRecommendation entry by ID
@app.route('/healthrecommendation/<int:recommendation_id>', methods=['DELETE'])
def delete_health_recommendation(recommendation_id):
    recommendation = HealthRecommendation.query.get(recommendation_id)
    if recommendation:
        try:
            db.session.delete(recommendation)
            db.session.commit()
            return jsonify({"message": "HealthRecommendation entry deleted"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    return jsonify({"error": "HealthRecommendation entry not found"}), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)