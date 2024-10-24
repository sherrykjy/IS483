from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
# from user import User
# from event import Event
from flask_cors import CORS, cross_origin
from invokes import invoke_http

from datetime import datetime, timedelta, date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/healthpal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS' ] = False

db = SQLAlchemy(app)
CORS(app)

userURL = "http://localhost:5001/user/"
eventURL = "http://localhost:5002/event/"

class User(db.Model):    
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    gender = db.Column(db.String(64), nullable = False)
    height = db.Column(db.Float, nullable = False)
    weight = db.Column(db.Float, nullable = False)
    contact_details = db.Column(db.String(64), nullable = False)
    nationality = db.Column(db.String(64), nullable = False)
    email = db.Column(db.String(64), nullable = False, unique = True)
    location_group = db.Column(db.String(64), nullable = False)
    school = db.Column(db.String(64), nullable = False)
    password = db.Column(db.String(64), nullable = False) 
    parent_id = db.Column(db.String(64), db.ForeignKey('user_id'), nullable = True) 
    role = db.Column(db.String(64), nullable = False)
    created_date = db.Column(db.DateTime, nullable = False)
    last_login = db.Column(db.DateTime, nullable = False)
    total_point = db.Column(db.Integer, nullable = False)
    health_tier = db.Column(db.Integer, nullable = False)
    user_event = db.relationship('UserEvents', backref='user', lazy=True)

