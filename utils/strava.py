# import os
# import requests
# from flask import Flask, redirect, request, jsonify, session, url_for
# import time
# from datetime import datetime
# # from dotenv import load_dotenv

# # Load environment variables
# # load_dotenv()

# app = Flask(__name__)
# app.secret_key = 'random_secret_key_for_session'  # Use a secure secret key in production

# # Get credentials from environment variables
# CLIENT_ID = "136238"
# CLIENT_SECRET = "763de85e0d51a7f9d8f518947e85181084d772c9"
# REDIRECT_URI = "http://localhost:5020/callback"
# AUTH_URL = 'https://www.strava.com/oauth/authorize'
# TOKEN_URL = 'https://www.strava.com/oauth/token'
# API_BASE_URL = 'https://www.strava.com/api/v3'

# # Store user tokens in memory (in a production app, use a database)
# users = {}

# # Step 1: Redirect users to Strava to authorize
# @app.route('/connect')
# def connect_strava():
#     strava_auth_url = (
#         f'{AUTH_URL}?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}'
#         f'&scope=read,activity:read'
#     )
#     return redirect(strava_auth_url)

# # Step 2: Callback from Strava to exchange the authorization code for an access token
# @app.route('/callback')
# def callback():
#     code = request.args.get('code')

#     if not code:
#         return jsonify({'error': 'No authorization code provided'}), 400

#     # Exchange the authorization code for an access token
#     token_response = requests.post(
#         TOKEN_URL,
#         data={
#             'client_id': CLIENT_ID,
#             'client_secret': CLIENT_SECRET,
#             'code': code,
#             'grant_type': 'authorization_code',
#         }
#     )
#     token_data = token_response.json()

#     if 'access_token' not in token_data:
#         return jsonify({'error': 'Failed to obtain access token'}), 400

#     # Store user access and refresh tokens in session or in a database
#     access_token = token_data['access_token']
#     refresh_token = token_data['refresh_token']
#     expires_at = token_data['expires_at']
    
#     # In this case, we'll store user tokens in a dictionary using session to track the user
#     user_id = token_data['athlete']['id']
#     users[user_id] = {
#         'access_token': access_token,
#         'refresh_token': refresh_token,
#         'expires_at': expires_at,
#     }

#     session['user_id'] = user_id

#     return jsonify(users)

# # Step 3: Fetch user activities from Strava
# @app.route('/activities', methods=['GET'])
# def get_activities():

#     user_id = session.get('user_id')

#     if not user_id or user_id not in users:
#         return jsonify({'error': 'User not authenticated or access token missing'}), 403

#     # Check if the access token is expired, and refresh if necessary
#     token_info = users[user_id]
#     if token_info['expires_at'] < time.time():
#         token_info = refresh_access_token(user_id)

#     access_token = token_info['access_token']
#     headers = {'Authorization': f'Bearer {access_token}'}
    
#     response = requests.get(f'{API_BASE_URL}/athlete/activities', headers=headers)

#     if response.status_code != 200:
#         return jsonify({'error': 'Failed to fetch activities'}), response.status_code

#     return jsonify(response.json())

# # Helper function to refresh the access token
# def refresh_access_token(user_id):
#     token_info = users[user_id]
#     refresh_token = token_info['refresh_token']

#     response = requests.post(
#         TOKEN_URL,
#         data={
#             'client_id': CLIENT_ID,
#             'client_secret': CLIENT_SECRET,
#             'grant_type': 'refresh_token',
#             'refresh_token': refresh_token,
#         }
#     )
    
#     new_token_data = response.json()
#     access_token = new_token_data['access_token']
#     refresh_token = new_token_data['refresh_token']
#     expires_at = new_token_data['expires_at']

#     # Update stored token info
#     users[user_id] = {
#         'access_token': access_token,
#         'refresh_token': refresh_token,
#         'expires_at': expires_at,
#     }
#     return users[user_id]

# if __name__ == '__main__':
#     app.run(port=5020, debug=True)

