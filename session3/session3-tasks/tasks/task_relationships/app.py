from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config.from_pyfile('config.cfg')

db = SQLAlchemy(app)

class Student(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(30), unique=True)
	password = db.Column(db.String(30))
	email = db.Column(db.String(50))
	join_date = db.Column(db.DateTime)

	def __repr__(self):
		return '<Student %r>' % self.username

class Course(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))

	def __repr__(self):
	 return f'name : {self.name}'

