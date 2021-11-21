from . import main
from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin


@main.route("/")
def hello_world():
    return "Hello World!"


@main.route("/cors")
@cross_origin()
def cors_test():
    return jsonify({'data': 'Hello from flask with cors'})
