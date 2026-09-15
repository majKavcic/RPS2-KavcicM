from flask import Flask
from flask import render_template

app = Flask(__name__)

APP_ADDRESS = "0.0.0.0"
APP_PORT = 80

# GLAVNI ROUTE APLIKACIJE

@app.route("/", methods = ["GET", "POST"])
def hello_world():
    return render_template("index.html")


# ZAGON APLIKACIJE
app.config["DEBUG"] = True
app.run(host = APP_ADDRESS, port = APP_PORT)

