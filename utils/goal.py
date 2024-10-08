from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/healthpal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Goal(db.Model):
    __tablename__ = 'goal'
    
    goal_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    goal_description = db.Column(db.String(256), nullable=False)
    tier = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    target = db.Column(db.Integer, nullable = False)

    def __init__(self, user_id, goal_description, tier, target):
        self.user_id = user_id
        self.goal_description = goal_description
        self.tier = tier
        self.date_created = datetime.now()
        self.date_completed = target

    def json(self):
        return {
            "goal_id": self.goal_id,
            "user_id": self.user_id,
            "goal_description": self.goal_description,
            "tier": self.tier,
            "date_created": self.date_created.isoformat(),
            "target": self.target,
        }

# Create a new goal
@app.route('/goal', methods=['POST'])
def create_goal():
    data = request.json
    new_goal = Goal(
        user_id=data.get('user_id'),
        goal_description=data.get('goal_description'),
        tier=data.get('tier'),
        completed=data.get('completed', False),
        target=data.get('target')
    )
    try:
        db.session.add(new_goal)
        db.session.commit()
        return jsonify(new_goal.json()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Get all goals for a user
@app.route('/goals/<int:user_id>', methods=['GET'])
def get_goals(user_id):
    goals = Goal.query.filter_by(user_id=user_id).all()
    if goals:
        return jsonify([goal.json() for goal in goals]), 200
    return jsonify({"error": "No goals found for this user"}), 404

# Get a goal by ID
@app.route('/goal/<int:goal_id>', methods=['GET'])
def get_goal(goal_id):
    goal = Goal.query.get(goal_id)
    if goal:
        return jsonify(goal.json()), 200
    return jsonify({"error": "Goal not found"}), 404

# Update a goal by ID
@app.route('/goal/<int:goal_id>', methods=['PUT'])
def update_goal(goal_id):
    goal = Goal.query.get(goal_id)
    if goal:
        data = request.json
        goal.goal_description = data.get('goal_description', goal.goal_description)
        goal.tier = data.get('tier', goal.tier)
        goal.target = data.get('target', goal.target)
        try:
            db.session.commit()
            return jsonify(goal.json()), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
        
    return jsonify({"error": "Goal not found"}), 404

# Delete a goal by ID
@app.route('/goal/<int:goal_id>', methods=['DELETE'])
def delete_goal(goal_id):
    goal = Goal.query.get(goal_id)
    if goal:
        try:
            db.session.delete(goal)
            db.session.commit()
            return jsonify({"message": "Goal deleted"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    return jsonify({"error": "Goal not found"}), 404

if __name__ == '__main__':
    app.run(port=5011, debug=True)
