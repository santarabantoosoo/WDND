from flask import Flask, render_template, request, redirect, url_for, jsonify, abort, Response
from flask_sqlalchemy import SQLAlchemy
from config import app, db
from models import Account, Savings
import sys

# CREATE ACCOUNT

# TODO create an account and implement ' try/except/finally ' with error handling

# ACCESS ACCOUNT

@app.route('/account/<acc_id>/inquire', methods = ['GET'])
def access_account(acc_id):

    error = False
    body = {}

    try:
        account = Account.query.get(acc_id)
        
        body['account_id'] = account.id
        body['first_name'] = account.first_name
        body['balance'] = account.balance

        if account.svg:
            body['svg_id'] = account.svg.id
            body['svg_balance'] = account.svg.saving_balance
        else:
            body['svg_id'] = 'null'    
    except:
        error = True
        print(sys.exc_info())
        db.session.rollback()
    
    finally:
        db.session.close()

    if error:
        abort(400)
    else:
        return jsonify(body)        







# @app.route('/account/<id>/inquire')
# def inquire(id):
#     error = False
#     body = {}
#     try:
#         user_account = Account.query.get(id) 
#         body['account_id'] = user_account.id
#         body['first_name'] = user_account.first_name
#         body['balance'] = user_account.balance

#         if user_account.svg:
#             body['svg_id'] = user_account.svg.id
#             body['svg_balance'] = user_account.svg.saving_balance
#         else:
#             body['svg_id'] = 'null'
#     except:
#         db.session.rollback()
#         error = True
#         print(sys.exc_info())
#     finally:
#         db.session.close()

#     # For returning JSON
#     if error:
#         abort(400)
#     else:
#         return jsonify(body)


# WITHDRAW WITH VALIDATION OVER VALUES AND THROWING CUSTOM ERROR MESSAGE TO VIEW
@app.route('/account/<id>/withdraw', methods=['POST'])
def withdraw(id):
    error = False
    body = {}

    try:
        user_account = Account.query.get(id)
        old_balance = int(user_account.balance)
        withdraw_amount = int(request.get_json()['amount'])

        if withdraw_amount > old_balance:
            return jsonify({'error': 'Insufficient Balance'}), 400
        else:
            new_balance = old_balance - withdraw_amount
            user_account.balance = new_balance
            db.session.commit()
            body['balance'] = user_account.balance
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()

    if error:
        abort(400)
    else:
        return jsonify(body)

# DEPOSIT
@app.route('/account/<id>/deposit', methods=['POST'])
def deposit(id):
    error = False
    body = {}
    try:
        user_obj = Account.query.get(id)
        old_balance = int(user_obj.balance)
        withdraw_amount = eval(request.get_json()['amount'])
        new_balance = old_balance + withdraw_amount
        user_obj.balance = new_balance
        db.session.commit()
        body["balance"] = user_obj.balance
    except:
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()

    if error:
        abort(400)
    else:
        return jsonify(body)


# DELETE ACCOUNT
@app.route('/account/<u_id>', methods=['DELETE'])
def delete_account(u_id):
    # print(u_id)
    error = False
    body = {}
    try:
        Account.query.filter_by(id=u_id).delete()
        # Account.query.delete(id = u_id)
        # print(Account.query.get(u_id))
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()

    return jsonify({'success': True})

# CREATE SAVINGS ACCOUNT
@app.route('/savings/<acc_id>/create', methods=['POST'])
def create_savings(acc_id):
    body = {}
    error = False
    try:
        user_obj = Account.query.get(acc_id)
        svg_init_balance = eval(request.get_json()['svg_init_balance'])
        new_svg = Savings(saving_balance=svg_init_balance)
        new_svg.savings = user_obj
        db.session.commit()
        body['svg_id'] = user_obj.svg.id
        body['svg_balance'] = user_obj.svg.saving_balance
    except:
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()

    if error:
        abort(400)
    else:
        return jsonify(body)


# REDIRECTING EXAMPLE FOR ACCOUNT CREATE
@app.route('/account/<acc_id>/details')
def c_account(acc_id):
    user_obj = Account.query.get(acc_id)
    return render_template('account.html', data=user_obj)

# INDEX ROUTE
@app.route('/')
def index(data=None):
    return render_template('index.html', data=Account.query.count())
