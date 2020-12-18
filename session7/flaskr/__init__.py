import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from functools import wraps
from jose import jwt
from urllib.request import urlopen
import json

from models import setup_db, Account


def create_app(test_config=None):
  # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # @app.after_request
    # def after_request(response):
    #     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    #     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    #     return response
    # __________________________________________________AUTH0__________________________________________________

    AUTH0_DOMAIN = 'felgoal.eu.auth0.com'
    ALGORITHMS = ['RS256']
    API_AUDIENCE = 'sawsan'

    class AuthError(Exception):
        def __init__(self, error, status_code):
            self.error = error
            self.status_code = status_code

    def verify_decode_jwt(token):
        # GET THE PUBLIC KEY FROM AUTH0
        jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
        jwks = json.loads(jsonurl.read())
        # print (jwks) 
        # GET THE DATA IN THE HEADER
        unverified_header = jwt.get_unverified_header(token)

        # CHOOSE OUR KEY
        rsa_key = {}
        if 'kid' not in unverified_header:
            raise AuthError({
                'code': 'invalid_header',
                'description': 'Authorization malformed.'
            }, 401)

        for key in jwks['keys']:
            if key['kid'] == unverified_header['kid']:
                rsa_key = {
                    'kty': key['kty'],
                    'kid': key['kid'],
                    'use': key['use'],
                    'n': key['n'],
                    'e': key['e']
                }

        # Finally, verify!!!
        if rsa_key:
            try:
                # USE THE KEY TO VALIDATE THE JWT
                payload = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=ALGORITHMS,
                    audience=API_AUDIENCE,
                    issuer='https://' + AUTH0_DOMAIN + '/'
                )

                return payload

            except jwt.ExpiredSignatureError:
                raise AuthError({
                    'code': 'token_expired',
                    'description': 'Token expired.'
                }, 401)

            except jwt.JWTClaimsError:
                raise AuthError({
                    'code': 'invalid_claims',
                    'description': 'Incorrect claims. Please, check the audience and issuer.'
                }, 401)
            except Exception:
                raise AuthError({
                    'code': 'invalid_header',
                    'description': 'Unable to parse authentication token.'
                }, 400)
        raise AuthError({
            'code': 'invalid_header',
                    'description': 'Unable to find the appropriate key.'
        }, 400)
        # ____________________________________________________________________________________________________

    # ___________________________________________________AUTH___________________________________________________

    def get_token_auth_header():
        # Check if Authorization is present in the header or not
        if 'Authorization' not in request.headers:
            abort(401)

        auth_header = request.headers['Authorization'].split(' ')
        # print(auth_header)

        if len(auth_header) != 2:
            abort(401)
        elif auth_header[0].lower() != 'bearer':
            abort(401)

        return auth_header[1]

    # TODO implement the requires_auth decorator. Make sure that you get a customed error, not a 500 server error.  
    # ______________________________________________________________________________________________________

    @app.route('/')
    @requires_auth
    def index(jwt):
        return jsonify({
            'success': True,
            'message': 'Hello Udacians'
        })

    @app.route('/accounts')
    def retrieve_accounts():

        user_accounts = Account.query.count()

        # if user_accounts == 0:
        #     abort(404)

        return jsonify({
            'success': True,
            'total_accounts': user_accounts
        })

    @app.route('/accounts/<account_id>', methods=['PATCH'])
    def edit_account_first_name(account_id):
        account = Account.query.get(account_id)
        body = request.get_json()
        first_name = body.get("first_name", None)
        account.first_name = first_name
        account.update()
        return jsonify({'success': True, 'first_name': first_name})

    @app.route('/accounts/create', methods=['POST'])
    def create_account():
        body = request.get_json()
        first_name = body.get("first_name", None)
        last_name = body.get("last_name", None)
        init_balance = body.get("balance", None)
        search = body.get('search', None)

        # if first_name is None or last_name is None or init_balance is None:
        #     abort(400)

        res_body = {}

        # TDD Example
        if search:
            selection = Account.query.filter(
                Account.first_name.contains(search)).count()

            return jsonify({
                "success": True,
                "total_records": selection
            })

        else:
            error = False
            if first_name is None or init_balance is None:
                error = True
                abort(400)
            else:
                try:
                    new_account = Account(first_name=first_name,
                                          last_name=last_name, balance=init_balance)
                    new_account.insert()
                    res_body['created'] = new_account.id
                    res_body['first_name'] = new_account.first_name
                    res_body['last_name'] = new_account.last_name
                    res_body['balance'] = new_account.balance
                    res_body['success'] = True

                    return jsonify(res_body)

                except:
                    abort(422)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource Not Found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    @app.errorhandler(401)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unauthorized"
        }), 401

    return app
