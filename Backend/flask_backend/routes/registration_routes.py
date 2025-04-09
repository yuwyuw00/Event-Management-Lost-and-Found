from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.registration_model import register_user_for_event

registration_bp = Blueprint('register', __name__)

@registration_bp.route('/', methods=['POST'])
@jwt_required()
def register():
    data = request.json
    identity = get_jwt_identity()
    mongo = request.environ['app'].mongo
    register_user_for_event(mongo, identity['username'], data['event_id'])
    return jsonify({'msg': 'Registered for event'}), 201