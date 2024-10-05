from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost:3306/healthpal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

# Streak model
class Streak(db.Model):
    __tablename__ = 'streak'
    
    streak_id = db.Column(db.Integer, primary_key=True)
    goal_id = db.Column(db.Integer, nullable=False)
    week_started = db.Column(db.Integer, nullable=False)
    week_current = db.Column(db.Integer, nullable=False)
    streak_count = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, streak_id, goal_id, week_started, week_current, streak_count=1):
        self.streak_id = streak_id
        self.goal_id = goal_id
        self.week_started = week_started
        self.week_current = week_current
        self.streak_count = streak_count

    def json(self):
        return {
            "streak_id": self.streak_id,
            "goal_id": self.goal_id,
            "week_started": self.week_started,
            "week_current": self.week_current,
            "streak_count": self.streak_count,
        }

# Create a new streak
@app.route('/streak', methods=['POST'])
def create_streak():
    data = request.json
    new_streak = Streak(
        goal_id=data.get('goal_id'),
        week_started=data.get('week_started'),
        week_current=data.get('week_current', None),
        streak_count=data.get('streak_count', 1)
    )
    try:
        db.session.add(new_streak)
        db.session.commit()
        return jsonify(new_streak.json()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Get all streaks for a goal
@app.route('/streaks/<int:goal_id>', methods=['GET'])
def get_streaks(goal_id):
    streaks = Streak.query.filter_by(goal_id=goal_id).all()
    if streaks:
        return jsonify([streak.json() for streak in streaks]), 200
    return jsonify({"error": "No streaks found for this goal"}), 404

# Get a streak by ID
@app.route('/streak/<int:streak_id>', methods=['GET'])
def get_streak(streak_id):
    streak = Streak.query.get(streak_id)
    if streak:
        return jsonify(streak.json()), 200
    return jsonify({"error": "Streak not found"}), 404

@app.route('/streak/<int:streak_id>', methods=['PUT'])
def update_streak(streak_id):
    streak = Streak.query.get(streak_id)
    print(streak) 
    if streak:
        data = request.get_json()
        print(data)
        try:
            # Corrected: Removed commas that caused single-element tuple assignment
            streak.streak_id = data.get('streak_id')
            streak.goal_id = data.get('goal_id')
            streak.week_started = data.get('week_started')
            streak.week_current = data.get('week_current')
            streak.streak_count = data.get('streak_count')
            
            db.session.commit()
            return jsonify({"code": 200, "data": streak.json()})
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
        
    return jsonify({"error": "Streak not found"}), 404

# Delete a streak by ID
@app.route('/streak/<int:streak_id>', methods=['DELETE'])
def delete_streak(streak_id):
    streak = Streak.query.get(streak_id)
    if streak:
        try:
            db.session.delete(streak)
            db.session.commit()
            return jsonify({"message": "Streak deleted"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    return jsonify({"error": "Streak not found"}), 404

if __name__ == '__main__':
    app.run(port=5010, debug=True)
