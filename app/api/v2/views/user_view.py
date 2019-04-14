from flask import Flask, jsonify, json, request, make_response
from flask_restful import Resource, Api
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,get_jwt_identity)
# local imports
from app.api.v2.models.user_model import Users
app = Flask(__name__)

api = Api(app) 
app.config['JWT_SECRET_KEY'] = 'WAGS'

class CreateUsers(Resource):

    def post(self):
        

            first_name = request.get_json()['first_name']
            last_name = request.get_json()['last_name']
            username = request.get_json()['username']
            phone= request.get_json()['phone']
            email= request.get_json()['email']
            password = request.get_json()['password']
            validator = "@"
            validator2 = ".com"
            errors = {}
            for key, value in request.get_json().items():
                if not value.strip():
                    errors[key] = "cannot be empty"
            if errors:
                return make_response(jsonify(
                   {"status": 404, "data": errors}), 404)
                
            if validator not in email or validator2 not in email:
                return make_response(jsonify(
                   {"status": 404, "message": "invalid email"}), 404)
                        
        
            Users().save_user(first_name, last_name, email, phone, username, password)
            return make_response(jsonify(
                   {"status": 200, "data": [
                    {"message": "Registration successful"}]}), 200)
      


class Login (Resource):
        def post(self):
            username = request.json.get('username').lower()
            password = request.json.get('password').lower()
            if Users().fetch_user():
                return jsonify({'status_code': 404,
                                'message': 'invalid username'})
            if Users().validate_pass():
                return jsonify({'status_code': 404,
                                'message': 'invalid password.'})
            

            token = create_access_token(identity=username)
            response = jsonify({'token': token,
                                "message": "Welcome " + username,
                                "status_code": 201})
            return response
