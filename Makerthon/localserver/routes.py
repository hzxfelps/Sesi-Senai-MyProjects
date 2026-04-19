from flask import Blueprint, request, jsonify
from logic import process_data

routes = Blueprint("routes", __name__)

@routes.route("/data", methods=["POST"])
def receive_data():
    data = request.json
    process_data(data)
    return jsonify({"status": "ok"})