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
def get_trades():
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
                "message": "trade_card.py internal error: " + ex_str
            }), 500
            
def processCardTrades(user_details):
    user_id = user_details["user_id"]
    trade_response = invoke_http(f"{trade_URL}/{user_id}", method='GET', json=user_details)

    if trade_response["code"] == 200:
        return {"code": 404, "message": "User just traded within the last 24 hours"}
    
    # Return the remaining trades
    new_trade_response = invoke_http(f"{trade_URL}", method='POST')
    return new_trade_response

        
if __name__ == '__main__':
    app.run(port=5015, debug=True)
