# LIBRARIES
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect


# MY LIBRARIES
from module import dbLogic

app = Flask(__name__)

APP_ADDRESS = "127.0.0.1"
APP_PORT = 80

# URL POVEZAVE
URL_DNEVNIK = "http://" + str(APP_ADDRESS) + ":" + str(APP_PORT) + "/dnevnik"

# GLAVNI ROUTE APLIKACIJE

@app.route("/", methods = ["GET", "POST"])
def index():
    data = {
        "uspeh" : False,
        "itm" : None,
        "teza": "",
        "visina": ""
    }
    if request.method == "POST":
        data["teza"] = request.form.get("teza")
        data["visina"] = request.form.get("visina")
        
        if data["teza"] and data["visina"]:
            data["itm"] = izracunaj_itm(float(data["visina"]), float(data["teza"]))
            dbLogic.insertData(float(data["visina"]), float(data["teza"]), data["itm"])
        print(data)
    
    return render_template("index.html", podatki = data)

@app.route("/dnevnik", methods = ["GET", "POST"])
def dnevnik():
    data = {
        "seznam" : [],
    }
    data["seznam"] = dbLogic.getAll()
    return render_template("dnevnik.html", podatki = data)
    
# NOVO !!!
@app.route("/izbrisi/<sID>")
def dnevnik_izbirsi(sID):
    ID = int(sID)
    dbLogic.deleteItm(ID)
    # OBVETNO POSKRBI DA JE ZGORAJ NAPISAN IMPORT in KONSTANTA
    return redirect(URL_DNEVNIK)

def izracunaj_itm(visinaCm, tezaKg):
    itm = tezaKg / (visinaCm/100) ** 2
    return itm

# ZAGON APLIKACIJE
app.config["DEBUG"] = True
app.run(host = APP_ADDRESS, port = APP_PORT)