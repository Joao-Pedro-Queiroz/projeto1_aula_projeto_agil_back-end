from flask import Flask, request
from flask_pymongo import PyMongo


"""app = Flask("nome_da_minha_aplicacao")
app.config["MONGO_URI"] = 
mongo = PyMongo(app)


@app.route('/usuarios', methods=['GET'])
def get_all_users():
    filtro = { "idade": { "$gt": 17 } }
    projecao = {"_id": 0}
    dados_usuarios = mongo.db.usuarios.find(filtro, projecao)

    resp = {
        "usuarios": list(dados_usuarios)
    }

    return resp, 200


if __name__ == '__main__':
    app.run(debug=True)"""