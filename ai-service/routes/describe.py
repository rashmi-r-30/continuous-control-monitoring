from flask import Blueprint, request, jsonify

# Create blueprint
describe_bp = Blueprint('describe', __name__)

# Create route
@describe_bp.route('/', methods=['POST'])
def describe():
    data = request.json

    return jsonify({
        "message": "Describe endpoint working",
        "received_data": data
    })