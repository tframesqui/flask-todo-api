# Import flask and template operators
from flask import Flask

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

from api.modules.todo.resource import todo

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

app.register_blueprint(todo)

db.create_all()