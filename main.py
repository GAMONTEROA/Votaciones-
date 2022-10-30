from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorResultado import ControladorResultado

import pymongo
import certifi

app=Flask(__name__)
cors = CORS(app)

ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://gamonteroa:Montero2022@cluster0.ftrqujn.mongodb.net/res_votaciones?retryWrites=true&w=majority",tlsCAFile=ca)
db = client.test
print(db)

baseDatos = client["res_votaciones"]
print(baseDatos.list_collection_names())

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

#anotacion para declarar que el servicio def test se ejecuta cuando el metodo = a get

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

#Declarar controladores

ControladorCandidato=ControladorCandidato()
ControladorPartido=ControladorPartido()
ControladorMesa=ControladorMesa()
ControladorResultado=ControladorResultado()

@app.route("/candidatos",methods=['GET'])
def getCandidatos():
    json=ControladorCandidato.index()
    return jsonify(json)

@app.route("/candidatos",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json=ControladorCandidato.create(data)
    return jsonify(json)

@app.route("/candidatos/<string:id>",methods=['GET'])
def getCandidato(id):
    json=ControladorCandidato.show(id)
    return jsonify(json)

@app.route("/candidatos/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json=ControladorCandidato.update(id,data)
    return jsonify(json)

@app.route("/candidatos/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    json=ControladorCandidato.delete(id)
    return jsonify(json)

####Partidos####

@app.route("/partidos",methods=['GET'])
def getPartidos():
    json=ControladorPartido.index()
    return jsonify(json)

@app.route("/partidos",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json=ControladorPartido.create(data)
    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['GET'])
def getPartido(id):
    json=ControladorPartido.show(id)
    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=ControladorPartido.update(id,data)
    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=ControladorPartido.delete(id)
    return jsonify(json)

####Mesas####

@app.route("/mesas",methods=['GET'])
def getMesas():
    json=ControladorMesa.index()
    return jsonify(json)

@app.route("/mesas",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json=ControladorMesa.create(data)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['GET'])
def getMesa(id):
    json=ControladorMesa.show(id)
    return jsonify(json)

@app.route("/mesas/<string:id>",methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json=ControladorMesa.update(id,data)
    return jsonify(json)

@app.route("/mesas/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    json=ControladorMesa.delete(id)
    return jsonify(json)

######Asignar Partido a Candidato #######
@app.route("/candidatos/<string:id>/partido/<string:id_partido>",methods=['PUT'])
def asignarPartidoaCandidato(id,id_partido):
    json=ControladorCandidato.asignarPartido(id,id_partido)
    return jsonify(json)

###### Resultados #######

@app.route("/resultados",methods=['GET'])
def getResultados():
    json=ControladorResultado.index()
    return jsonify(json)
@app.route("/resultados/<string:id>",methods=['GET'])
def getResultado(id):
    json=ControladorResultado.show(id)
    return jsonify(json)
@app.route("/resultados/candidato/<string:id_candidato>/mesa/<string:id_mesa>",methods=['POST'])
def crearResultado(id_candidato,id_mesa):
    data = request.get_json()
    json=ControladorResultado.create(data,id_candidato,id_mesa)
    return jsonify(json)
@app.route("/resultados/<string:id_resultado>/candidato/<string:id_candidato>/mesa/<string:id_mesa>",methods=['PUT'])
def modificarResultado(id_resultado,id_candidato,id_mesa):
    data = request.get_json()
    json=ControladorResultado.update(id_resultado,data,id_candidato,id_mesa)
    return jsonify(json)
@app.route("/resultados/<string:id_resultado>",methods=['DELETE'])
def eliminarResultado(id_resultado):
    json=ControladorResultado.delete(id_resultado)
    return jsonify(json)
@app.route("/resultados/mesa/<string:id_mesa>",methods=['GET'])
def votosporCandidato(id_mesa,id_candidato):
    json=ControladorResultado.votosporCandidato(id_mesa,id_candidato)
    return jsonify(json)
@app.route("/resultados/participacion",methods=['GET'])
def mesasMayorParticipacion():
    json=ControladorResultado.mesasMayorParticipacion()
    return jsonify(json)
@app.route("/resultados/promedio_notas/materia/<string:id_materia>",methods=['GET'])
def getParticipacionporPartido(id_partido):
    json=ControladorResultado.votosporPartido(id_partido)
    return jsonify(json)


if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])


