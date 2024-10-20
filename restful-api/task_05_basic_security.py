#!/usr/bin/python3

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    create_access_token, get_jwt_identity, jwt_required, JWTManager
)

# Users dictionary storing usernames, hashed passwords, and roles
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

app = Flask(__name__)
auth = HTTPBasicAuth()

# Configure JWT secret key
app.config["JWT_SECRET_KEY"] = "my_secret_key"
jwt = JWTManager(app)


@auth.verify_password
def verify_credentials(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted", 200


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # Check for missing username or password
    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # Create a JWT token with user role
        access_token = create_access_token(
            identity={"username": username, "role": user["role"]}
        )
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Bad username or password"}), 401


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted", 200


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()

    # Check if the current user is an admin
    if current_user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted", 200


# Error handling for unauthorized access
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


# Error handling for invalid tokens
@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


# Error handling for expired tokens
@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


# Error handling for revoked tokens
@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


# Error handling for tokens that need to be fresh
@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
