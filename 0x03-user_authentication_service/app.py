#!/usr/bin/env python3
'''Task 6 module '''
from flask import Flask, jsonify, request, abort, redirect


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    '''Index page '''
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
