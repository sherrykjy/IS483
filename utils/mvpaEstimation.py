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
    
    print(connect_result)
    # Get all activities
    activities = invoke_http(f"{strava_URL}/activities", method='GET')
    print(2)
    # Get all activities within a week
    current_week = datetime.date(datetime.now()).isocalendar()[1]
    distance = 0
    time = 0
    
    for activity in activities:
        print(activities)
        if datetime.strptime(activity["start_date_local"], "%Y-%m-%dT%H:%M:%SZ").isocalendar()[1] == 39:
            distance += activity["distance"]
            time += activity["elapsed_time"]
        else:
            break
            
    weekly_speed_in_m_per_s = distance/time
    met = (weekly_speed_in_m_per_s / 0.2) + 3.5
    
    return {
        "code": 200,
        "met": met
    }
    
if __name__ == "__main__":
    app.run(port=5012, debug=True)
    
    