from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
# from .user import User
from flask_cors import CORS, cross_origin

from datetime import datetime, timedelta, date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/healthpal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS' ] = False

db = SQLAlchemy(app)
CORS(app)

class Event(db.Model):
    __tablename__ = 'events'
    
    event_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    second_title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(64), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    organiser = db.Column(db.String(64), nullable=False)
    event_type = db.Column(db.String(64), nullable=False)
    # created_by = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
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

    def __init__(self, title, second_title, description, location, start_date, end_date, organiser, event_type, max_signups, mode, participant_remark, entry_code, event_point, event_program, tier, organiser_phone, organiser_email, current_signups=0):
        self.title = title
        self.second_title = second_title
        self.description = description
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.organiser = organiser
        self.event_type = event_type
        # self.created_by = created_by
        self.max_signups = max_signups
        self.current_signups = current_signups
        self.mode = mode
        self.participant_remark = participant_remark
        self.entry_code = entry_code
        self.event_point = event_point
        self.event_program = event_program
        self.tier = tier
        self.organiser_phone = organiser_phone
        self.organiser_email = organiser_email

    def json(self):
        return {
            "event_id": self.event_id,
            "title": self.title,
            "second_title": self.second_title,
            "description": self.description,
            "location": self.location,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "organiser": self.organiser,
            "event_type": self.event_type,
            # "created_by": self.created_by,
            "created_date": self.created_date.isoformat(),
            "max_signups": self.max_signups,
            "current_signups": self.current_signups,
            "mode": self.mode,
            "participant_remark": self.participant_remark,
            "entry_code": self.entry_code,
            "event_point": self.event_point,
            "event_program": self.event_program,
            "tier": self.tier,
            "organiser_phone": self.organiser_phone,
            "organiser_email": self.organiser_email
        }

