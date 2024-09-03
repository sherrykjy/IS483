from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/user'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS' ] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    
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
    password = db.Column(db.Stirng(64), nullable = False)
    parent_id = db.Column(db.Stirng(64), db.ForeignKey('user_id'), nullable = False)
    role = db.Column(db.String(64), nullable = False)
    created_date = db.Column(db.DateTime, nullable = False)
    last_login = db.Column(db.DateTime, nullable = False)
    total_points = db.Column(db.Integer, nullable = False)
    children = db.relationship('User', backref = db.backref('parent', remote_side =[user_id]), lazy = True)
    
    def __init__(self, user_id, name, age, gender, height, weight, contact_details, nationality, email, location_group, school, password, parent_id=None, role='User', created_date=None, last_login=None, total_points=0):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.contact_details = contact_details
        self.nationality = nationality
        self.email = email
        self.location_group = location_group
        self.school = school
        self.password = password
        self.parent_id = parent_id
        self.role = role
        self.created_date = datetime.now()
        self.last_login = datetime.now()
        self.total_points = 0

    def json(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "height": self.height,
            "weight": self.weight,
            "contact_details": self.contact_details,
            "nationality": self.nationality,
            "email": self.email,
            "location_group": self.location_group,
            "school": self.school,
            "password": self.password,
            "parent_id": self.parent_id,
            "role": self.role,
            "created_date": self.created_date.isoformat(),
            "last_login": self.last_login.isoformat(),
            "total_points": self.total_points
        }
    
@app.route("/user", methods=['GET'])
def get_all():
    users = User.query.all()
    return jsonify([user.json() for user in users])

@app.route("/user/<string:userid>", methods=['GET'])
def find_by_userid(userid):
    user = User.query.filter_by(user_id=userid).first()
    if user:
        return jsonify(user.json())
    return jsonify({"message": "User not found"}), 404

@app.route("/user/<string:userid>", methods=['POST'])
def create_user(userid):
    if User.query.filter_by(user_id=userid).first():
        return jsonify({"message": "User with this ID already exists"}), 400
    
    data = request.json
    new_user = User(
        user_id=userid,
        name=data.get('name'),
        age=data.get('age'),
        gender=data.get('gender'),
        height=data.get('height'),
        weight=data.get('weight'),
        contact_details=data.get('contact_details'),
        nationality=data.get('nationality'),
        email=data.get('email'),
        location_group=data.get('location_group'),
        school=data.get('school'),
        password=data.get('password'),
        parent_id=data.get('parent_id'),
        role=data.get('role'),
        created_date=data.get('created_date'),
        last_login=data.get('last_login'),
        total_points=data.get('total_points')
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify(new_user.json()), 201

if __name__ == '__main__':
    app.run(port=5000, debug=True)