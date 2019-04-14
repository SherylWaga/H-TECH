from flask import Flask,jsonify,request, make_response
from flask_restful import Resource
import psycopg2
import random 
import json
import datetime

from flask_jwt_extended import (create_access_token, jwt_required, 
                                get_jwt_identity, get_current_user, get_raw_jwt, JWTManager)

connection = psycopg2.connect(dbname='dab67m4dtjn66i', user='etfeuvuknkkukm', password='8fd8db2a94d104296e790e37ebb7bab43662457cdc4bf7b19bfa26dd972b7914', host='ec2-50-17-231-192.compute-1.amazonaws.com', port='5432')
curr = connection.cursor()



class Home(Resource):
	def get(self):
		return {"message" : "Welcome To Patient Montoring & Management System "}

class Register(Resource):
	def post(self):
		data = request.get_json(force=True)
		un_id = random.randint(1, 1000)
		un_id = str(un_id)
		first_name = data['first_name']
		last_name = data['last_name']
		email = data['email']
		id_number = data['id_number']
		phone_number = data['phone_number']
		age = data['age']
		weight = data['weight']
		location = data['location']
		next_appointment = data['next_appointment']
		curr.execute(""" INSERT INTO pattient(un_id, first_name, last_name, email, id_number, phone_number, age, weight, location, next_appointment)
											VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",\
												(un_id, first_name, last_name, email, id_number, phone_number, age, weight, location, next_appointment))
		connection.commit()
		return {"message": "User Created Successfully"}

class Tests(Resource):
	def post(self):
		data = request.get_json(force=True)
		un_id = data['un_id']
		tests = data['tests']
		results = data['results']

		curr.execute(""" INSERT INTO tests(un_id, tests, results)
									VALUES(%s, %s, %s)""",\
										(un_id, tests, results))
		connection.commit()
		return {"message":"Created Successfully"}
