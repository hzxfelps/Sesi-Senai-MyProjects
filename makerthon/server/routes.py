from flask import Blueprint, request, jsonify
from logic import update_group, get_next_group

routes = Blueprint("routes", __name__)

# Recebe dados do ESP32
@routes.route("/data", methods=["POST"])
def receive_data():
    data = request.json
    update_group(data)
    return jsonify({"status": "ok"})


# Robô busca prioridade
@routes.route("/next", methods=["GET"])
def next_group():
    grupo, nivel = get_next_group()

    return jsonify({
        "grupo": grupo,
        "nivel": nivel
    })