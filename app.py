from flask import Flask, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://gabrielprady1:RjNiPqINfNSV2xlX@cluster0.do8a1uo.mongodb.net/biblioteca_db"
mongo = PyMongo(app)

@app.route('/usuarios', methods=['GET'])
def get_all_users():
    filtro = {
    }
    # Define uma projeção para não incluir o campo "_id" nos resultados
    projecao = {"_id": 0}
    # Recupera os dados dos usuários do banco de dados MongoDB usando o filtro e a projeção definidos
    dados_usuarios = mongo.db.usuarios_proj_agil.find(filtro, projecao)
    # Cria uma resposta JSON contendo os usuários encontrados
    resp = {
        "usuarios": list(dados_usuarios),
    }
    # Retorna a resposta JSON e o código de status 200 (OK)
    return resp, 200

@app.route('/entidades', methods=['GET'])
def get_all_entidades():
    filtro = {
    }
    # Define uma projeção para não incluir o campo "_id" nos resultados
    projecao = {"_id": 0}
    # Recupera os dados dos usuários do banco de dados MongoDB usando o filtro e a projeção definidos
    dados_entidades = mongo.db.entidades_proj_agil.find(filtro, projecao)
    # Cria uma resposta JSON contendo os usuários encontrados
    resp = {
        "usuarios": list(dados_entidades),
    }
    # Retorna a resposta JSON e o código de status 200 (OK)
    return resp, 200

@app.route('/empresas', methods=['GET'])
def get_all_recrutadores():
    filtro = {
    }
    # Define uma projeção para não incluir o campo "_id" nos resultados
    projecao = {"_id": 0}
    # Recupera os dados dos usuários do banco de dados MongoDB usando o filtro e a projeção definidos
    dados_empresas = mongo.db.recrutadores_proj_agil.find(filtro, projecao)
    # Cria uma resposta JSON contendo os usuários encontrados
    resp = {
        "usuarios": list(dados_empresas),
    }
    # Retorna a resposta JSON e o código de status 200 (OK)
    return resp, 200

@app.route('/usuarios', methods=['POST'])
def adicionar_usuario():
    # Define os dados do usuário a serem adicionados
    usuario = {
      "cpf": "9999999999",
      "curso": "Ciência da Computação",
      "data_nascimento": "17/02/2002",
      "entidades": [
        "ALESP",
        "ASD"
        "ASDASDASD",
        "ASDASDASDASDASD"
      ],
      "id": 2,
      "interesses": [
        "Python",
      ],
      "nome": "Altran",
      "periodo": 10,
      "projetos": [
        "Projeto 4",
        "Projeto 5",
        "Projeto 6"
      ]
    }
    # Insere o usuário no banco de dados MongoDB
    mongo.db.usuarios_proj_agil.insert_one(usuario)
    # Retorna uma mensagem de sucesso e o código de status 201 (Criado)
    return {"mensagem": "Usuário adicionado com sucesso"}, 201

@app.route('/entidades', methods=['POST'])
def adicionar_entidade():
    # Define os dados do usuário a serem adicionados
    usuario = {
            "apresentacao": "Entidade de teste 2",
            "area_atuacao": "557.243.189-49",
            "data_criacao": "17/02/2001",
            "id": 1,
            "info_contato": {
                "email": "abc@gmail.com",
                "linkedin": "linkedin.com",
                "telefone": "123456789"
            },
            "nome": "Entidade",
            "presidente": 'Gabriel Prady',
            "projetos": [
                "Projeto 1",
                "Projeto 2",
                "Projeto 3"
            ],
            "vice_presidente": "Engenharia de Software"
        }
    # Insere o usuário no banco de dados MongoDB
    mongo.db.entidades_proj_agil.insert_one(usuario)
    # Retorna uma mensagem de sucesso e o código de status 201 (Criado)
    return {"mensagem": "Entidade adicionada com sucesso"}, 201

@app.route('/empresas', methods=['POST'])
def adicionar_empresas():
    # Define os dados do usuário a serem adicionados
    usuario = {
            "apresentacao": "Apresentação 1",
            "cargo": "Diretor",
            "cnpj": "123456789",
            "email": "abc@gmail.com",
            "empresa": "17/02/2001",
            "id": 1,
            "info_contato": {
                "celular": "123456789",
                "linkedin": "www.linkedin.com",
                "site": "www.site.com"
            },
            "nome": "Recrutador"
        }
    # Insere o usuário no banco de dados MongoDB
    mongo.db.recrutadores_proj_agil.insert_one(usuario)
    # Retorna uma mensagem de sucesso e o código de status 201 (Criado)
    return {"mensagem": "Empresa adicionada com sucesso"}, 201

if __name__:
    app.run(debug=True)
    