# Create a new event
@app.route('/event', methods=['POST'])
def create_event():
    data = request.json
    new_event = Event(
        title=data.get('title'),
        second_title=data.get('second_title'),
        description=data.get('description'),
        location=data.get('location'),
        start_date=datetime.strptime(data.get('start_date'), '%Y-%m-%d %H:%M:%S'),
        end_date=datetime.strptime(data.get('end_date'), '%Y-%m-%d %H:%M:%S'),
        organiser=data.get('organiser'),
        event_type=data.get('event_type'),
        max_signups=data.get('max_signups'),
        current_signups=data.get('current_signups', 0),
        mode=data.get('mode'),
        participant_remark=data.get('participant_remark'),
        entry_code=data.get('entry_code'),
        event_point=data.get('event_point'),
        event_program=data.get('event_program'),
        tier=data.get('tier'),
        organiser_phone=data.get('organiser_phone'),
        organiser_email=data.get('organiser_email')
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
        return jsonify({
            "code": 200, 
            "data": event.json()
        }), 200
    
    return jsonify({
        "code": 404,
        "error": "Event not found"
    }), 404

# Update an event by ID
@app.route('/event/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    event = Event.query.get(event_id)
    if event:
        data = request.json
        event.title = data.get('title', event.title)
        event.second_title = data.get('second_title', event.second_title)
        event.description = data.get('description', event.description)
        event.location = data.get('location', event.location)
        event.start_date = datetime.strptime(data.get('start_date'), '%Y-%m-%d %H:%M:%S')
        event.end_date = datetime.strptime(data.get('end_date'), '%Y-%m-%d %H:%M:%S')
        event.organiser = data.get('organiser', event.organiser)
        event.event_type = data.get('event_type', event.event_type)
        event.max_signups = data.get('max_signups', event.max_signups)
        event.current_signups = data.get('current_signups', event.current_signups)
        event.mode = data.get('mode', event.mode)
        event.participant_remark = data.get('participant_remark', event.participant_remark)
        event.entry_code = data.get('entry_code', event.entry_code)
        event.event_point = data.get('event_point', event.event_point)
        event.event_program = data.get('event_program', event.event_program)
        event.tier = data.get('tier', event.tier)
        event.organiser_phone = data.get('organiser_phone', event.organiser_phone)
        event.organiser_email = data.get('organiser_email', event.organiser_email)

        try:
            db.session.commit()
            return jsonify({"code": 200, "data": event.json()}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    return jsonify({"error": "Event not found"}), 404

# Update partial fields of event by ID
@app.route('/event/<int:event_id>', methods=['PATCH'])
def partial_update_event(event_id):
    event = Event.query.get(event_id)
    if event:
        data = request.json

        # Update fields only if they are provided in the request
        if 'title' in data:
            event.title = data['title']
        if 'second_title' in data:
            event.second_title = data['second_title']
        if 'description' in data:
            event.description = data['description']
        if 'location' in data:
            event.location = data['location']
        if 'start_date' in data:
            try:
                event.start_date = datetime.strptime(data['start_date'], '%Y-%m-%d %H:%M:%S')
            except ValueError:
                return jsonify({"error": "Invalid date format for start_date. Use 'YYYY-MM-DD HH:MM:SS'."}), 400
        if 'end_date' in data:
            try:
                event.end_date = datetime.strptime(data['end_date'], '%Y-%m-%d %H:%M:%S')
            except ValueError:
                return jsonify({"error": "Invalid date format for end_date. Use 'YYYY-MM-DD HH:MM:SS'."}), 400
        if 'organiser' in data:
            event.organiser = data['organiser']
        if 'event_type' in data:
            event.event_type = data['event_type']
        if 'max_signups' in data:
            event.max_signups = data['max_signups']
        if 'current_signups' in data:
            event.current_signups = data['current_signups']
        if 'mode' in data:
            event.mode = data['mode']
        if 'participant_remark' in data:
            event.participant_remark = data['participant_remark']
        if 'entry_code' in data:
            event.entry_code = data['entry_code']
        if 'event_point' in data:
            event.event_point = data['event_point']
        if 'event_program' in data:
            event.event_program = data['event_program']
        if 'tier' in data:
            event.tier = data['tier']
        if 'organiser_phone' in data:
            event.organiser_phone = data['organiser_phone']
        if 'organiser_email' in data:
            event.organiser_email = data['organiser_email']

        try:
            db.session.commit()
            return jsonify({"code": 200, "data": event.json()}), 200
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

# Get available events 
@app.route('/event/available', methods=['GET'])
def get_available_events():
    try:
        events = Event.query.all()

        if events:
            available_events = []
            current = datetime.now()

            for event in events:
                # Check for event capacity
                if event.current_signups < event.max_signups:

                    # Check for event date and time > 1 hour from now
                    if current < event.start_date and (event.start_date - current).total_seconds() > 3600:
                        available_events.append(event)
                    
            if available_events:
                return jsonify({
                    "code": 200,
                    "data": [event.json() for event in available_events]
                }), 200

            else:
                return jsonify({
                    "code": 400, 
                    "message": "No available events"
                }), 400
        
        return jsonify({
            "code": 400,
            "message": "No events found"
        }), 400
    
    except Exception as e:
        return jsonify({
            "code": 500,
            "message": f"An error occurred: {str(e)}"
        }), 500

# Get events based on search on title and location, and filter by date
@app.route('/event/search', methods=['GET'])
def search_event():
    try:
        keyword = request.args.get('search_input')
        date = request.args.get('date_input')

        # Convert date_str to datetime object if provided
        date_filter = None
        if date:
            try:
                date_filter = datetime.strptime(date, '%Y-%m-%d').date()
            except ValueError:
                return jsonify({
                    "code": 400,
                    "message": "Invalid date format. Use 'YYYY-MM-DD'."
                }), 400

        # check if input provided
        if keyword or date:
            response = get_available_events()
            # print(response[1])

            if response[1] != 200:
                return jsonify({
                    "code": 400,
                    "message": "No available events"
                }), 400
            
            available_events = response[0].get_json()["data"]
            search_results = []

            for event in available_events:
                title = event["title"].lower()
                location = event["location"].lower()
                start_date = datetime.strptime(event["start_date"], "%Y-%m-%dT%H:%M:%S").date()

                # search input match
                search_match = False
                date_match = False

                # using search
                if keyword:
                    if keyword.lower() in title or keyword.lower() in location:
                        search_match = True

                # not using search
                else:
                    search_match = True
                
                # using date filter
                if date_filter:
                    if start_date == date_filter:
                        date_match = True

                # not using date filer
                else:
                    date_match = True

                if search_match and date_match:
                    search_results.append(event)
            
            print(search_results)
            
            if search_results:
                return jsonify({
                    "code": 200,
                    "data": search_results
                }), 200
            
            return jsonify({
                "code": 400,
                "message": "No search results found"
            }), 400
        
        return jsonify({
            "code": 400,
            "message": "No search keyword provided or date selected"
        }), 400
    
    except Exception as e:
        return jsonify({
            "code": 500,
            "message": f"An error occurred: {str(e)}"
        }), 500


if __name__ == '__main__':
    app.run(port=5002, debug=True)
