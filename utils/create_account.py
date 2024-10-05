from flask import Flask, request, jsonify
from flask_cors import CORS
import os, sys
import requests
from invokes import invoke_http
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/healthpal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS' ] = False

user_URL = "http://localhost:5001/user"

@app.route("/create_account", methods=['POST'])
def create_account():
    if request.is_json:
        try:
            user_information = request.get_json()
            print("\nReceived user infromation in JSON:", user_information)
            result = processUserInformation(user_information)
            return jsonify(result), result['code']
        
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line" + str(exc_tb.tb_lineno)
            print(ex_str)
            
            return jsonify({
                "code": 500,
                "message": "create_account.py internal error: " + ex_str
            }), 500
            
def processUserInformation(user_information):
    
    # 1. Check if user's email exist in database
    # Invoke the user microservice
    print('\n-----Invoking user microservice-----')
    user_result = invoke_http(f"{user_URL}/{user_information['email']}", method='GET')
    print('user_result:', user_result)
    
    # 2. Check code
    user_result_code = user_result["code"]
    
    # 3. If response is 404 (No account found), create a new account
    # Invoke the user microservice
    if user_result_code == 404:
        print('\n-----Invoking user microservice as user email is not found-----')
        account_creation_result = invoke_http(user_URL, method='POST', json=user_information)
        print('account creation result:', account_creation_result)
        
        account_creation_result_code = account_creation_result["code"]
        
        if account_creation_result_code == 200:
            return {
                "code": account_creation_result_code,
                "data": {"account creation result": account_creation_result["data"]},
                "message": "User account creation success"
            }
            
        else:
            return {
                "code": account_creation_result_code,
                "data": {"account creation result": account_creation_result["data"]},
                "message": "User account creation failed due to internal error"
            }
    
    # 4. If response is 200 (Account found), send error 
    elif user_result_code == 200:
        print('\n-----User email found, account creation aborted-----')
        return {
                "code": 400,
                "data": {"user result": user_result["data"]},
                "message": "User account creation failure as user email exists"
            }
        
    # 5. Handle unexpected error codes
    else:
        return {
            "code": user_result_code,
            "data": {"user result": user_result["data"]},
            "message": "An unexpected error occurred while checking for user"
        }

if __name__ == '__main__':
    app.run(port=5008, debug=True)