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

@app.route("/trade_card", methods=['GET'])
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
            
def processCardTrades():
    trades_response = invoke_http(f"{trade_URL}s", method='GET')
    trades = trades_response.get("data", [])
    
    updated_trades = []
    for trade in trades:
        # Convert trade_date from ISO format and compare with current time
        trade_date = datetime.fromisoformat(trade["trade_date"])
        if trade_date + timedelta(hours=24) > datetime.now():
            trade_id = trade["trade_id"]
            trade_result = invoke_http(f"{trade_URL}/{trade_id}", method='DELETE')
            
            if trade_result["code"] == 200:
                print(f"Trade with ID {trade_id} successfully deleted.")
            else:
                print(f"Failed to delete trade with ID {trade_id}")
        else:
            # Keep the trades that are still within the 24-hour window
            updated_trades.append(trade)
    
    # Return the remaining trades
    return {"code": 200, "data": updated_trades}

        
if __name__ == '__main__':
    app.run(port=5012, debug=True)
