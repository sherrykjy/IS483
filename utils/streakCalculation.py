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

goal_URL = "http://localhost:5011/goal"
streak_URL = "http://localhost:5010/streak"
mvp_URL = "http://localhost:5021/estimate_mvpa"
coin_URL = "http://localhost:5004/healthcoins"
user_URL = "http://localhost:5001/user"

@app.route('/update_streak', methods=['GET'])
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
    print("haha1", met_result)
    
    # Get Streak 
    
    estimated_met = met_result["weekly_met"]
    streak_result = invoke_http(f"{streak_URL}/{user_id}")
    print("haha2", streak_result)

    coinEarned = 0
    streak_json = {}
    
    if streak_result["week_current"] + 1 == datetime.date(datetime.now()).isocalendar()[1]:
        if (estimated_met >= 3) and (goal_result["target"]):
            streak_count = streak_result["streak_count"] + 1
            streak_json = {
                "streak_id": streak_result["streak_id"],
                "goal_id": streak_result["goal_id"],
                "week_started": streak_result["week_started"],
                "week_current": datetime.date(datetime.now()).isocalendar()[1],
                "streak_count": streak_count
                }
            coinEarned = 10 + streak_count * 5
            
    elif streak_result["week_current"] == datetime.date(datetime.now()).isocalendar()[1]:
            streak_json = {
                "streak_id": streak_result["streak_id"],
                "goal_id": streak_result["goal_id"],
                "week_started": streak_result["week_started"],
                "week_current": streak_result["week_current"],
                "streak_count": streak_result["streak_count"]
                }
            coinEarned = 0
            
    else:
        streak_json = {
            "streak_id": streak_result["streak_id"],
            "goal_id": streak_result["goal_id"],
            "week_started": datetime.date(datetime.now()).isocalendar()[1],
            "week_current": datetime.date(datetime.now()).isocalendar()[1],
            "streak_count": 1
            }
        
        coinEarned = 10

    streak_update_result = invoke_http(f"{streak_URL}/{streak_id}", method='PUT', json=streak_json)
    print(streak_update_result)

    # create a new coin transaction
    coin_json = {
        "user_id": user_id,
        "points_earned": coinEarned,
        "earned_date": datetime.now().isoformat(),
        "source": "streak"
    }
    coin_result = invoke_http(f"{coin_URL}", method='POST', json=coin_json)
    print(coin_result)
    
    user_result = invoke_http(f"{user_URL}/id/{user_id}", method='GET')
    user_email = user_result["data"]["email"]
    user_total_coin = user_result["data"]["total_point"]
    
    print(user_total_coin + coinEarned)
    # update user's coins
    user_json = {
        "total_point": user_total_coin + coinEarned
    }
    
    user_result = invoke_http(f"{user_URL}/{user_email}", method='PATCH', json=user_json)

    return {"code": streak_update_result}

if __name__ == '__main__':
    app.run(port=5030, debug=True)
        