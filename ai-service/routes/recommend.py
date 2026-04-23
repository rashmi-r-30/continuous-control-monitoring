from flask import Blueprint, request, jsonify

recommend_bp = Blueprint('recommend', __name__)

@recommend_bp.route('/', methods=['POST'])
def recommend():
    data = request.json

    return jsonify({
        "message": "Recommend endpoint working",
        "received_data": data
    })