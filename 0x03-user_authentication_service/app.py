#!/usr/bin/env python3
'''Task 6 module '''
from flask import Flask, jsonify, request, abort, redirect

from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    '''Index page '''
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    ''' Creates an account '''
    email, password = request.form.get("email"), request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({'email': email, "message": "User created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    ''' Login '''
    email, password = request.form.get('email'), request.form.get('password')
    if not AUTH.valid_login:
        abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie('session_id', session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
