from flask import Flask, render_template, request, redirect, url_for, jsonify, abort, Response
from flask_sqlalchemy import SQLAlchemy
from config import app, db
from models import Account, Savings
import sys

# TODO CREATE ACCOUNT  (optional)

# TODO:1 CREATE SAVINGS ACCOUNT -- 

# TODO:2 Acces account by ID and print savings account details if available

# TODO:3 WITHDRAW WITH VALIDATION OVER VALUES AND THROWING CUSTOM ERROR MESSAGE TO VIEW

# TODO:4 DEPOSIT

# TODO:5 DELETE ACCOUNT, make sure that if an account has a saving account, it is deleted as well


# REDIRECTING EXAMPLE FOR ACCOUNT CREATE
@app.route('/account/<acc_id>/details')
def c_account(acc_id):
    user_obj = Account.query.get(acc_id)
    return render_template('account.html', data=user_obj)

# INDEX ROUTE
@app.route('/')
def index(data=None):
    return render_template('index.html', data=Account.query.count())
