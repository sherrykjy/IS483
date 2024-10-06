# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import os, sys
# import requests
# from invokes import invoke_http
# from os import environ
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

# app = Flask(__name__)
# CORS(app)

# strava_URL = "http://localhost:5020"


# # Calculate weekly MVPA based on speed of activities
# @app.route('/estimate_mvpa', methods=['GET'])
# def estimate_mvpa():
#         try:
#             result = processStravaInformation()
#             return jsonify(result), result['code']
        
#         except Exception as e:
#             exc_type, exc_obj, exc_tb = sys.exc_info()
#             fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#             ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
#             print(ex_str)
            
#             return jsonify({
#                 "code": 500,
#                 "message": "user_login.py internal error: " + ex_str
#             }), 500
    
    
# def processStravaInformation():
    
#     # Log into Strava
#     connect_result = invoke_http(f"{strava_URL}/connect", method='GET')
    
#     print(connect_result)
#     # Get all activities
#     activities = invoke_http(f"{strava_URL}/activities", method='GET')
#     print(2)
#     # Get all activities within a week
#     current_week = datetime.date(datetime.now()).isocalendar()[1]
#     distance = 0
#     time = 0
    
#     for activity in activities:
#         print(activities)
#         if datetime.strptime(activity["start_date_local"], "%Y-%m-%dT%H:%M:%SZ").isocalendar()[1] == 39:
#             distance += activity["distance"]
#             time += activity["elapsed_time"]
#         else:
#             break
            
#     weekly_speed_in_m_per_s = distance/time
#     met = (weekly_speed_in_m_per_s / 0.2) + 3.5
    
#     return {
#         "code": 200,
#         "met": met
#     }
    
# if __name__ == "__main__":
#     app.run(port=5009, debug=True)
# ______________________________________   
from flask import Flask, request, jsonify
from flask_cors import CORS
import os, sys
import requests
from invokes import invoke_http
from os import environ
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
CORS(app)

class strava_users(db.Model):
    __tablename__ = 'strava_users'
    
    id = db.Column(db.Integer, primary_key=True)
    strava_id = db.Column(db.String(50), unique=True, nullable=False)
    access_token = db.Column(db.String(200), nullable=False)
    refresh_token = db.Column(db.String(200), nullable=False)
    expires_at = db.Column(db.Integer, nullable=False)

    def __init__(self, id, strava_id, access_token, refresh_token, expires_at):
        self.id = id
        self.strava_id = strava_id
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expires_at = expires_at

    def json(self):
        return {
            "id": self.id,
            "strava_id": self.strava_id,
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
            "expires_at": self.expires_at
        }

strava_URL = "http://localhost:5020"

# Calculate weekly MVPA based on speed of activities
@app.route('/estimate_mvpa', methods=['GET'])
def estimate_mvpa():
    try:
        # Step 1: Fetch user data from the database
        user = strava_users.query.first()  # Adjust this query as necessary

        if not user:
            return jsonify({"code": 404, "message": "User not found"}), 404

        # Step 2: Check if the token has expired, refresh if necessary
        if user.expires_at < time.time():
            user = refresh_access_token(user)

        # Step 3: Call the Strava API to get activities
        result = processStravaInformation(user.access_token)
        return jsonify(result), result['code']
        
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
        print(ex_str)

        return jsonify({
            "code": 500,
            "message": "Internal error: " + ex_str
        }), 500

# Fetch activities from Strava using the user's access token
def processStravaInformation(access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    activities_response = requests.get(f'{strava_URL}/activities', headers=headers)
    
    if activities_response.status_code != 200:
        raise Exception(f"Failed to fetch activities: {activities_response.json()['error']}")

    activities = activities_response.json()

    # Process activities (filter by current week)
    current_week = datetime.now().isocalendar()[1]
    distance = 0
    time_spent = 0
    
    for activity in activities:
        activity_week = datetime.strptime(activity["start_date_local"], "%Y-%m-%dT%H:%M:%SZ").isocalendar()[1]
        
        if activity_week == current_week:
            distance += activity["distance"]
            time_spent += activity["elapsed_time"]

    if time_spent == 0:
        return {
            "code": 400,
            "message": "No activities found for the current week."
        }

    weekly_speed_in_m_per_s = distance / time_spent
    met = (weekly_speed_in_m_per_s / 0.2) + 3.5

    return {
        "code": 200,
        "met": met
    }

# Helper function to refresh the access token
def refresh_access_token(user):
    token_response = requests.post(
        TOKEN_URL,
        data={
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'grant_type': 'refresh_token',
            'refresh_token': user.refresh_token,
        }
    )
    
    new_token_data = token_response.json()
    user.access_token = new_token_data['access_token']
    user.refresh_token = new_token_data['refresh_token']
    user.expires_at = new_token_data['expires_at']
    
    db.session.commit()
    
    return user

if __name__ == "__main__":
    app.run(port=5009, debug=True)