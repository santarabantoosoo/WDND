from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config.from_pyfile('config.cfg')

db = SQLAlchemy(app)

class Member(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(30), unique=True)
	password = db.Column(db.String(30))
	email = db.Column(db.String(50))
	join_date = db.Column(db.DateTime)

	orders = db.relationship('Order', backref='member', lazy='select')
	courses = db.relationship('Course', secondary='user_courses', backref='member', lazy='select')

	def __repr__(self):
		return '<Member %r>' % self.username

class Order(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	price = db.Column(db.Integer)
	member_id = db.Column(db.Integer, db.ForeignKey('member.id'))

class Course(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))

	def __repr__(self):
	 return f'name : {self.name}'

db.Table('user_courses',
	db.Column('member_id', db.Integer, db.ForeignKey('member.id')),
	db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
	)

# @app.route('/')
# def index():
# 	a = Course.query.count()
# 	b = Course.query.all()
	
# 	return jsonify([i for i in range(10)])
		