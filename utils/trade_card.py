from flask import Flask, request, jsonify
from flask_cors import CORS
import os, sys
import requests
from invokes import invoke_http
from os import environ
import hashlib

app = Flask(__name__)

userCard_URL = "http://localhost:5006/usercard"
trade_URL = "http://localhost:5012/trade"

@app.route("/trade_card", methods=['POST'])
def trade_card():
    if request.is_json:
        try:
            trade_details = request.get_json()
            print("\nReceived login information in JSON:", trade_details)
            result = processCardTrade(trade_details)
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
            
def processCardTrade(trade_details):
    
    # 1. Remove Card1 from User1 - Card 1 already exist in trade details
    trade_id = trade_details['trade_id']
    trader_one = trade_details['trader_one_id']
    card_in_market = trade_details['card_one_id']
    card_one_name = trade_details['card_one_name']
    
    trader_two = trade_details['trader_two_id']
    card_in_deck = trade_details['card_two_id']
    card_two_name = trade_details['card_two_name']
    
    card_remove_result = invoke_http(f"{userCard_URL}/{card_in_market}", method='DELETE')
    
    # 2. Add Card1 to User2
    card_information = 0
    card_add_result = invoke_http(f"{userCard_URL}/{card_in_market}", method='POST', json=card_information)
    
    # 3. Remove Card2 from User2
    card_remove_result = invoke_http(f"{userCard_URL}/{card_in_deck}", method='DELETE')
    
    # 4. Add Card2 to User1
    card_information = 0
    
    
    card_add_result = invoke_http(f"{userCard_URL}/{card_in_deck}", method='POST', json=card_information)
    
    # 5. Change traded to True
    trade_result = invoke_http(f"{trade_URL}/{trade_id}", method='POST')