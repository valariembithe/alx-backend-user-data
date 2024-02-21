#!/usr/bin/env python3
'''Task 6 module '''
from flask import Flask, jsonify, request, abort, redirect


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    '''Index page '''
    return jsonify({"message": "Bienvenue"})

@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    ''' Creates an account '''
    email, password = request.form.get("email"), request.form.get('password')
    try:
        Auth.register_user(email, password)
        return jsonify({'email': email, "message": "User created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
