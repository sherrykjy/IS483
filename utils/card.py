from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS, cross_origin

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

    def __init__(self, title, card_type, points_required, event_id=None):
        self.title = title
        self.card_type = card_type
        self.points_required = points_required
        self.event_id = event_id

    def json(self):
        return {
            "card_id": self.card_id,
            "title": self.title,
            "card_type": self.card_type,
            "points_required": self.points_required,
            "event_id": self.event_id
        }

# Create a new Card
@app.route('/card', methods=['POST'])
def create_card():
    data = request.json
    new_card = Card(
        title=data.get('title'),
        card_type=data.get('card_type'),
        points_required=data.get('points_required'),
        event_id=data.get('event_id')
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

# Get a Card by ID
@app.route('/card/<int:card_id>', methods=['GET'])
def get_card(card_id):
    card = Card.query.get(card_id)
    if card:
        return jsonify(card.json()), 200
    return jsonify({"error": "Card not found"}), 404

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