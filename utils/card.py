from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS, cross_origin
from collections import defaultdict

# from .event import Event

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/healthpal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Card(db.Model):
    __tablename__ = 'cards'
    
    card_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    card_type = db.Column(db.String(64), nullable=False)
    points_required = db.Column(db.Integer, nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'), nullable=True)
    description = db.Column(db.String(200), nullable=False)
    recommendation = db.Column(db.String(300), nullable=False)

    def __init__(self, title, card_type, points_required, description, recommendation, event_id=None):
        self.title = title
        self.card_type = card_type
        self.points_required = points_required
        self.event_id = event_id
        self.description = description
        self.recommendation = recommendation

    def json(self):
        return {
            "card_id": self.card_id,
            "title": self.title,
            "card_type": self.card_type,
            "points_required": self.points_required,
            "event_id": self.event_id,
            "description": self.description,
            "recommendation": self.recommendation
        }

# Create a new Card
@app.route('/card', methods=['POST'])
def create_card():
    data = request.json
    new_card = Card(
        title=data.get('title'),
        card_type=data.get('card_type'),
        points_required=data.get('points_required'),
        event_id=data.get('event_id'),
        description=data.get('description'),
        recommendation=data.get('recommendation')
    )
    try:
        db.session.add(new_card)
        db.session.commit()
        return jsonify(new_card.json()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Get all Cards
@app.route('/cards', methods=['GET'])
def get_cards():
    cards = Card.query.all()
    return jsonify([card.json() for card in cards]), 200

# Get all Cards grouped by card_type
@app.route('/card/grouped', methods=['GET'])
def get_cards_grouped():
    try:
        cards = Card.query.all()
        grouped_cards = defaultdict(list)
        print(cards)

        for card in cards:
            grouped_cards[card.card_type].append(card.json())
        
        return jsonify({"code": 200, "data": grouped_cards}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Get a Card by ID
@app.route('/card/<int:card_id>', methods=['GET'])
def get_card(card_id):
    card = Card.query.get(card_id)
    if card:
        return jsonify({"code": 200, "data": card.json()}), 200
    return jsonify({"error": "Card not found"}), 404

# Get Card by Event ID
@app.route('/card/event/<int:event_id>', methods=['GET'])
def get_cards_by_event(event_id):
    cards = Card.query.filter_by(event_id=event_id).all()

    if cards:
        return jsonify({
            "code": 200, 
            "data": [card.json() for card in cards]
        }), 200
    
    return jsonify({
        "code": 404,
        "error": "Cards not found"
    }), 404

# Update a Card by ID
@app.route('/card/<int:card_id>', methods=['PUT'])
def update_card(card_id):
    card = Card.query.get(card_id)
    if card:
        data = request.json
        card.title = data.get('title', card.title)
        card.card_type = data.get('card_type', card.card_type)
        card.points_required = data.get('points_required', card.points_required)
        card.event_id = data.get('event_id', card.event_id)
        card.description = data.get('description', card.description)
        card.recommendation = data.get('recommendation', card.recommendation)
        
        try:
            db.session.commit()
            return jsonify(card.json()), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    return jsonify({"error": "Card not found"}), 404

# Delete a Card by ID
@app.route('/card/<int:card_id>', methods=['DELETE'])
def delete_card(card_id):
    card = Card.query.get(card_id)
    if card:
        try:
            db.session.delete(card)
            db.session.commit()
            return jsonify({"message": "Card deleted"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    return jsonify({"error": "Card not found"}), 404

if __name__ == '__main__':
    app.run(port=5003, debug=True)