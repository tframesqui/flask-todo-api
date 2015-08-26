from flask import Blueprint
from flask_restful import Resource, Api, url_for

todo_bp = Blueprint('api', __name__)

class Todo(Resource):
	def get(self):
		return {'teste': True}