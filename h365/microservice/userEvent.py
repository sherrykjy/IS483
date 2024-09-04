from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from .user import User
from .event import Event

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/userevent'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS' ] = False

db = SQLAlchemy()

class UserEvents(db.Model):
    __tablename__ = 'user_event'
    
    user_event_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'), nullable=False)
    registered = db.Column(db.Boolean, nullable=False, default=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, user_id, event_id, registered=True, completed=True):
        self.user_id = user_id
        self.event_id = event_id
        self.registered = registered
        self.completed = completed

    def json(self):
        return {
            "user_event_id": self.user_event_id,
            "user_id": self.user_id,
            "event_id": self.event_id,
            "registered": self.registered,
            "completed": self.completed
        }
        
# Create a new UserEvent
@app.route('/userevent', methods=['POST'])
def create_user_event():
    data = request.json
    new_user_event = UserEvents(
        user_id=data.get('user_id'),
        event_id=data.get('event_id'),
        registered=data.get('registered', True),
        completed=data.get('completed', False)
    )
    try:
        db.session.add(new_user_event)
        db.session.commit()
        return jsonify(new_user_event.json()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Get all UserEvents
@app.route('/userevents', methods=['GET'])
def get_user_events():
    user_events = UserEvents.query.all()
    return jsonify([user_event.json() for user_event in user_events]), 200

# Get a UserEvent by ID
@app.route('/userevent/<int:user_event_id>', methods=['GET'])
def get_user_event(user_event_id):
    user_event = UserEvents.query.get(user_event_id)
    if user_event:
        return jsonify(user_event.json()), 200
    return jsonify({"error": "UserEvent not found"}), 404

# Update a UserEvent by ID
@app.route('/userevent/<int:user_event_id>', methods=['PUT'])
def update_user_event(user_event_id):
    user_event = UserEvents.query.get(user_event_id)
    if user_event:
        data = request.json
        user_event.user_id = data.get('user_id', user_event.user_id)
        user_event.event_id = data.get('event_id', user_event.event_id)
        user_event.registered = data.get('registered', user_event.registered)
        user_event.completed = data.get('completed', user_event.completed)
        
        try:
            db.session.commit()
            return jsonify(user_event.json()), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    return jsonify({"error": "UserEvent not found"}), 404

# Delete a UserEvent by ID
@app.route('/userevent/<int:user_event_id>', methods=['DELETE'])
def delete_user_event(user_event_id):
    user_event = UserEvents.query.get(user_event_id)
    if user_event:
        try:
            db.session.delete(user_event)
            db.session.commit()
            return jsonify({"message": "UserEvent deleted"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    return jsonify({"error": "UserEvent not found"}), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)