from flask import Flask,jsonify,request, make_response
from flask_restful import Resource


class Home(Resource):
	def get(self):
		return {"message" : "Welcome To Patient Montoring & Management System "}