from flask import Flask, request, jsonify
from flask_cors import CORS
import os, sys
from datetime import datetime, timedelta
import requests
from invokes import invoke_http
from os import environ

app = Flask(__name__)
CORS(app)

trade_URL = "http://localhost:5013/trade"

@app.route("/active_trades", methods=['GET'])
def get_trades():
    # if request.is_json:
    try:
        # trade_details = request.get_json()
        # print("\nReceived trade information in JSON:", trade_details)
        result = getActiveTrades()
        return jsonify(result), result['code']
    
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
        print(ex_str)
        
        return jsonify({
            "code": 500,
            "message": "get_trades.py internal error: " + ex_str
        }), 500
            
def getActiveTrades():
    try:
        trades_response = invoke_http(f"{trade_URL}s", method='GET')
        trades = trades_response.get("data", [])
        print(trades)
        
        updated_trades = []
        for trade in trades:
            # Convert trade_date from ISO format and compare with current time
            trade_date = datetime.fromisoformat(trade["trade_date"])
            # If trade_date + 24 hours is less than current time (in the past), delete the trade
            if trade_date + timedelta(hours=24) < datetime.now():
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
    
    except Exception as e:
        return {"code": 500, "message": str(e)}

        
if __name__ == '__main__':
    app.run(port=5012, debug=True)
