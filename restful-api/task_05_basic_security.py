from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt, get_jwt_identity
)

app = Flask(__name__)

# Configure JWT with a strong secret key.
app.config["JWT_SECRET_KEY"] = "your-strong-secret-key"  # Change this in production!
jwt = JWTManager(app)

# In-memory user store with hashed passwords and roles.
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

# Set up basic authentication.
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None

# Basic Authentication Protected Route.
@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return jsonify(message="Basic Auth: Access Granted"), 200

# Login endpoint for JWT Authentication.
@app.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    user = users.get(username, None)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"msg": "Bad username or password"}), 401

    # Include the user's role in the JWT payload.
    access_token = create_access_token(identity=username, additional_claims={"role": user["role"]})
    return jsonify(access_token=access_token), 200

# JWT Protected Route.
@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return jsonify(message="JWT Auth: Access Granted"), 200

# Role-based Protected Route: Only accessible to admin users.
@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify(error="Admin access required"), 403
    return jsonify(message="Admin Access: Granted"), 200

# Custom error handlers for JWT errors to ensure a consistent 401 status code.
@jwt.unauthorized_loader
def unauthorized_response(callback):
    return jsonify({"msg": "Missing or invalid Authorization Header"}), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({"msg": "Invalid token"}), 401

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"msg": "Token has expired"}), 401

if __name__ == "__main__":
    app.run(debug=True)
