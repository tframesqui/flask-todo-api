# Import flask and template operators
from flask import Flask
from flask_restful import Api
from sqlalchemy import create_engine

from api.modules.todo.resource import Todo, todo_bp

app = Flask(__name__)
api = Api(app)

#configuring resources to use
api.add_resource(Todo, '/todo')


app.config.from_object('config')

db = SQLAlchemy(app)

app.register_blueprint(todo_bp)

#db.create_all()