#________________________________________
import os
import requests
from flask import Flask, redirect, request, jsonify, session, url_for
import time
from datetime import datetime
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/healthpal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS' ] = False

db = SQLAlchemy(app)
CORS(app)

class strava_users(db.Model):
    __tablename__ = 'strava_users'
    
    id = db.Column(db.Integer, primary_key=True)
    strava_id = db.Column(db.String(50), unique=True, nullable=False)
    access_token = db.Column(db.String(200), nullable=False)
    refresh_token = db.Column(db.String(200), nullable=False)
    expires_at = db.Column(db.Integer, nullable=False)

    def __init__(self, strava_id, access_token, refresh_token, expires_at):
        self.strava_id = strava_id
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expires_at = expires_at

    def json(self):
        return {
            "id": self.id,
            "strava_id": self.strava_id,
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
            "expires_at": self.expires_at
        }
        
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default_secret_key')

# Get credentials from environment variables
CLIENT_ID = "136238"
CLIENT_SECRET = "763de85e0d51a7f9d8f518947e85181084d772c9"
REDIRECT_URI = "http://localhost:5020/callback"
AUTH_URL = 'https://www.strava.com/oauth/authorize'
TOKEN_URL = 'https://www.strava.com/oauth/token'
API_BASE_URL = 'https://www.strava.com/api/v3'

# Step 1: Redirect users to Strava to authorize
@app.route('/connect')
def connect_strava():
    strava_auth_url = (
        f'{AUTH_URL}?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}'
        f'&scope=read,activity:read'
    )
    return redirect(strava_auth_url)

# Step 2: Callback from Strava to exchange the authorization code for an access token
@app.route('/callback')
def callback():
    code = request.args.get('code')

    if not code:
        return jsonify({'error': 'No authorization code provided'}), 400

    # Exchange the authorization code for an access token
    token_response = requests.post(
        TOKEN_URL,
        data={
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'code': code,
            'grant_type': 'authorization_code',
        }
    )
    token_data = token_response.json()

    if 'access_token' not in token_data:
        return jsonify({'error': 'Failed to obtain access token'}), 400

    # Retrieve or create the user in the database
    user_id = token_data['athlete']['id']
    user = strava_users.query.filter_by(strava_id=user_id).first()

    if user:
        # Update existing user tokens
        user.access_token = token_data['access_token']
        user.refresh_token = token_data['refresh_token']
        user.expires_at = token_data['expires_at']
        db.session.commit()
    else:
        # Create a new user
        user = strava_users(
            strava_id=user_id,
            access_token=token_data['access_token'],
            refresh_token=token_data['refresh_token'],
            expires_at=token_data['expires_at']
        )
        db.session.add(user)
        db.session.commit()

    # db.session.commit()

    session['user_id'] = user_id

    return jsonify({'message': 'User authenticated successfully! Please return to H365.'})

# Step 3: Fetch user activities from Strava
@app.route('/activities', methods=['GET'])
def get_activities():
    # user_id = session.get('user_id')
    # token_info = session.get('token_info')

    # if not user_id:
    #     return jsonify({'error': 'User not authenticated'}), 403

    user = strava_users.query.first()

    print(user)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Check if the token has expired, and refresh if necessary
    if user.expires_at < time.time():
        user = refresh_access_token(user)

    access_token = user.access_token
    headers = {'Authorization': f'Bearer {access_token}'}

    response = requests.get(f'{API_BASE_URL}/athlete/activities', headers=headers)

    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch activities'}), response.status_code

    return jsonify({"data": response.json()})

# Helper function to refresh the access token
def refresh_access_token(user):
    response = requests.post(
        TOKEN_URL,
        data={
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'grant_type': 'refresh_token',
            'refresh_token': user.refresh_token,
        }
    )

    new_token_data = response.json()
    user.access_token = new_token_data['access_token']
    user.refresh_token = new_token_data['refresh_token']
    user.expires_at = new_token_data['expires_at']

    db.session.commit()

    return user

if __name__ == '__main__':
    app.run(port=5020, debug=True)
