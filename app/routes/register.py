import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from flask import Blueprint, request, jsonify
from utils.file_io import save_user

register_bp = Blueprint('register', __name__)

@register_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")

    if not username or not email:
        return jsonify({"error": "Username and email required"}), 400

    user = {"username": username, "email": email}
    success = save_user(user)

    if success:
        return jsonify({"message": f"User {username} registered!"}), 201
    else:
        return jsonify({"error": "User already exists"}), 409
