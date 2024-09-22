from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost:3306/healthpal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Trade(db.Model):
    __tablename__ = 'trade'
    
    trade_id = db.Column(db.Integer, primary_key=True)
    
    # Trader One
    # user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    # card_one_id = db.Column(db.Integer, db.ForeignKey('card.card_id'), nullable=False)
    user_id = db.Column(db.Integer,  nullable=False)
    card_one_id = db.Column(db.Integer,  nullable=False)
    # card_one_name = db.Column(db.String(255), nullable=False)
    card_earned_date = db.Column(db.DateTime, nullable=False)
    
    # Trader Two
    # trader_two_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=True)
    card_two_id = db.Column(db.Integer,  nullable=True)
    # card_two_name = db.Column(db.String(255), nullable=True)
    # two_earned_date = db.Column(db.DateTime, nullable=True)
    
    # traded = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, user_id, card_one_id, card_earned_date, card_two_id):
        self.user_id = user_id
        self.card_one_id = card_one_id
        # self.card_one_name = card_one_name
        self.card_earned_date = card_earned_date
        # self.trader_two_id = trader_two_id
        self.card_two_id = card_two_id
        # self.card_two_name = card_two_name
        # self.two_earned_date = two_earned_date
        # self.traded = traded

    def json(self):
        return {
            "trade_id": self.trade_id,
            "user_id": self.user_id,
            "card_one_id": self.card_one_id,
            # "card_one_name": self.card_one_name,
            "card_earned_date": self.card_earned_date.isoformat(),
            # "trader_two_id": self.trader_two_id,
            "card_two_id": self.card_two_id,
            # "card_two_name": self.card_two_name,
            # "two_earned_date": self.two_earned_date.isoformat(),
            # "traded": self.traded
        }

# Create a new Trade
@app.route('/trade', methods=['POST'])
def create_trade():
    data = request.json
    new_trade = Trade(
        user_id=data.get('user_id'),
        card_one_id=data.get('card_one_id'),
        # card_one_name=data.get('card_one_name'),
        card_earned_date=datetime.strptime(data.get('card_earned_date'), '%Y-%m-%dT%H:%M:%S'),
        # trader_two_id=data.get('trader_two_id'),
        card_two_id=data.get('card_two_id'),
        # card_two_name=data.get('card_two_name'),
        # two_earned_date=datetime.strptime(data.get('two_earned_date'), '%Y-%m-%dT%H:%M:%S'),
        # traded=data.get('traded', False)
    )
    
    try:
        db.session.add(new_trade)
        db.session.commit()
        return jsonify(new_trade.json()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Get all Trades
@app.route('/trades', methods=['GET'])
def get_trades():
    trades = Trade.query.all()
    return jsonify([trade.json() for trade in trades]), 200

# Get a Trade by ID
@app.route('/trade/<int:trade_id>', methods=['GET'])
def get_trade(trade_id):
    trade = Trade.query.get(trade_id)
    if trade:
        return jsonify(trade.json()), 200
    return jsonify({"error": "Trade not found"}), 404

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
    app.run(port=5010, debug=True)

