from flask import Flask, request
from flask_pymongo import PyMongo

app = Flask(__name__)

# Configuração para conexão com o MongoDB
app.config["MONGO_URI"] = "mongodb+srv://gabrielprady1:RjNiPqINfNSV2xlX@cluster0.do8a1uo.mongodb.net/biblioteca_db"
mongo = PyMongo(app)

# Rotas para obter todos os usuários, entidades e empresas
@app.route('/usuarios', methods=['GET'])
def get_all_users():
    # Define um filtro vazio para obter todos os usuários
    filtro = {}
    # Define uma projeção para não incluir o campo "_id" nos resultados
    projecao = {"_id": 0}
    # Recupera os dados dos usuários do banco de dados MongoDB usando o filtro e a projeção definidos
    dados_usuarios = mongo.db.usuarios.find(filtro, projecao)
    # Cria uma resposta JSON contendo os usuários encontrados
    resp = {"usuarios": list(dados_usuarios)}
    # Retorna a resposta JSON e o código de status 200 (OK)
    return resp, 200

@app.route('/entidades', methods=['GET'])
def get_all_entities():
    # Define um filtro vazio para obter todas as entidades
    filtro = {}
    # Define uma projeção para não incluir o campo "_id" nos resultados
    projecao = {"_id": 0}
    # Recupera os dados das entidades do banco de dados MongoDB usando o filtro e a projeção definidos
    dados_entidades = mongo.db.entidades.find(filtro, projecao)
    # Cria uma resposta JSON contendo as entidades encontradas
    resp = {"entidades": list(dados_entidades)}
    # Retorna a resposta JSON e o código de status 200 (OK)
    return resp, 200

@app.route('/empresas', methods=['GET'])
def get_all_companies():
    # Define um filtro vazio para obter todas as empresas
    filtro = {}
    # Define uma projeção para não incluir o campo "_id" nos resultados
    projecao = {"_id": 0}
    # Recupera os dados das empresas do banco de dados MongoDB usando o filtro e a projeção definidos
    dados_empresas = mongo.db.empresas.find(filtro, projecao)
    # Cria uma resposta JSON contendo as empresas encontradas
    resp = {"empresas": list(dados_empresas)}
    # Retorna a resposta JSON e o código de status 200 (OK)
    return resp, 200

# Rotas para adicionar um novo usuário, entidade ou empresa
@app.route('/usuarios', methods=['POST'])
def add_user():
    # Define os dados do usuário a serem adicionados
    novo_usuario = request.json
    # Insere o usuário no banco de dados MongoDB
    mongo.db.usuarios.insert_one(novo_usuario)
    # Exemplo de chamada para adicionar um usuário
#     usuario = {
#     "cpf": "9999999999",
#     "curso": "Ciência da Computação",
#     "data_nascimento": "17/02/2002",
#     "entidades": [
#     "ALESP",
#     "ASD"
#     "ASDASDASD",
#     "ASDASDASDASDASD"
#     ],
#     "id": 2,
#     "interesses": [
#     "Python",
#     ],
#     "nome": "Altran",
#     "periodo": 10,
#     "projetos": [
#     "Projeto 4",
#     "Projeto 5",
#     "Projeto 6"
#     ]
# }
    # Retorna uma mensagem de sucesso e o código de status 201 (Criado)
    return {"mensagem": "Usuário adicionado com sucesso"}, 201

@app.route('/entidades', methods=['POST'])
def add_entity():
    # Define os dados da entidade a serem adicionados
    nova_entidade = request.json
    # Exemplo de chamada para adicionar uma entidade
    # usuario = {
    #     "apresentacao": "Entidade de teste 2",
    #     "area_atuacao": "557.243.189-49",
    #     "data_criacao": "17/02/2001",
    #     "id": 1,
    #     "info_contato": {
    #         "email": "abc@gmail.com",
    #         "linkedin": "linkedin.com",
    #         "telefone": "123456789"
    #     },
    #     "nome": "Entidade",
    #     "presidente": 'Gabriel Prady',
    #     "projetos": [
    #         "Projeto 1",
    #         "Projeto 2",
    #         "Projeto 3"
    #     ],
    #     "vice_presidente": "Engenharia de Software"
    # }
    # Insere a entidade no banco de dados MongoDB
    mongo.db.entidades.insert_one(nova_entidade)
    # Retorna uma mensagem de sucesso e o código de status 201 (Criado)
    return {"mensagem": "Entidade adicionada com sucesso"}, 201

