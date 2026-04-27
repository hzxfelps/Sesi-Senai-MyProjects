from flask import Flask, request, jsonify, render_template
import time

app = Flask(__name__)

grupos = {}
historico = {}
estado_escuta = False

# ------------------------
# PÁGINAS
# ------------------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/laser")
def laser():
    return render_template("laser.html")

@app.route("/biologia")
def biologia():
    return render_template("biologia.html")

# ------------------------
# ESP32 ENVIA DADOS
# ------------------------

@app.route("/update")
def update():
    grupo = int(request.args.get("grupo"))
    nivel = int(request.args.get("nivel"))

    grupos[grupo] = nivel
    historico[grupo] = time.time()

    print("Grupos:", grupos)

    return jsonify({"ok": True})

# ------------------------
# BOTÃO DO HTML
# ------------------------

@app.route("/estado")
def estado():
    global estado_escuta

    ouvir = request.args.get("ouvindo")

    if ouvir is not None:
        estado_escuta = (ouvir == "1")

    return jsonify({"ouvindo": estado_escuta})

# ------------------------
# PEPPER PEGA PRÓXIMO GRUPO
# ------------------------

@app.route("/next")
def next():
    if not grupos:
        return jsonify({"grupo": None})

    g = min(grupos, key=lambda x: (grupos[x], historico[x]))

    return jsonify({
        "grupo": g,
        "nivel": grupos[g]
    })

# ------------------------

app.run(host="0.0.0.0", port=5000)