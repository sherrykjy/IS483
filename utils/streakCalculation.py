from flask import Flask, request, jsonify
from flask_cors import CORS
import os, sys
import requests
from invokes import invoke_http
from os import environ
import hashlib

app = Flask(__name__)
CORS(app)

user_URL = "http://localhost:5001/user"

@app.route('/update_streak_if_mvpa/<int:user_id>/<int:goal_id>/<int:week>', methods=['GET'])
def update_streak_if_mvpa(user_id, goal_id, week):
    # Fetch the goal
    goal = Goal.query.get(goal_id)
    if not goal:
        return jsonify({"error": "Goal not found"}), 404

    # Call the MVPA estimation microservice
    mvpa_response = requests.get(f'http://localhost:5020/estimate_mvpa/{user_id}/{week}')
    if mvpa_response.status_code != 200:
        return jsonify({'error': 'Failed to estimate MVPA'}), 400

    mvpa_data = mvpa_response.json()
    mvpa_minutes = mvpa_data.get('mvpa_minutes', 0)

    # Compare the MVPA with the goal's target
    if mvpa_minutes >= goal.target:
        # Fetch the user's streak for the current goal and week
        streak = Streak.query.filter_by(goal_id=goal_id, week_started=week).first()
        if streak:
            streak.streak_count += 1  # Increment the streak count
            streak.week_current = week
        else:
            # If no streak exists for the goal, create a new one
            streak = Streak(goal_id=goal_id, week_started=week, week_current=week, streak_count=1)

        try:
            db.session.add(streak)
            db.session.commit()
            return jsonify(streak.json()), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    else:
        return jsonify({"message": "MVPA does not meet the target"}), 200
