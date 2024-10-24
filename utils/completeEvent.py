from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os, sys
import requests
from invokes import invoke_http
from os import environ
import hashlib
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/healthpal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS' ] = False

db = SQLAlchemy(app)
CORS(app)

userURL = "http://localhost:5001/user"
eventURL = "http://localhost:5002/event"
cardURL = "http://localhost:5003/card"
healthCoinURL = "http://localhost:5004/healthcoins"
userCardURL = "http://localhost:5006/usercard"
userEventURL = "http://localhost:5007/userevent"

@app.route('/attendance/<int:event_id>', methods=['POST'])
def process_attendance(event_id):
    if request.json:
        try:
            user_event_ids = request.json.get('user_event_ids', [])
            user_ids = request.json.get('user_ids', [])
            print("user event ids received:", user_event_ids)
            print("user ids received:", user_ids)

            if not user_event_ids or not user_ids:
                return jsonify({"code": 400, "error": "user_event_ids and user_ids are required"}), 400

            # 1. Check if event exists
            event_response = invoke_http(f"{eventURL}/{event_id}", method='GET')
            if event_response["code"] != 200:
                return jsonify({
                    "code": 404,
                    "message": "Event not found"
                }), 404
            event_data = event_response["data"]
            event_point = event_data["event_point"]

            # 2. Check if there is a special collectible to be added
            special_collectible = False
            card_response = invoke_http(f"{cardURL}/event/{event_id}", method='GET')
            print(card_response)
            if card_response["code"] == 200:
                card_data = card_response["data"][0]
                card_id = card_data["card_id"]
                special_collectible = True

            # # 3. Update complete status for users
            for user_event_id in user_event_ids:
                # check if user_event exists
                user_event_check = invoke_http(f"{userEventURL}/{user_event_id}", method='GET')
                if user_event_check["code"] != 200:
                    return jsonify({
                        "code": 404,
                        "message": "User Event not found"
                    }), 404
                
                # update user_event to completed
                user_event_response = invoke_http(f"{userEventURL}/{user_event_id}", method='PATCH', json={"completed": True})
                print(user_event_response)
                if user_event_response["code"] != 200:
                    raise Exception("Error updating completion status for User Event")

            # 4. Add HealthCoins for users
            for user_id in user_ids:
                # 4.1. Update HealthCoins in User
                # check if user exists
                user_check = invoke_http(f"{userURL}/id/{user_id}", method='GET')
                if user_check["code"] != 200:
                    return jsonify({
                        "code": 404,
                        "message": "User not found"
                    }), 404
                user_data = user_check["data"]
                
                # update total_point for user
                user_response = invoke_http(f"{userURL}/id/{user_id}", method='PATCH', json={"total_point": user_data["total_point"] + event_point})
                print(user_response)
                if user_response["code"] != 200:
                    raise Exception("Error updating HealthCoins for User")

                # 4.2. Add HealthCoins record in Health_Coin
                healthCoin_response = invoke_http(healthCoinURL, method='POST', json={"user_id": user_id, "points_earned": event_point, "earned_date": str(datetime.now()), "source": "Event"})
                print(healthCoin_response)
                if healthCoin_response["code"] != 201:
                    raise Exception("Error adding HealthCoins record")

                # 5. Add collectibles for users (in user_cards)
                if (special_collectible):
                    usercard_check = invoke_http(f"{userCardURL}/user/{user_id}/card/{card_id}", method='GET')
                    # add card for user if not exists
                    if usercard_check["code"] != 200:
                        usercard_response = invoke_http(userCardURL, method='POST', json={"user_id": user_id, "card_id": card_id, "earned_date": str(datetime.now())})
                        if usercard_response["code"] != 201:
                            raise Exception("Error adding event collectible for user")
                    else:
                        print("User already has this collectible")
            
            db.session.commit()

            return jsonify({
                "code": 200,
                "message": "Attendance recorded"
            })
        
        except Exception as e:
            db.session.rollback()
            return jsonify({
                "code": 500,
                "message": f"An error occurred: {str(e)}"
            }), 500
    
    return jsonify({
        "code": 400, 
        "error": "Invalid JSON input"
    }), 400

if __name__ == '__main__':
    app.run(port=5016, debug=True)