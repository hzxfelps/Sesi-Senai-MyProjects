from flask import Flask, request, jsonify, render_template
import time

app = Flask(__name__)

grupos = {}
historico = {}
estado_escuta = False


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/update")
def update():
    grupo = int(request.args.get("grupo"))
    nivel = int(request.args.get("nivel"))

    grupos[grupo] = nivel
    historico[grupo] = time.time()

    print("Grupos:", grupos)

    return jsonify({"status": "ok", "dados": grupos})


@app.route("/estado")
def estado():
    global estado_escuta

    ouvir = request.args.get("ouvindo")

    if ouvir is not None:
        estado_escuta = (ouvir == "1")

    return jsonify({"ouvindo": estado_escuta})


@app.route("/next")
def get_next():
    if not grupos:
        return jsonify({"grupo": None})

    # prioridade: menor nível + mais tempo esperando
    g = min(grupos, key=lambda x: (grupos[x], historico[x]))

    return jsonify({
        "grupo": g,
        "nivel": grupos[g]
    })


app.run(host="0.0.0.0", port=5000)