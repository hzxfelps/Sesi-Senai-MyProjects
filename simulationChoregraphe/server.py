from flask import Flask, request, jsonify

app = Flask(__name__)

grupos = {}
estado_escuta = False


@app.route("/update", methods=["GET"])
def update():
    grupo = request.args.get("grupo")
    nivel = request.args.get("nivel")

    if grupo and nivel:
        grupos[int(grupo)] = int(nivel)

    return jsonify({"status": "ok", "dados": grupos})


@app.route("/estado", methods=["GET"])
def estado():
    global estado_escuta

    ouvir = request.args.get("ouvindo")

    if ouvir is not None:
        estado_escuta = (ouvir == "1")

    return jsonify({"ouvindo": estado_escuta})


@app.route("/next", methods=["GET"])
def get_next():
    if not grupos:
        return jsonify({"grupo": None, "nivel": None})

    # pega o grupo com menor nível
    g = min(grupos, key=grupos.get)

    nivel = grupos.pop(g)  # REMOVE após uso

    return jsonify({
        "grupo": g,
        "nivel": nivel
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)