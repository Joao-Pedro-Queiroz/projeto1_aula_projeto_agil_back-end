from flask import Flask, jsonify, make_response
from pymongo import MongoClient
import certifi

# Conexão com o MongoDB Atlas
client = MongoClient("mongo_uri", tlsCAFile=certifi.where())
db = client["banco_de_dados"]

app = Flask(__name__)

@app.route('/usuarios', methods=['GET'])
def get_all_usuarios():
    # Define uma projeção para não incluir o campo "_id" nos resultados
    projecao = {"_id": 0}
    usuarios = list(db.usuarios_proj_agil.find({}, projecao))
    return make_response(jsonify(usuarios), 200)

@app.route('/entidades', methods=['GET'])
def get_all_entidades():
    # Define uma projeção para não incluir o campo "_id" nos resultados
    projecao = {"_id": 0}
    entidades = list(db.entidades_proj_agil.find({}, projecao))
    return make_response(jsonify(entidades), 200)

@app.route('/empresas', methods=['GET'])
def get_all_empresas():
    # Define uma projeção para não incluir o campo "_id" nos resultados
    projecao = {"_id": 0}
    empresas = list(db.empresas_proj_agil.find({}, projecao))
    return make_response(jsonify(empresas), 200)

if __name__ == '__main__':
    app.run(debug=True)