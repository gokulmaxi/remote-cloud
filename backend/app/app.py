#!/usr/bin/python3
"""flask api for remote containers."""
from flask import Flask, jsonify
import docker
from route.users_mgmt import user_mgmt
from db import db
from flask import Flask
from flask_cors import CORS, cross_origin

users = {"foo@bar.tld": {"password": "secret"}}
app = Flask(__name__)
app.config["CORS_HEADERS"] = "Content-Type"
app.config[
    "MONGO_URI"
] = "mongodb://mongouser:mongoPass@mongodb:27017/mydatabase?authSource=admin"
cors = CORS(app)
app.secret_key = "super secret string"  # Change this!
app.register_blueprint(user_mgmt)
client = docker.from_env()


if __name__ == "__main__":
    app.config[
        "MONGO_URI"
    ] = "mongodb://mongouser:mongoPass@mongodb:27017/?authMechanism=DEFAULT"
    # config['PROD']['DB_URI']
    app.run(debug=True)
