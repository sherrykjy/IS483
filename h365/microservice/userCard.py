from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from .user import User
from .card import Card  

from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/usercard'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS' ] = False

db = SQLAlchemy()

class UserCard(db.Model):
    __tablename__ = 'user_card'
    
    user_card_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey('card.card_id'), nullable=False)
    earned_date = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __init__(self, user_id, card_id, earned_date=None):
        self.user_id = user_id
        self.card_id = card_id
        self.earned_date = datetime.now()

    def json(self):
        return {
            "user_card_id": self.user_card_id,
            "user_id": self.user_id,
            "card_id": self.card_id,
            "earned_date": self.earned_date.isoformat()
        }

# Create a new UserCard
@app.route('/usercard', methods=['POST'])
def create_user_card():
    data = request.json
    new_user_card = UserCard(
        user_id=data.get('user_id'),
        card_id=data.get('card_id')
    )
    try:
        db.session.add(new_user_card)
        db.session.commit()
        return jsonify(new_user_card.json()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Get all UserCards
@app.route('/usercards', methods=['GET'])
def get_user_cards():
    user_cards = UserCard.query.all()
    return jsonify([user_card.json() for user_card in user_cards]), 200

# Get a UserCard by ID
@app.route('/usercard/<int:user_card_id>', methods=['GET'])
def get_user_card(user_card_id):
    user_card = UserCard.query.get(user_card_id)
    if user_card:
        return jsonify(user_card.json()), 200
    return jsonify({"error": "UserCard not found"}), 404

# Update a UserCard by ID
@app.route('/usercard/<int:user_card_id>', methods=['PUT'])
def update_user_card(user_card_id):
    user_card = UserCard.query.get(user_card_id)
    if user_card:
        data = request.json
        user_card.user_id = data.get('user_id', user_card.user_id)
        user_card.card_id = data.get('card_id', user_card.card_id)
        user_card.earned_date = datetime.strptime(data.get('earned_date'), '%Y-%m-%dT%H:%M:%S') if data.get('earned_date') else user_card.earned_date

        try:
            db.session.commit()
            return jsonify(user_card.json()), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    return jsonify({"error": "UserCard not found"}), 404

# Delete a UserCard by ID
@app.route('/usercard/<int:user_card_id>', methods=['DELETE'])
def delete_user_card(user_card_id):
    user_card = UserCard.query.get(user_card_id)
    if user_card:
        try:
            db.session.delete(user_card)
            db.session.commit()
            return jsonify({"message": "UserCard deleted"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    return jsonify({"error": "UserCard not found"}), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)