class Event(db.Model):    
    event_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    second_title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(64), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    organiser = db.Column(db.String(64), nullable=False)
    event_type = db.Column(db.String(64), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    max_signups = db.Column(db.Integer, nullable=False)
    current_signups = db.Column(db.Integer, nullable=False, default=0)
    mode = db.Column(db.String(64), nullable=False)
    participant_remark = db.Column(db.String(200), nullable=False)
    entry_code = db.Column(db.String(64), nullable=True)
    event_point = db.Column(db.Integer, nullable=False)
    event_program = db.Column(db.String(200), nullable=False)
    tier = db.Column(db.Integer, nullable=False)
    organiser_phone = db.Column(db.String(64), nullable=False)
    organiser_email = db.Column(db.String(64), nullable=False)
    user_event = db.relationship('UserEvents', backref='events', lazy=True)

class UserEvents(db.Model):
    __tablename__ = 'user_events'
    
    user_event_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'), nullable=False)
    registered = db.Column(db.Boolean, nullable=False, default=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, user_event_id, user_id, event_id, registered, completed):
        self.user_event_id = user_event_id
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

# Get the next user_event_id
def get_next_user_event_id():
    try:
        # Get the maximum user_event_id from the table
        max_user_event_id = db.session.query(db.func.max(UserEvents.user_event_id)).scalar()
        # If there are no UserEvents yet, start with user_event_id 1
        if max_user_event_id is None:
            return 1
        return max_user_event_id + 1
    except Exception as e:
        print(f"Error getting next user_id: {str(e)}")
        return None
        
# Create a new UserEvent
@app.route('/userevent', methods=['POST'])
def create_user_event():
    data = request.json
    new_user_event = UserEvents(
        user_event_id=get_next_user_event_id(),
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
        return jsonify({
            "code": 200,
            "data": user_event.json()
        }), 200
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

# Update partial fields of UserEvent by user_event_id
@app.route('/userevent/<int:user_event_id>', methods=['PATCH'])
def partial_update_user_event(user_event_id):
    user_event = UserEvents.query.get(user_event_id)
    if user_event:
        data = request.json

        # Update fields only if they are provided in the request
        if 'user_id' in data:
            user_event.user_id = data['user_id']
        if 'event_id' in data:
            user_event.event_id = data['event_id']
        if 'registered' in data:
            user_event.registered = data['registered']
        if 'completed' in data:
            user_event.completed = data['completed']
        
        try:
            db.session.commit()
            return jsonify({"code": 200, "data": user_event.json()}), 200
        
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    
    return jsonify({"error": "User Event not found"}), 404

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

# Get active user events for a user
@app.route('/userevent/active/<int:user_id>', methods=['GET'])
def get_active_user_events(user_id):
    try:
        user_events = UserEvents.query.filter_by(user_id=user_id, registered=True, completed=False).all()

        if user_events:
            final = []

            for user_event in user_events:
                event_id = user_event.event_id

                eventInfoURL = eventURL + str(event_id)
                event = invoke_http(eventInfoURL, method='GET')

                if isinstance(event, dict) and event.get("code", 200) != 200:
                    return jsonify(event), event["code"]

                else:
                    final.append(event)
            
            return jsonify(final), 200

        return jsonify({
            "code": 400,
            "message": "No active events found for this user_id"
        }), 400
    
    except Exception as e:
        return jsonify({
            "code": 500,
            "message": f"An error occurred: {str(e)}"
        }), 500

# Enrol user in an event
@app.route('/userevent/enrol', methods=['POST'])
def enrol_user_event():
    try:
        data = request.json
        user_id_input = data.get('user_id')
        event_id_input = data.get('event_id')
        entry_code_input = data.get('entry_code')

        targetEventURL = eventURL + str(event_id_input)

        # Check if event exists 
        event_response = invoke_http(targetEventURL, method='GET')
        event = event_response["data"] 

        if not event or event.get("code", 200) != 200:
            return jsonify({"error": "Event not found"}), 404

        print(event)

        # Check if entry code matches if entry code is required
        if (event["entry_code"] is not None and event["entry_code"] != entry_code_input):
            return jsonify({"error": "Entry code does not match"}), 400

        # Check whether max capacity has been reached
        if event["current_signups"] >= event["max_signups"]:
            return jsonify({"error": "Event is full"}), 400

        # Check if user is already registered for the event
        user_event = UserEvents.query.filter_by(user_id=user_id_input, event_id=event_id_input).first()
        if user_event:
            return jsonify({"error": "User is already registered for this event"}), 400

        # Add record in UserEvents table
        next_user_event_id = get_next_user_event_id()
        if next_user_event_id is None:
            return jsonify({"error": "Failed to generate user_event_id"}), 500
        
        new_user_event = UserEvents(user_event_id=next_user_event_id,
                                    user_id=user_id_input,
                                    event_id=event_id_input,
                                    registered=True,
                                    completed=False
                                    )
        
        db.session.add(new_user_event)
        db.session.commit()

        # Update current signups for the event
        response = invoke_http(targetEventURL, method='PATCH', json={"current_signups": event["current_signups"] + 1})
        
        if response["code"] != 200:
            db.session.rollback()
            return jsonify({"error": "Failed to update event signups"}), 500

        return jsonify({"code": 201, "data": new_user_event.json()}), 201

    except Exception as e:
        return jsonify({
            "code": 500,
            "message": f"An error occurred: {str(e)}"
        }), 500

# Get users by event id
@app.route('/userevent/eventusers/<int:event_id>', methods=['GET'])
def get_users_by_event(event_id):
    try:
        # get all users who are registered for the event
        user_events = UserEvents.query.filter_by(event_id=event_id, registered=True).all()

        if user_events:
            output = []

            for user_event in user_events:
                user_id = user_event.user_id

                # get info for each user
                userInfoURL = userURL + "id/" + str(user_id)
                user = invoke_http(userInfoURL, method='GET')

                if isinstance(user, dict) and user["code"] != 200:
                    return jsonify(user), user["code"]

                else:
                    userInfo = user["data"]
                    output.append({
                        "user_event_id": user_event.user_event_id,
                        "event_id": user_event.event_id,
                        "user_id": userInfo["user_id"],
                        "name": userInfo["name"],
                        "contact_details": userInfo["contact_details"],
                        "email": userInfo["email"],
                        "gender": userInfo["gender"],
                        "registered": user_event.registered,
                        "completed": user_event.completed
                    })
            
            return jsonify({
                "code": 200,
                "data": output
            }), 200

        return jsonify({
            "code": 400,
            "message": "No users found for this event_id"
        }), 400
    
    except Exception as e:
        return jsonify({
            "code": 500,
            "message": f"An error occurred: {str(e)}"
        }), 500
    
if __name__ == '__main__':
    app.run(port=5007, debug=True)