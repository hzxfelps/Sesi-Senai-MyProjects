from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

estado_escuta = False

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/laser")
def laser():
    return render_template("laser.html")

@app.route("/biologia")
def biologia():
    return render_template("biologia.html")

@app.route("/estado")
def estado():
    global estado_escuta

    ouvir = request.args.get("ouvindo")

    if ouvir is not None:
        estado_escuta = (ouvir == "1")

    return jsonify({"ouvindo": estado_escuta})

app.run(host="0.0.0.0", port=5000)