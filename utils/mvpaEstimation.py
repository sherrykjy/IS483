from flask import Flask, request, jsonify
from flask_cors import CORS
import os, sys
import requests
from invokes import invoke_http
from os import environ
from datetime import datetime

app = Flask(__name__)
CORS(app)

strava_URL = "http://localhost:5020"


# Calculate weekly MVPA based on speed of activities
@app.route('/estimate_mvpa', methods=['GET'])
def estimate_mvpa():
        try:
            result = processStravaInformation()
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
    
    
def processStravaInformation():
    
    # Log into Strava
    connect_result = invoke_http(f"{strava_URL}/connect", method='GET')
    

    activities = invoke_http(f"{strava_URL}/activities", method='GET')["data"]

    # Get all activities within a week
    current_week = datetime.date(datetime.now()).isocalendar()[1]
    weekly_distance = 0
    weekly_time = 0
    
    to_return = {
        "weekly_met": 0,
        "weekly_time_lapse": 0,
        "daily_time_lapse": 0,
        "monthly_top_activity": ""
    }
    
    activity_dict = {}
    
    for activity in activities:
        # check if it is within current month:
        if datetime.strptime(activity["start_date_local"], "%Y-%m-%dT%H:%M:%SZ").month == datetime.now().month:
            # initalise top activity
            if activity["sport_type"] not in activity_dict:
                activity_dict[activity["sport_type"]] = 1
            else: 
                activity_dict[activity["sport_type"]] += 1
                
            if datetime.strptime(activity["start_date_local"], "%Y-%m-%dT%H:%M:%SZ").isocalendar()[1] == current_week:
                weekly_distance += activity["distance"]
                weekly_time += activity["elapsed_time"]
                
                if datetime.strptime(activity["start_date_local"], "%Y-%m-%dT%H:%M:%SZ") == datetime.now().date():
                    daily_met = ((activity["distance"]/activity["elapsed_time"])/ 0.2) + 3.5
                    
                    if daily_met >= 3:
                        to_return["daily_time_lapse"] = round(activity["elapsed_time"]/60, 0)
                        
        else:
            break
            
    weekly_speed_in_m_per_s = weekly_distance/weekly_time
    to_return["weekly_met"] = (weekly_speed_in_m_per_s / 0.2) + 3.5
    to_return["weekly_time_lapse"] = round(weekly_time/60,0)
    
    res = [key for key in activity_dict if all(activity_dict[temp] <= activity_dict[key] for temp in activity_dict)]
    
    to_return["monthly_top_activity"] = res
    
    print(to_return)
    
    return to_return
    
if __name__ == "__main__":
    app.run(port=5009, debug=True)
    
    