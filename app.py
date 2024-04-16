from flask import Flask, request
from flask_pymongo import PyMongo


app = Flask("nome_da_minha_aplicacao")
app.config["MONGO_URI"] = "mongodb+srv://admin:admin@cluster0.pxnlzfp.mongodb.net/biblioteca_db"
mongo = PyMongo(app)


@app.route('/usuarios', methods=['DELETE'])
def remover_usuario():
    # Define um filtro para encontrar o usuário com CPF "12345678901"
    filtro = {
        "id": 2
    }
    # Remove o usuário do banco de dados MongoDB
    mongo.db.usuarios_proj_agil.delete_one(filtro)
    # Retorna uma mensagem de sucesso e o código de status 200 (OK)
    return {"mensagem": "Usuário removido com sucesso"}, 200

@app.route('/entidades', methods=['DELETE'])
def remover_entidade():
    # Define um filtro para encontrar a entidade com CNPJ "12345678901234"
    filtro = {
        "id": 0
    }
    # Remove a entidade do banco de dados MongoDB
    mongo.db.entidades_proj_agil.delete_one(filtro)
    # Retorna uma mensagem de sucesso e o código de status 200 (OK)
    return {"mensagem": "Entidade removida com sucesso"}, 200

@app.route('/empresas', methods=['DELETE'])
def remover_empresa():
    # Define um filtro para encontrar a empresa com CNPJ "12345678901234"
    filtro = {
        "id": 0
    }
    # Remove a empresa do banco de dados MongoDB
    mongo.db.empresas_proj_agil.delete_one(filtro)
    # Retorna uma mensagem de sucesso e o código de status 200 (OK)
    return {"mensagem": "Empresa removida com sucesso"}, 200


if __name__ == '__main__':
    app.run(debug=True)