from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday = db.Column(db.String)
    animals = db.Column(db.String)

class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    animals = db.Column(db.String)

class Animal(db.Model):
    __tablename__ = 'animals'

    name = db.Column(db.String)
    species = db.Column(db.String)
    zookeeper = db.Column(db.String)
    enclosure = db.Column(db.String)

    id = db.Column(db.Integer, primary_key=True)
