from flask import Flask, request, jsonify
from flask_cors import CORS
import os, sys
import requests
from invokes import invoke_http
from os import environ
import hashlib
from datetime import datetime

app = Flask(__name__)
CORS(app)

goal_URL = "http://localhost:5008/goal"
streak_URL = "http://localhost:5010/streak"
mvp_URL = "http://localhost:5020/estimate_mvpa"

@app.route('/update_streak/<int:user_id>/<int:goal_id>', methods=['GET'])
def update_streak_if_mvpa():
    if request.is_json:
        try:
            streak_information = request.get_json()
            print("\nReceived login information in JSON:", streak_information)
            result = processStreakInformation(streak_information)
            return jsonify(result), result['code']
        
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)
            
            return jsonify({
                "code": 500,
                "message": "user_login.py internal error: " + ex_str
            }), 500

def processStreakInformation(streak_information):
    
    goal_id = streak_information['goal_id']
    user_id = streak_information['user_id']
    streak_id = streak_information['streak_id']
    
    # Get Goal of User
    goal_result = invoke_http(f"{goal_URL}/{user_id}", method='GET')
    
    # Get Estimated MET
    met_result = invoke_http(f"{mvp_URL}")
    # Get Streak 
    
    estimated_met = met_result["met"]
    streak_json= None
    
    if (estimated_met >= 3) and (goal_result["target"]):
        streak_result = invoke_http(f"{streak_URL}/{user_id}")
        
        if streak_result["week_current"] + 1 == datetime.date(datetime.now()).isocalendar()[1]:
            streak_json = {
                "streak_id": streak_result.streak_id,
                "goal_id": streak_result.goal_id,
                "week_started": streak_result.week_started,
                "week_current": datetime.date(datetime.now()).isocalendar()[1],
                "streak_count": streak_result.streak_count + 1
                }
    else:
        streak_json = {
            "streak_id": streak_result.streak_id,
            "goal_id": streak_result.goal_id,
            "week_started": datetime.date(datetime.now()).isocalendar()[1],
            "week_current": datetime.date(datetime.now()).isocalendar()[1],
            "streak_count": 1
            }
        
    streak_update_result = invoke_http(f"{streak_URL}/{streak_id}", method='PUT', json=streak_json)
    
    return streak_update_result
            
        