@app.route('/empresas', methods=['POST'])
def add_company():
    # Define os dados da empresa a serem adicionados
    nova_empresa = request.json
    # Exemplo de chamada para adicionar uma empresa
    # usuario = {
    #     "apresentacao": "Apresentação 1",
    #     "cargo": "Diretor",
    #     "cnpj": "123456789",
    #     "email": "abc@gmail.com",
    #     "empresa": "17/02/2001",
    #     "id": 1,
    #     "info_contato": {
    #         "celular": "123456789",
    #         "linkedin": "www.linkedin.com",
    #         "site": "www.site.com"
    #     },
    #     "nome": "Recrutador"
    # }
    # Insere a empresa no banco de dados MongoDB
    mongo.db.empresas.insert_one(nova_empresa)
    # Retorna uma mensagem de sucesso e o código de status 201 (Criado)
    return {"mensagem": "Empresa adicionada com sucesso"}, 201

# Rotas para atualizar um usuário, entidade ou empresa existente
@app.route('/usuarios/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    # Obtém os novos dados do usuário
    novos_dados = request.json
    # Atualiza o usuário no banco de dados MongoDB usando o ID fornecido
    mongo.db.usuarios.update_one({"id": user_id}, {"$set": novos_dados})
    # Retorna uma mensagem de sucesso e o código de status 200 (OK)
    return {"mensagem": "Usuário atualizado com sucesso"}, 200

@app.route('/entidades/<int:entity_id>', methods=['PUT'])
def update_entity(entity_id):
    # Obtém os novos dados da entidade
    novos_dados = request.json
    # Atualiza a entidade no banco de dados MongoDB usando o ID fornecido
    mongo.db.entidades.update_one({"id": entity_id}, {"$set": novos_dados})
    # Retorna uma mensagem de sucesso e o código de status 200 (OK)
    return {"mensagem": "Entidade atualizada com sucesso"}, 200

@app.route('/empresas/<int:company_id>', methods=['PUT'])
def update_company(company_id):
    # Obtém os novos dados da empresa
    novos_dados = request.json
    # Atualiza a empresa no banco de dados MongoDB usando o ID fornecido
    mongo.db.empresas.update_one({"id": company_id}, {"$set": novos_dados})
    # Retorna uma mensagem de sucesso e o código de status 200 (OK)
    return {"mensagem": "Empresa atualizada com sucesso"}, 200

# Rotas para excluir um usuário, entidade ou empresa
@app.route('/usuarios/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Remove o usuário do banco de dados MongoDB usando o ID fornecido
    mongo.db.usuarios.delete_one({"id": user_id})
    # Retorna uma mensagem de sucesso e o código de status 200 (OK)
    return {"mensagem": "Usuário removido com sucesso"}, 200

@app.route('/entidades/<int:entity_id>', methods=['DELETE'])
def delete_entity(entity_id):
    # Remove a entidade do banco de dados MongoDB usando o ID fornecido
    mongo.db.entidades.delete_one({"id": entity_id})
    # Retorna uma mensagem de sucesso e o código de status 200 (OK)
    return {"mensagem": "Entidade removida com sucesso"}, 200

@app.route('/empresas/<int:company_id>', methods=['DELETE'])
def delete_company(company_id):
    # Remove a empresa do banco de dados MongoDB usando o ID fornecido
    mongo.db.empresas.delete_one({"id": company_id})
    # Retorna uma mensagem de sucesso e o código de status 200 (OK)
    return {"mensagem": "Empresa removida com sucesso"}, 200

if __name__ == "__main__":
    # Executa a aplicação Flask em modo de depuração
    app.run(debug=True)
