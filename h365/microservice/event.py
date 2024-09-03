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

if __name__ == '__main__':
    app.run(port=5000, debug=True)
