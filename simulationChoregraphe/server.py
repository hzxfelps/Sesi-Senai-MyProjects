from flask import Flask, request, jsonify

app = Flask(__name__)

grupos = {}

@app.route("/update", methods=["GET"])
def update():
    grupo = request.args.get("grupo")
    nivel = request.args.get("nivel")

    if grupo and nivel:
        grupos[int(grupo)] = int(nivel)

    return {"status": "ok", "dados": grupos}


@app.route("/next", methods=["GET"])
def get_next():
    if not grupos:
        return {"grupo": None, "nivel": None}

    # menor nível = mais prioridade
    g = min(grupos, key=grupos.get)

    return {
        "grupo": g,
        "nivel": grupos[g]
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)