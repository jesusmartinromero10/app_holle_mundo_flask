from flask import Flask, render_template


app = Flask(__name__)

@app.route("/hola") #conecta el servidor con python en primeraentrada 

def primeraentrada():
    return "hola mundo"

@app.route("/adios")
def salida():
    return "Hasta luego pecadorrrrrrrrrr"

@app.route("/doble/<int:numero>") #si ponemos entre <> un nombre se convierte en la variable de la funcion
def doble(numero):
    return str(numero * 2)

@app.route("/primerhtml")
def primerhtml():
    return render_template("hola.html") #busca el html