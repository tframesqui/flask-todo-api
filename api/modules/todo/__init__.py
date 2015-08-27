from flask import Blueprint
from flask_restful import Resource, reqparse, abort
from api.modules.todo.models import Item
from api.db import db
from flask.ext.restful import fields, marshal


todo_bp = Blueprint('api', __name__)

parser = reqparse.RequestParser()
parser.add_argument('name')

todo_fields = {
	'name': fields.String,
	'done': fields.Boolean
}

class Todo(Resource):
	def get(self):
		return {'items': marshal(Item.query.all(), todo_fields)}

	def post(self):
		args = parser.parse_args()
		item = Item(args['name'])
		item.done = False
		db.session.add(item)
		db.session.commit()
		return {'id': item.id}

