from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/healthpal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS' ] = False

db = SQLAlchemy(app)
CORS(app)

class User(db.Model):
    __tablename__ = 'user'
    
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable = False)
    birthdate = db.Column(db.Date, nullable = False)
    gender = db.Column(db.String(64), nullable = False)
    height = db.Column(db.Float, nullable = False)
    weight = db.Column(db.Float, nullable = False)
    contact_details = db.Column(db.String(64), nullable = False)
    nationality = db.Column(db.String(64), nullable = False)
    email = db.Column(db.String(64), nullable = False, unique = True)
    location_group = db.Column(db.String(64), nullable = False)
    school = db.Column(db.String(64), nullable = False)
    password = db.Column(db.String(64), nullable = False) 
    parent_id = db.Column(db.String(64), db.ForeignKey('user.user_id'), nullable = True) 
    role = db.Column(db.String(64), nullable = False)
    created_date = db.Column(db.DateTime, nullable = False)
    last_login = db.Column(db.DateTime, nullable = False)
    total_point = db.Column(db.Integer, nullable = False)
    health_tier = db.Column(db.Integer, nullable = False)
    # children = db.relationship('User', backref = db.backref('parent', remote_side =[user_id]), lazy = True)
    target_minutes = db.Column(db.Integer, nullable = False)
    preferred_intensity = db.Column(db.Integer, nullable = False)
    goal_date = db.Column(db.Date, nullable = False)
    
    def __init__(self, user_id, name, birthdate, gender, height, weight, contact_details, nationality, email, location_group, school, password, target_minutes, preferred_intensity, goal_date, parent_id=None, role='User', created_date=None, last_login=None, total_point=0, health_tier = 0):
        self.user_id = user_id
        self.name = name
        self.birthdate = birthdate
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
        self.total_point = 0
        self.health_tier = 1 
        self.target_minutes = target_minutes
        self.preferred_intensity = preferred_intensity
        self.goal_date = goal_date

    def json(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "birthdate": self.birthdate.isoformat(),
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
            "total_point": self.total_point,
            "health_tier":self.health_tier,
            "target_minutes": self.target_minutes,
            "preferred_intensity": self.preferred_intensity,
            "goal_date": self.goal_date.isoformat()
        }

# Get the next user_id
def get_next_user_id():
    try:
        # Get the maximum user_id from the table
        max_user_id = db.session.query(db.func.max(User.user_id)).scalar()
        # If there are no users yet, start with user_id 1
        if max_user_id is None:
            return 1
        return max_user_id + 1
    except Exception as e:
        print(f"Error getting next user_id: {str(e)}")
        return None
    
# Create a new user
@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    next_user_id = get_next_user_id()

    if next_user_id is None:
        return jsonify({"error": "Failed to generate user_id"}), 500
    
    new_user = User(
        user_id=next_user_id,
        name=data.get('name'),
        birthdate=datetime.strptime(data.get('birthdate'), '%Y-%m-%d'),
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
        role=data.get('role', 'User'),
        target_minutes=data.get('target_minutes'),
        preferred_intensity=data.get('preferred_intensity'),
        goal_date=datetime.strptime(data.get('goal_date'), '%Y-%m-%d')
    )
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"code": 200, "data": new_user.json()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.json() for user in users]), 200

# Get a user by Email
@app.route('/user/<string:email>', methods=['GET'])
def get_user(email):
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({"code": 200, "data": user.json()}), 200
    return jsonify({"code": 404, "error": "User not found"}), 404

# Get a user by ID
@app.route('/user/id/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({"code": 200, "data": user.json()}), 200
    return jsonify({"code": 404, "error": "User not found"}), 404

# Update a user by Email
@app.route('/user/<string:email>', methods=['PUT'])
def update_user(email):
    user = User.query.filter_by(email=email).first()
    if user:
        user.last_login = datetime.now()
        
        try:
            db.session.commit()
            return jsonify(user.json()), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
        
    return jsonify({"error": "User not found"}), 404

# Update partial fields of user by Email
@app.route('/user/<string:email>', methods=['PATCH'])
def partial_update_user(email):
    user = User.query.filter_by(email=email).first()
    if user:
        data = request.json

        # Update fields only if they are provided in the request
        if 'name' in data:
            user.name = data['name']
        if 'birthdate' in data:
            user.birthdate = datetime.strptime(data['birthdate'], '%Y-%m-%d')
        if 'gender' in data:
            user.gender = data['gender']
        if 'height' in data:
            user.height = data['height']
        if 'weight' in data:
            user.weight = data['weight']
        if 'contact_details' in data:
            user.contact_details = data['contact_details']
        if 'nationality' in data:
            user.nationality = data['nationality']
        if 'location_group' in data:
            user.location_group = data['location_group']
        if 'school' in data:
            user.school = data['school']
        if 'password' in data:
            user.password = data['password']
        if 'role' in data:
            user.role = data['role']
        if 'last_login' in data:
            user.last_login = data['last_login']
        if 'total_point' in data:
            user.total_point = data['total_point']
        if 'health_tier' in data:
            user.health_tier = data['health_tier']
        if 'target_minutes' in data:
            user.target_minutes = data['target_minutes']
        if 'preferred_intensity' in data:
            user.preferred_intensity = data['preferred_intensity']
        if 'goal_date' in data:
            user.goal_date = datetime.strptime(data['goal_date'], '%Y-%m-%d')
        
        try:
            db.session.commit()
            return jsonify({"code": 200, "data": user.json()}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    
    return jsonify({"error": "User not found"}), 404
            
# Delete a user by Email
@app.route('/user/<string:email>', methods=['DELETE'])
def delete_user(email):
    user = User.query.filter_by(email=email).first()
    if user:
        try:
            db.session.delete(user)
            db.session.commit()
            return jsonify({"message": "User deleted"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
    return jsonify({"error": "User not found"}), 404

# Get User's Profile Information
@app.route('/user/profile/<string:email>', methods=['GET'])
def get_user_profile(email):
    user = User.query.filter_by(email=email).first()
    if user:
        formatted_date = user.birthdate.strftime("%d %B %Y")
        return jsonify({"code": 200,
                        "data": {"name": user.name, "birthdate": formatted_date, "gender": user.gender, 
                                "school": user.school, "location_group": user.location_group, 
                                "height": user.height, "weight": user.weight, 
                                "target_minutes": user.target_minutes, "preferred_intensity": user.preferred_intensity}}), 200
    
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(port=5001, debug=True)