from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
# from .user import User
from flask_cors import CORS, cross_origin

from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/healthpal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS' ] = False

db = SQLAlchemy(app)
CORS(app)

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

# Create a new HealthPoints entry
@app.route('/healthpoints', methods=['POST'])
def create_health_points():
    data = request.json
    new_health_points = HealthPoints(
        user_id=data.get('user_id'),
        points_earned=data.get('points_earned'),
        source=data.get('source')
    )
    try:
        db.session.add(new_health_points)
        db.session.commit()
        return jsonify(new_health_points.json()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Get all HealthPoints entries
@app.route('/healthpoints', methods=['GET'])
def get_health_points():
    health_points_list = HealthPoints.query.all()
    return jsonify([hp.json() for hp in health_points_list]), 200

# Get a HealthPoints entry by ID
@app.route('/healthpoints/<int:points_id>', methods=['GET'])
def get_health_points_by_id(points_id):
    health_points = HealthPoints.query.get(points_id)
    if health_points:
        return jsonify(health_points.json()), 200
    return jsonify({"error": "HealthPoints entry not found"}), 404

# Update a HealthPoints entry by ID
@app.route('/healthpoints/<int:points_id>', methods=['PUT'])
def update_health_points(points_id):
    health_points = HealthPoints.query.get(points_id)
    if health_points:
        data = request.json
        health_points.user_id = data.get('user_id', health_points.user_id)
        health_points.points_earned = data.get('points_earned', health_points.points_earned)
        health_points.earned_date = data.get('earned_date', health_points.earned_date)
        health_points.source = data.get('source', health_points.source)
        
        try:
            db.session.commit()
            return jsonify(health_points.json()), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    return jsonify({"error": "HealthPoints entry not found"}), 404

# Delete a HealthPoints entry by ID
@app.route('/healthpoints/<int:points_id>', methods=['DELETE'])
def delete_health_points(points_id):
    health_points = HealthPoints.query.get(points_id)
    if health_points:
        try:
            db.session.delete(health_points)
            db.session.commit()
            return jsonify({"message": "HealthPoints entry deleted"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    return jsonify({"error": "HealthPoints entry not found"}), 404

if __name__ == '__main__':
    app.run(port=5004, debug=True)