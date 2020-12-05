# GENERAL TODO...  Each room should finish
# 1- methods in models.py 
# 2- inserting data through for loop 
# 3- CORS
# 4- a single endpoint, assigned according to room number 

# For each team, finish a single endpoint with appropraite error status, add the error handler decorators then test the endpoint in POSTMAN. Save POSTMAN request in collections to be used later.  


from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy #, or_
from flask_cors import CORS
import random
import pandas as pd


from models import setup_db, Task

TASKS_TO_VIEW = 7

# TODO initialize CORS and allow cookies. 
# TODO make sure that anyone can access the resource if the URL contains tasks

def create_app(test_config=None):
  app = Flask(__name__)
  setup_db(app)
  CORS(app)


# TODO implement CORS Headers,  allow GET PUT POST PATCH OPTIONS
  # @app.after_request
  

# TODO [[[ROOM1]] complete the for loop to add data from excel. Avoid duplication in data entry 

# df = pd.read_excel('df.xlsx')
# for c, row in df.iterrows():
    

  # @app.route('/tasks')  
  # TODO get only results including cola where the times are not equal to 4.  [hint: use 4 from the query parameter and add the inequality in the route]

  # TODO apply pagination, with 10 items per page. response should be jsonified and should include:
  # 1- paginated tasks 
  # 2- total number of tasks


    # return jsonify({
    #   'success': ,
    #    'tasks': ,
    #    'total_tasks': 
    # })

  
# TODO [[[ROOM2]]] given a task ID, update the task's times into half the original number 

  # @app.route('/task/(int:Task_id)', methods=['PATCH'])
  # def task_new(Task_id):
  #   pass

  #   return jsonify({
  #       'success': True,
  #     })
      
# TODO  [[[ROOM3]]] delete a task. Do you think it should be allowed or CORS would prevent it ?
  # @app.route('/tasks/1/<int:Task_id>', methods=['DELETE'])
  # def delete_Task(Task_id):
  #   pass
    
    #   return jsonify({
    #     'success': True,
    #     'deleted': 'add item',
    #     'tasks': 'add item',
    #     'total_tasks': 'add item'
    #   })

# TODO [[[ROOM4]]] modify what's needed to create a task

  # @app.route('/tasks/1', methods=['POST'])
  # def task():
  #   pass

      # return jsonify({
      #   'success': True,
      #   'created': 'add item',
      #   'tasks': 'add item',
      #   'total_tasks': 'add item'
      # })

  # Bonus TODO
  # Is there an easier and more efficient way to handle RESTFUL APIs instead of routes? check FLASK_RESTFUL extension and try to implement it here. check the resource below
  #  https://rahmanfadhil.com/flask-rest-api/ 


  @app.route('/')
  def index():
    return jsonify({
      'testing APP' :  'U R good to go.. add different routes and test them'
      })

  return app
