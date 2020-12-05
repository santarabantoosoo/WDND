# GENERAL TODO 
# complete all methods for the class 'Task'

import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import pandas as pd 
import json


database_name = "api"
database_path = "postgres://{}:{}@{}/{}".format('santarabantoosoo', '123','localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

class Task(db.Model):
  __tablename__ = 'tasks'
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.Text)
  description = db.Column(db.Text)
  times = db.Column(db.Integer)

# TODO complete the insert method

  def insert(self):
    pass

# TODO complete the update method

  def update(self):
    pass

  def delete(self):
    db.session.delete(self)
    db.session.commit()

# TODO complete the format method to enable data to be returned as json  

  def format(self):
    pass