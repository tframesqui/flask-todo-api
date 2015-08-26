from api import db

class Base(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	date_created = db.Column(db.DateTime)
	date_modified = db.Column(db.DateTime)