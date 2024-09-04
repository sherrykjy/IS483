from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from .user import User

from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/event'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS' ] = False

db = SQLAlchemy()

class Event(db.Model):
    __tablename__ = 'event'
    
    event_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(64), nullable=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    organizer = db.Column(db.String(64), nullable=True)
    event_type = db.Column(db.String(64), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    max_signups = db.Column(db.Integer, nullable=False)
    current_signups = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, title, description, location, start_date, end_date, organizer, event_type, created_by, max_signups, current_signups=0):
        self.title = title
        self.description = description
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.organizer = organizer
        self.event_type = event_type
        self.created_by = created_by
        self.max_signups = max_signups
        self.current_signups = current_signups

    def json(self):
        return {
            "event_id": self.event_id,
            "title": self.title,
            "description": self.description,
            "location": self.location,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "organizer": self.organizer,
            "event_type": self.event_type,
            "created_by": self.created_by,
            "created_date": self.created_date.isoformat(),
            "max_signups": self.max_signups,
            "current_signups": self.current_signups
        }

# Create a new event
@app.route('/event', methods=['POST'])
def create_event():
    data = request.json
    new_event = Event(
        title=data.get('title'),
        description=data.get('description'),
        location=data.get('location'),
        start_date=datetime.strptime(data.get('start_date'), '%Y-%m-%d'),
        end_date=datetime.strptime(data.get('end_date'), '%Y-%m-%d'),
        organizer=data.get('organizer'),
        event_type=data.get('event_type'),
        created_by=data.get('created_by'),
        max_signups=data.get('max_signups'),
        current_signups=data.get('current_signups', 0)
    )
    try:
        db.session.add(new_event)
        db.session.commit()
        return jsonify(new_event.json()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Get all events
@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([event.json() for event in events]), 200

# Get an event by ID
@app.route('/event/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = Event.query.get(event_id)
    if event:
        return jsonify(event.json()), 200
    return jsonify({"error": "Event not found"}), 404

# Update an event by ID
@app.route('/event/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    event = Event.query.get(event_id)
    if event:
        data = request.json
        event.title = data.get('title', event.title)
        event.description = data.get('description', event.description)
        event.location = data.get('location', event.location)
        event.start_date = datetime.strptime(data.get('start_date'), '%Y-%m-%d')
        event.end_date = datetime.strptime(data.get('end_date'), '%Y-%m-%d')
        event.organizer = data.get('organizer', event.organizer)
        event.event_type = data.get('event_type', event.event_type)
        event.max_signups = data.get('max_signups', event.max_signups)
        event.current_signups = data.get('current_signups', event.current_signups)

        try:
            db.session.commit()
            return jsonify(event.json()), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    return jsonify({"error": "Event not found"}), 404

# Delete an event by ID
@app.route('/event/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = Event.query.get(event_id)
    if event:
        try:
            db.session.delete(event)
            db.session.commit()
            return jsonify({"message": "Event deleted"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    return jsonify({"error": "Event not found"}), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)
