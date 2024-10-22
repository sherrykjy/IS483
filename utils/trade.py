from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime, timedelta
from invokes import invoke_http

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/healthpal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

userURL = "http://localhost:5001/user"
cardURL = "http://localhost:5003/card"

class Trade(db.Model):
    __tablename__ = 'trade'
    
    trade_id = db.Column(db.Integer, primary_key=True)
    
    # Trader One
    # user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    # card_one_id = db.Column(db.Integer, db.ForeignKey('card.card_id'), nullable=False)
    user_id = db.Column(db.Integer,  nullable=False)
    card_one_id = db.Column(db.Integer,  nullable=False)
    # card_one_name = db.Column(db.String(255), nullable=False)
    # card_earned_date = db.Column(db.DateTime, nullable=False)
    
    # Trader Two
    # trader_two_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=True)
    card_two_id = db.Column(db.Integer,  nullable=True)
    # card_two_name = db.Column(db.String(255), nullable=True)
    # two_earned_date = db.Column(db.DateTime, nullable=True)

    # Date the trade was initiated
    trade_date = db.Column(db.DateTime, nullable=False)
    
    # traded = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, trade_id, user_id, card_one_id, card_two_id, trade_date):
        self.trade_id = trade_id
        self.user_id = user_id
        self.card_one_id = card_one_id
        # self.card_one_name = card_one_name
        # self.card_earned_date = card_earned_date
        # self.trader_two_id = trader_two_id
        self.card_two_id = card_two_id
        # self.card_two_name = card_two_name
        # self.two_earned_date = two_earned_date
        # self.traded = traded
        self.trade_date = trade_date

    def json(self):
        return {
            "trade_id": self.trade_id,
            "user_id": self.user_id,
            "card_one_id": self.card_one_id,
            # "card_one_name": self.card_one_name,
            # "card_earned_date": self.card_earned_date.isoformat(),
            # "trader_two_id": self.trader_two_id,
            "card_two_id": self.card_two_id,
            # "card_two_name": self.card_two_name,
            # "two_earned_date": self.two_earned_date.isoformat(),
            # "traded": self.traded
            "trade_date": self.trade_date.isoformat()
        }

# Get the next trade_id
def get_next_trade_id():
    try:
        # Get the maximum trade_id from the table
        max_trade_id = db.session.query(db.func.max(Trade.trade_id)).scalar()
        # If there are no trades yet, start with trade_id 1
        if max_trade_id is None:
            return 1
        return max_trade_id + 1
    except Exception as e:
        print(f"Error getting next trade_id: {str(e)}")
        return None

# Sort trades by date
# order should be asc or desc as input
def sort_trades(trades, order='asc'):
    def parse_date(date_str):
        try:
            # Try parsing as ISO 8601 format
            return datetime.fromisoformat(date_str)
        except ValueError:
            # If parsing fails, try the RFC 1123 format
            return datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %Z')
    
    # Sort trades by parsed date
    return sorted(trades, key=lambda x: parse_date(x['trade_date']), reverse=(order == 'desc'))

