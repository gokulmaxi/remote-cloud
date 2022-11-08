#!/usr/bin/env python3
"""User management route for cloud app."""
from flask import Blueprint, jsonify, current_app, request
from db import db
from utils.json_handler import parse_json

user_mgmt = Blueprint("users", __name__)


@user_mgmt.route("/")
def index():
    """Just found."""
    return "This is an example app"


@user_mgmt.route("/api/signin", methods=["POST"])
def create_user():
    """Redirects to default route."""
    raw_data = request.get_json()
    user = raw_data["email"]
    id = db.db.users.find_one({"email": user})
    data = parse_json(id)
    return jsonify(data)
