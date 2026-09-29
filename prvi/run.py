#System libaries
from flask import Flask
from flask import render_template
from flask import request

#my libaries
from module import dbConfig
from module import dbLogic

app = Flask(__name__)

APP_ADDRESS = "0.0.0.0"
APP_PORT = 80

# GLAVNI ROUTE APLIKACIJE

@app.route("/", methods = ["GET", "POST"])
def index():
    data = {
        "uspeh" : False,
        "itm": None,
        "teza": None,
        "visina": None
    }
    data["uspeh"] = dbLogic.getAll()
    if request.method == "POST":
        data["teza"] = request.form.get("teza")
        data["visina"] = request.form.get("visina")
        
        if data["visina"] and data["teza"]:
            data["itm"] = izracunaj_itm(float(data["visina"]), float(data["teza"]))
        print(data)
    
    return render_template("index.html", podatki = data)
    
def izracunaj_itm(visinaCm, tezaKg):
    itm = tezaKg / (visinaCm/100) ** 2
    return itm


# ZAGON APLIKACIJE
app.config["DEBUG"] = True
app.run(host = APP_ADDRESS, port = APP_PORT)
