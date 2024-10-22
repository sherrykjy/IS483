from flask import Flask, request, jsonify
from flask_cors import CORS
import os, sys
from datetime import datetime, timedelta
import requests
from invokes import invoke_http
from os import environ

app = Flask(__name__)
CORS(app)

userCard_URL = "http://localhost:5006/usercard"
trade_URL = "http://localhost:5013/trade"

@app.route("/create_trade", methods=['POST'])
def create_new_trade():
    if request.is_json:
        try:
            trade_details = request.get_json()
            print("\nReceived trade information in JSON:", trade_details)
            result = processCardTrades(trade_details)
            return jsonify(result), result['code']
        
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)
            
            return jsonify({
                "code": 500,
                "message": "create_trade.py internal error: " + ex_str
            }), 500
        
    else:
        return jsonify({
            "code": 400,
            "message": "JSON object not found"
        }), 400
            
def processCardTrades(trade_details):
    user_id = trade_details["user_id"]
    card_one_id = trade_details["card_one_id"]
    card_two_id = trade_details["card_two_id"]

    try: 
        # Check if user has an existing trade (within the last 24 hours)
        trade_response = invoke_http(f"{trade_URL}/user/{user_id}", method='GET')
        print(trade_response)
        if trade_response["code"] == 200:
            return {"code": 400, "message": "User just traded within the last 24 hours"}
        
        # Get user's cards
        user_cards_response = invoke_http(f"{userCard_URL}/user/{user_id}", method='GET')
        if user_cards_response["code"] != 200:
            return {"code": 404, "message": "User has no cards"}
        user_cards = user_cards_response["data"]["cards"]

        # Check whether user has the card being offered & whether user already has the card being requested
        card_one_found = False
        card_two_found = False
        for card in user_cards:
            if card["card_id"] == card_one_id:
                card_one_found = True
            if card["card_id"] == card_two_id:
                card_two_found = True
        if not card_one_found:
            return {"code": 400, "message": "User does not have card being offered"}
        if card_two_found:
            return {"code": 400, "message": "User already has the card being requested. User should not have duplicate cards."}

        # Create a new trade
        new_trade_response = invoke_http(f"{trade_URL}", method='POST', json=trade_details)
        print("\nCreate trade response:", new_trade_response)
        return new_trade_response
    
    except Exception as e:
        return {"code": 500, "message": str(e)}

        
if __name__ == '__main__':
    app.run(port=5014, debug=True)
