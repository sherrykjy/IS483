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
        
if __name__ == '__main__':
    app.run(port=5000, debug=True)