# Create a new Trade
@app.route('/trade', methods=['POST'])
def create_trade():
    data = request.json
    next_trade_id = get_next_trade_id()

    if next_trade_id is None:
        return jsonify({"error": "Failed to generate trade_id"}), 500
    
    new_trade = Trade(
        trade_id=next_trade_id,
        user_id=data.get('user_id'),
        card_one_id=data.get('card_one_id'),
        # card_one_name=data.get('card_one_name'),
        # card_earned_date=datetime.strptime(data.get('card_earned_date'), '%Y-%m-%dT%H:%M:%S'),
        # trader_two_id=data.get('trader_two_id'),
        card_two_id=data.get('card_two_id'),
        # card_two_name=data.get('card_two_name'),
        # two_earned_date=datetime.strptime(data.get('two_earned_date'), '%Y-%m-%dT%H:%M:%S'),
        # traded=data.get('traded', False)
        trade_date=datetime.now()
    )
    
    try:
        db.session.add(new_trade)
        db.session.commit()
        return jsonify({"code": 201, "data": new_trade.json()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Get all Trades
@app.route('/trades', methods=['GET'])
def get_trades():
    try:
        trades = Trade.query.all()
        output = []
        for trade in trades:
            trade_id = trade.trade_id
            user_id = trade.user_id
            card_one_id = trade.card_one_id
            card_two_id = trade.card_two_id
            trade_date = trade.trade_date

            user_response = invoke_http(userURL+f"/id/{user_id}")
            card_one_response = invoke_http(cardURL+f"/{card_one_id}")
            card_two_response = invoke_http(cardURL+f"/{card_two_id}")
            # print(user_response)
            # print(card_one_response)
            # print(card_two_response)

            if user_response["code"] == 200 and card_one_response["code"] == 200 and card_two_response["code"] == 200:
                # print("check 1")
                name = user_response["data"]["name"]
                card_one_title = card_one_response["data"]["title"]
                card_one_type = card_one_response["data"]["card_type"]
                card_two_title = card_two_response["data"]["title"]
                card_two_type = card_two_response["data"]["card_type"]
                output.append({"trade_id": trade_id, "trade_date": trade_date.isoformat(), "user_id": user_id, "name": name, 
                            "card_one_id": card_one_id, "card_one_title": card_one_title, "card_one_type": card_one_type, 
                            "card_two_id": card_two_id, "card_two_title": card_two_title, "card_two_type": card_two_type})

        return jsonify({"code": 200, "data": output}), 200

    except Exception as e:
        return jsonify({
            "code": 500,
            "message": f"An error occurred: {str(e)}"
        }), 500

# Get Active Trades and delete trades that are older than 24 hours
@app.route('/active_trades', methods=['GET'])
def get_active_trades():
    try:
        trades_response = get_trades()

        if trades_response[1] != 200:
            return jsonify({
                "code": 400,
                "message": "No available trades"
            }), 400
        
        trades = trades_response[0].get_json()["data"]        
        print("trades:", trades)
        
        updated_trades = []
        for trade in trades:
            # Convert trade_date from ISO format and compare with current time
            trade_date = datetime.fromisoformat(trade["trade_date"])
            # If trade_date + 24 hours is less than current time (in the past), delete the trade
            if trade_date + timedelta(hours=24) < datetime.now():
                trade_id = trade["trade_id"]
                trade_result = delete_trade(trade_id)
                
                if trade_result[1] == 200:
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
    
# Get a Trade by ID
@app.route('/trade/<int:trade_id>', methods=['GET'])
def get_trade(trade_id):
    trade = Trade.query.get(trade_id)
    if trade:
        return jsonify(trade.json()), 200
    return jsonify({"error": "Trade not found"}), 404

# Get Trades by User ID
@app.route('/trade/user/<int:user_id>', methods=['GET'])
def get_trades_by_user(user_id):
    try:
        trades = Trade.query.filter_by(user_id=user_id).all()
        if len(trades) == 0: 
            return jsonify({
                "code": 404,
                "message": "No trades found for user"
            }), 404
        
        output = []
        for trade in trades:
            trade_id = trade.trade_id
            card_one_id = trade.card_one_id
            card_two_id = trade.card_two_id
            trade_date = trade.trade_date

            user_response = invoke_http(userURL+f"/id/{user_id}")
            card_one_response = invoke_http(cardURL+f"/{card_one_id}")
            card_two_response = invoke_http(cardURL+f"/{card_two_id}")
            # print(card_one_response)
            # print(card_two_response)

            if user_response["code"] == 200 and card_one_response["code"] == 200 and card_two_response["code"] == 200:
                name = user_response["data"]["name"]
                card_one_title = card_one_response["data"]["title"]
                card_one_type = card_one_response["data"]["card_type"]
                card_two_title = card_two_response["data"]["title"]
                card_two_type = card_two_response["data"]["card_type"]
                output.append({"trade_id": trade_id, "trade_date": trade_date, "user_id": user_id, "name": name,
                            "card_one_id": card_one_id, "card_one_title": card_one_title, "card_one_type": card_one_type, 
                            "card_two_id": card_two_id, "card_two_title": card_two_title, "card_two_type": card_two_type})

        return jsonify({"code": 200, "data": output}), 200

    except Exception as e:
        return jsonify({
            "code": 500,
            "message": f"An error occurred: {str(e)}"
        }), 500
    
# Get Trades by Search on card title, card type, user name, and order by date
@app.route('/trade/search', methods=['GET'])
def search_trade():
    try:
        keyword = request.args.get('search_input')
        order_by = request.args.get('order_by')
            
        if keyword or order_by:
            response = get_active_trades()
            print("search", response)

            if response["code"] != 200:
                return jsonify({
                    "code": 400,
                    "message": "No available trades"
                }), 400
            
            active_trades = response["data"]
            # print(active_trades)
            output = []

            if order_by and not keyword:
                output = sort_trades(active_trades, order_by)
                print("order by only")
            
            else:
                for trade in active_trades:
                    print(trade)
                    if keyword.lower() in trade["card_one_title"].lower() or keyword.lower() in trade["card_one_type"].lower() or keyword.lower() in trade["card_two_title"].lower() or keyword.lower() in trade["card_two_type"].lower() or keyword.lower() in trade["name"].lower():
                        output.append(trade)
                output = sort_trades(output, order_by)
            
            return jsonify({"code": 200, "data": output}), 200
        
        return jsonify({
            "code": 400,
            "message": "No search keyword provided or sort criteria selected"
        }), 400

    except Exception as e:
        return jsonify({
            "code": 500,
            "message": f"An error occurred: {str(e)}"
        }), 500

# Update a Trade by ID
# @app.route('/trade/<int:trade_id>', methods=['PUT'])
# def update_trade(trade_id):
#     trade = Trade.query.get(trade_id)
#     if trade:
#         data = request.json
#         trade.user_id = data.get('user_id', trade.user_id)
#         trade.card_one_id = data.get('card_one_id', trade.card_one_id)
#         trade.card_one_name = data.get('card_one_name', trade.card_one_name)
#         trade.card_earned_date = datetime.strptime(data.get('card_earned_date'), '%Y-%m-%dT%H:%M:%S') if data.get('card_earned_date') else trade.card_earned_date
#         trade.trader_two_id = data.get('trader_two_id', trade.trader_two_id)
#         trade.card_two_id = data.get('card_two_id', trade.card_two_id)
#         trade.card_two_name = data.get('card_two_name', trade.card_two_name)
#         trade.two_earned_date = datetime.strptime(data.get('two_earned_date'), '%Y-%m-%dT%H:%M:%S') if data.get('two_earned_date') else trade.two_earned_date
#         trade.traded = data.get('traded', trade.traded)
        
#         try:
#             db.session.commit()
#             return jsonify(trade.json()), 200
#         except Exception as e:
#             db.session.rollback()
#             return jsonify({"error": str(e)}), 400
#     return jsonify({"error": "Trade not found"}), 404

# Delete a Trade by ID
@app.route('/trade/<int:trade_id>', methods=['DELETE'])
def delete_trade(trade_id):
    trade = Trade.query.get(trade_id)
    if trade:
        try:
            db.session.delete(trade)
            db.session.commit()
            return jsonify({"code": 200, "message": "Trade deleted"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"code": 400, "error": str(e)}), 400
    return jsonify({"code": 404, "error": "Trade not found"}), 404

if __name__ == '__main__':
    app.run(port=5013, debug=True)

