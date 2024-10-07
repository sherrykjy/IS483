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

userCard_URL = "http://localhost:5006/usercard"
trade_URL = "http://localhost:5013/trade"

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
                "message": "trade_card.py internal error: " + ex_str
            }), 500
            
def processCardTrade(trade_details):
    # 1. Remove Card1 from User1 - Card 1 already exist in trade details
    trade_id = trade_details['trade_id']
    user_card_id_one = trade_details['user_card_id_one']
    user_id_one = trade_details['user_id_one']
    card_id_one = trade_details['card_id_one']
    
    user_card_id_two = trade_details['user_card_id_two']
    user_id_two = trade_details['user_id_two']
    card_id_two = trade_details['card_id_two']
    card_remove_result = invoke_http(f"{userCard_URL}/{user_card_id_one}", method='DELETE')
    
    if card_remove_result['code'] == 404: 
        print("failed to remove card")
    
    else:
        print(card_remove_result)
    
    # 2. Add Card1 to User2
    card_information_one = {
        "user_card_id": user_card_id_one,
        "user_id": user_id_two,
        "card_id": card_id_one,
        "earned_date": datetime.now().isoformat()
    }
    card_add_result = invoke_http(userCard_URL, method='POST', json=card_information_one)
    # print(card_add_result)
    if card_add_result['code'] == 201:
        print(card_add_result)
        
    else:
        print("failed to add card 1 to user 2")
    
    # 3. Remove Card2 from User2
    card_remove_result = invoke_http(f"{userCard_URL}/{user_card_id_two}", method='DELETE')
    
    if card_remove_result['code'] == 200: 
        print(card_remove_result)
    
    else:
        print("failed to remove card")

    # 4. Add Card2 to User1
    card_information_two = {
        "user_card_id": user_card_id_two,
        "user_id": user_id_one,
        "card_id": card_id_two,
        "earned_date": datetime.now().isoformat()
    }
    
    card_add_result = invoke_http(userCard_URL, method='POST', json=card_information_two)

    if card_add_result['code'] == 201:
        print(card_add_result)
        
    else:
        print("failed to add card 2 to user 1")

    # # if card_add_result['code'] == 404:
    # #     print("failed to add card to user 1")
        
    # # else:
    # print(card_add_result)
    
    # 5. Change traded to True
    trade_result = invoke_http(f"{trade_URL}/{trade_id}", method='DELETE')
    print(trade_result)
    
    if trade_result['code'] != 200:
        print("trade failed")
    
    return trade_result
        
if __name__ == '__main__':
    app.run(port=5015, debug=True)