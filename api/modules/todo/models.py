from api import db

class Base(db.Model):
    __abstract__=True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)

class Item(Base):
    __tablename__ = 'Item'

    def __init__(self, name):
        self.name = name

    name = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, nullable=False)