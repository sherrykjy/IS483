from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
# from .user import User
# from .card import Card  
from flask_cors import CORS, cross_origin
from invokes import invoke_http

from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/healthpal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS' ] = False

db = SQLAlchemy(app)
CORS(app)

cardURL = "http://localhost:5003/card/"
userURL = "http://localhost:5001/user/"
healthCoinURL = "http://localhost:5004/healthcoins"

class UserCard(db.Model):
    __tablename__ = 'user_cards'
    
    user_card_id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    # card_id = db.Column(db.Integer, db.ForeignKey('card.card_id'), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    card_id = db.Column(db.Integer, nullable=False)
    earned_date = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __init__(self, user_card_id, user_id, card_id, earned_date=None):
        self.user_card_id = user_card_id
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

# Get the next user_card_id
def get_next_user_card_id():
    try:
        # Get the maximum user_card_id from the table
        max_user_card_id = db.session.query(db.func.max(UserCard.user_card_id)).scalar()
        # If there are no UserCards yet, start with user_card_id 1
        if max_user_card_id is None:
            return 1
        return max_user_card_id + 1
    except Exception as e:
        print(f"Error getting next user_card_id: {str(e)}")
        return None
    
# Create a new UserCard
@app.route('/usercard', methods=['POST'])
def create_user_card():
    data = request.json
    next_user_card_id = get_next_user_card_id()

    if next_user_card_id is None:
        return jsonify({"error": "Failed to generate user_card_id"}), 400
    
    new_user_card = UserCard(
        user_card_id = next_user_card_id,
        user_id=data.get('user_id'),
        card_id=data.get('card_id'),
        earned_date=data.get('earned_date')
    )
    try:
        db.session.add(new_user_card)
        db.session.commit()
        return jsonify({"code": 201, "data": new_user_card.json()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"code": 400, "error": str(e)}), 400

# Get all UserCards
@app.route('/usercard', methods=['GET'])
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

# Get all UserCards by User ID
@app.route('/usercard/user/<int:user_id>', methods=['GET'])
def get_user_cards_by_user(user_id):
    try:
        user_cards = UserCard.query.filter_by(user_id=user_id).all()
        if user_cards:
            count = len(user_cards)
            all_cards_info = []
            for card in user_cards:
                response = invoke_http(cardURL + str(card.card_id), method='GET')
                card_info = response["data"]
                all_cards_info.append({
                    "user_card_id": card.user_card_id,
                    "user_id": card.user_id,
                    "card_id": card.card_id,
                    "earned_date": card.earned_date,
                    "card_type": card_info['card_type'],
                    "title": card_info['title'],
                    "points_required": card_info['points_required'],
                    "event_id": card_info['event_id'],
                    "description": card_info['description'],
                    "recommendation": card_info['recommendation']
                })
            return jsonify({
                "code": 200, 
                "data": {"count_redeemed": count,
                        "cards": all_cards_info}
            }), 200
        return jsonify({"code": 404, "error": "No cards found for this user ID"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Get UserCard by User ID and Card ID
@app.route('/usercard/user/<int:user_id>/card/<int:card_id>', methods=['GET'])
def get_user_card_by_user_and_card(user_id, card_id):
    user_card = UserCard.query.filter_by(user_id=user_id, card_id=card_id).first()
    if user_card:
        return jsonify({"code": 200, "data": user_card.json()}), 200
    return jsonify({"code": 404, "error": "UserCard not found"}), 404

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
            return jsonify({"message": "UserCard deleted",
                            "code": 200}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    return jsonify({"error": "UserCard not found"}), 404

# Buying a new card
@app.route('/usercard/buy', methods=['POST'])
def buy_new_card():
    try:
        data = request.json
        print(data)
        user_id = data.get('user_id')
        card_id = data.get('card_id')

        # (1) Fetch card info and validate response
        cardResponse = invoke_http(cardURL + str(card_id), method='GET')
        if cardResponse["code"] != 200:
            return jsonify({"code": 400, "error": "Error retrieving card details"}), 400
        card_info = cardResponse["data"]
        card_points = card_info["points_required"]

        # (2) Fetch user info and validate response
        userResponse = invoke_http(userURL + "id/" + str(user_id), method='GET')
        if userResponse["code"] != 200:
            return jsonify({"code": 400, "error": "Error retrieving user details"}), 400
        user_info = userResponse["data"]
        user_points = user_info["total_point"]

        # (3) Check if user has enough points to buy the card
        if user_points < card_points:
            return jsonify({"code": 400, "error": "Insufficient HealthCoins to buy this card"}), 400

        # If sufficient points, (4) add the card to user's collection, (5) deduct the points from user's total points, (6) add record in healthcoins db
        next_user_card_id = get_next_user_card_id()
        if next_user_card_id is None:
            return jsonify({"code": 500, "error": "Error getting next user_card_id"}), 500
        
        # (4) Add the card to user's collection
        new_user_card = UserCard(
            user_card_id=next_user_card_id,
            user_id=user_id,
            card_id=card_id,
            earned_date=datetime.now()
        )

        try:
            db.session.add(new_user_card)
            print("user card added")

            # (5) Deduct the points from user's total points
            deductionResponse = invoke_http(userURL + "id/" + str(user_id), method='PATCH', json={"total_point": user_points - card_points})
            if deductionResponse["code"] != 200:
                # db.session.rollback() # rollback addition of card
                # return jsonify({"code": 400, "error": "Error deducting points from user's total points"}), 400
                raise Exception("Error deducting points from user's total points")

            # (6) Add record in healthcoins db
            healthCoinResponse = invoke_http(healthCoinURL, method='POST', json={"user_id": user_id, "points_earned": -card_points, "earned_date": str(datetime.now()), "source": "Card Purchase"})
            print(healthCoinResponse)
            if healthCoinResponse["code"] != 201:
                # db.session.rollback() # rollback addition of card and points deduction
                # return jsonify({"code": 400, "error": "Error adding record in healthcoins db"}), 400
                raise Exception("Error adding record in healthcoins db")

            # all succeed
            db.session.commit()
            return jsonify({"code": 201, "data": new_user_card.json()}), 201

        except Exception as e:
            db.session.rollback()

            # Compensating transaction: Refund the points if they were deducted
            refundResponse = invoke_http(userURL + "id/" + str(user_id), method='PATCH', json={"total_point": user_points})
            if refundResponse["code"] != 200:
                return jsonify({"code": 500, "error": "Failed to rollback points deduction"}), 500
            
            return jsonify({"code": 400, "error": str(e)}), 400
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(port=5006, debug=True)