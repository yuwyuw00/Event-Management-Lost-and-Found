from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.event_model import create_event, get_all_events

event_bp = Blueprint('events', __name__)

@event_bp.route('/', methods=['POST'])
@jwt_required()
def add_event():
    identity = get_jwt_identity()
    if identity['role'] != 'admin':
        return jsonify({'msg': 'Admins only'}), 403
    mongo = request.environ['app'].mongo
    create_event(mongo, request.json)
    return jsonify({'msg': 'Event created'}), 201

@event_bp.route('/', methods=['GET'])
def list_events():
    mongo = request.environ['app'].mongo
    events = get_all_events(mongo)
    return jsonify(events), 200