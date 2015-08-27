# Import flask and template operators
from flask import Flask
from flask_restful import Api
from api.db import db

from api.modules.todo import Todo, todo_bp

app = Flask(__name__)
api = Api(app)

#configuring resources to use
api.add_resource(Todo, '/todo')

app.config.from_object('config')

app.register_blueprint(todo_bp)

db.init_app(app)