from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models.user_model import get_user_by_username, create_user
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    mongo = request.environ['app'].mongo
    if get_user_by_username(mongo, data['username']):
        return jsonify({'msg': 'Username already exists'}), 400
    hashed_password = generate_password_hash(data['password'])
    create_user(mongo, {'username': data['username'], 'password': hashed_password, 'role': 'user'})
    return jsonify({'msg': 'User created'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    mongo = request.environ['app'].mongo
    user = get_user_by_username(mongo, data['username'])
    if not user or not check_password_hash(user['password'], data['password']):
        return jsonify({'msg': 'Invalid credentials'}), 401
    access_token = create_access_token(identity={'username': user['username'], 'role': user['role']})
    return jsonify(access_token=access_token), 200