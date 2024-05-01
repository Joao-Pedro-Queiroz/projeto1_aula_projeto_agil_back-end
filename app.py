from flask import Flask, Response, jsonify, request, abort
from flask_pymongo import PyMongo
from datetime import date
import os
from auth import not_authenticated, hash_password
from functools import wraps
# Aplicação Flask e Mongo
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://admin:admin@cluster0.hmjqwho.mongodb.net/projeto1_agil"
mongo = PyMongo(app)

def check_auth(username, password):
    """Verifica se as credenciais de usuário e senha são válidas."""
    hashed_password = hash_password(password)
    filtro_ = {"nome": username, "password": hashed_password}
    print(filtro_)
    usuario = mongo.db.usuarios.find_one(filter=filtro_)
    print(usuario)
    return bool(usuario)

def requires_auth(f):
    """Decorador que protege rotas específicas com autenticação básica.
    Args:
        f (function): A função da rota Flask a ser decorada.
    Returns:
        function: A função decorada que agora inclui verificação de autenticação.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return not_authenticated()
        return f(*args, **kwargs)
    return decorated

# Função para obter o usuário atual
def get_current_user():
    # Obtem as credenciais de autenticação do cabeçalho da solicitação
    auth = request.authorization
    if not auth: # Se não houver credenciais de autenticação, retorne None
        return None
    # Procura o usuário no banco de dados pelo e-mail fornecido
    return mongo.db.usuarios.find_one({"email": auth.email})


##### FUNÇÕES DO TIPO GET #####

#CHECK
@app.route('/usuarios', methods=['GET'])
@requires_auth
def get_all_users():
    filtro = {
    }
    # Define uma projeção para não incluir o campo "_id" nos resultados
    projecao = {"_id": 0}
    # Recupera os dados dos usuários do banco de dados MongoDB usando o filtro e a projeção definidos
    dados_usuarios = mongo.db.usuarios.find(filtro, projecao)
    # Cria uma resposta JSON contendo os usuários encontrados
    resp = {
        "usuarios": list(dados_usuarios),
    }
    # Retorna a resposta JSON e o código de status 200 (OK)
    return resp, 200

#CHECK
@app.route('/entidades', methods=['GET'])
def get_all_entidades():
    filtro = {
    }
    # Define uma projeção para não incluir o campo "_id" nos resultados
    projecao = {"_id": 0}
    # Recupera os dados dos usuários do banco de dados MongoDB usando o filtro e a projeção definidos
    dados_entidades = mongo.db.entidades.find(filtro, projecao)
    # Cria uma resposta JSON contendo os usuários encontrados
    resp = {
        "entidades": list(dados_entidades),
    }
    # Retorna a resposta JSON e o código de status 200 (OK)
    return resp, 200


# Função que busca usuarios através do campo "nome"
#CHECK
@app.route('/usuarios/<string:nome>', methods=['GET'])
@requires_auth
def get_user_by_name(nome):
    # Define um filtro para encontrar o usuário com o nome especificado
    filtro = {
        "nome": nome
    }
    # Define uma projeção para não incluir o campo "_id" nos resultados
    projecao = {"_id": 0}
    # Recupera os dados do usuário do banco de dados MongoDB usando o filtro e a projeção definidos
    dados_usuarios = mongo.db.usuarios.find(filtro, projecao)
    # Cria uma resposta JSON contendo o usuário encontrado
    resp = {
        "usuario": list(dados_usuarios),
    }
    # Retorna a resposta JSON e o código de status 200 (OK)
    return resp, 200

# Função que busca entidades através do campo "nome"
#CHECK
@app.route('/entidades/<string:nome>', methods=['GET'])
def get_entidade_by_name(nome):
    # Define um filtro para encontrar a entidade com o nome especificado
    filtro = {
        "nome": nome
    }
    # Define uma projeção para não incluir o campo "_id" nos resultados
    projecao = {"_id": 0}
    # Recupera os dados da entidade do banco de dados MongoDB usando o filtro e a projeção definidos
    dados_entidades = mongo.db.entidades.find(filtro, projecao)
    # Cria uma resposta JSON contendo a entidade encontrada
    resp = {
        "entidade": list(dados_entidades),
    }
    # Retorna a resposta JSON e o código de status 200 (OK)
    return resp, 200


##### FUNÇÕES DO TIPO DELETE #####
#check
@app.route('/usuarios/<string:nome>', methods=['DELETE'])
@requires_auth
def remover_usuario(nome):
    # Define um filtro para encontrar o usuário com CPF "12345678901"
    filtro = {
        "nome": nome
    }
    # Remove o usuário do banco de dados MongoDB
    mongo.db.usuarios.delete_one(filtro)
    # Retorna uma mensagem de sucesso e o código de status 200 (OK)
    return {"mensagem": "Usuário removido com sucesso"}, 200

#chcek
@app.route('/entidades/<string:nome>', methods=['DELETE'])
@requires_auth
def remover_entidade(nome):
    # Define um filtro para encontrar a entidade com CNPJ "12345678901234"
    filtro = {
        "nome": nome
    }
    # Remove a entidade do banco de dados MongoDB
    mongo.db.entidades.delete_one(filtro)
    # Retorna uma mensagem de sucesso e o código de status 200 (OK)
    return {"mensagem": "Entidade removida com sucesso"}, 200


##### FUNÇÕES DO TIPO PUT #####

#chcek
@app.route('/usuarios/<string:email>', methods=['PUT'])
@requires_auth
def editar_usuario(email):
    # Define um filtro para encontrar o usuário com o e-mail especificado
    filtro = {"email": email}
    try: # Tente acessar o banco de dados para recuperar os dados do usuário
        # Define uma projeção para não incluir o campo "_id" nos resultados
        projecao = {"_id": 0}
        # Recupera os dados do usuário do banco de dados MongoDB usando o filtro e a projeção definidos
        dados_usuarios = list(mongo.db.usuarios.find(filtro, projecao))
    except: # Se ocorrer um erro ao acessar o banco de dados, retorne um erro 500 (Erro interno do servidor)
        return {"erro": "Erro no sistema"}, 500
    else: # Se os dados do usuário forem encontrados
        if dados_usuarios == []:# Se o usuário não for encontrado, retorne um erro 404 (Não encontrado)
            return {"erro": "Usuário não encontrado"}, 404
        else: # Se o usuário for encontrado
            data = request.json
            pswd = data["password"]
            data["password"] = hash_password(pswd)
            novos_dados = {
                "$set": data
            }
            try: # Tente atualizar os dados do usuário no banco de dados
                mongo.db.usuarios.update_one(filtro, novos_dados)
            except: # Se ocorrer um erro ao atualizar os dados do usuário, retorne um erro 400 (Solicitação inválida)
                return {"erro": "Dados inválidos"}, 400
            return {"mensagem": "Usuário atualizado com sucesso"}, 200

#check
@app.route('/entidades/<string:email>', methods=['PUT'])
@requires_auth
def editar_entidade(email):
    # Define um filtro para encontrar a entidade com o e-mail especificado
    filtro = {"email": email}
    # Tente acessar o banco de dados para recuperar os dados da entidade
    try:
        projecao = {"_id": 0}
        dados_entidades = list(mongo.db.entidades.find(filtro, projecao))
    except: # Se ocorrer um erro ao acessar o banco de dados, retorne um erro 500 (Erro interno do servidor)
        return {"erro": "Erro no sistma"}, 500
    else: # Se os dados da entidade forem encontrados
        if dados_entidades == []:
            return {"erro": "Entidades não encontrado"}, 404
        else: # Se a entidade for encontrada
            data = request.json
            pswd = data["password"]
            data["password"] = hash_password(pswd)
            novos_dados = {
                "$set": data
            }
            try: # Tente atualizar os dados da entidade no banco de dados
                mongo.db.entidades.update_one(filtro, novos_dados)
            except: # Se ocorrer um erro ao atualizar os dados da entidade, retorne um erro 400 (Solicitação inválida)
                return {"erro": "Dados inválidos"}, 400
            # Retorna uma mensagem de sucesso e o código de status 200 (OK)
            return {"mensagem": "Entidades atualizado com sucesso"}, 200


##### FUNÇÕES DO TIPO POST #####

#CHECK
@app.route('/usuarios', methods=['POST'])
# Função para adicionar um novo usuário
def adicionar_usuario():
    # Obter os dados do corpo da solicitação
    usuario = request.json
    nome = usuario.get("nome", "")
    email = usuario.get("email", "")
    password = usuario.get("password", "")
    curso = usuario.get("curso", "")
    data_nascimento = usuario.get("data_nascimento", "")
    cpf = usuario.get("cpf", "")
    entidades = usuario.get("entidades", [])
    id = usuario.get("id", "")
    interesses = usuario.get("interesses", [])
    periodo = usuario.get("periodo", "")
    projetos = usuario.get("projetos", [])
    # Verificar se os campos obrigatórios foram fornecidos
    if not nome or not email or not password or not curso or not data_nascimento or not cpf or not id or not periodo or not interesses:
        return {"error": "Nome, usuario, email, password, curso, data_nascimento, cpf, id e periodo são obrigatórios"}, 400
    # Verificar se o CPF já existe no banco de dados
    if mongo.db.usuarios.find_one(filter={"cpf": cpf}):
        return {"error": "Usuário já existe"}, 409
    # Gerar um hash SHA-256 da senha
    hashed_password = hash_password(password)
    # Criar um dicionário contendo os dados do usuário
    usuario = {
                "nome": nome, 
                "email": email, 
                "password": hashed_password, 
                "curso": curso, 
                "data_nascimento": data_nascimento, 
                "cpf": cpf, 
                "id": id, 
                "periodo": periodo, 
                "entidades": entidades, 
                "interesses": interesses, 
                "projetos": projetos
            }
    # Insere o usuário no banco de dados MongoDB
    mongo.db.usuarios.insert_one(usuario)
    # Retorna uma mensagem de sucesso e o código de status 201 (Criado)
    return jsonify({"msg": "Usuário criado com sucesso!"}), 201

#CHECK
@app.route('/entidades', methods=['POST'])
# Função para adicionar uma nova entidade
def adicionar_entidade():
    # Obter os dados do corpo da solicitação
    nome = request.json.get("nome", "")
    email = request.json.get("email", "")
    password = request.json.get("password", "")
    apresentacao = request.json.get("apresentacao", "")
    area_atuacao = request.json.get("area_atuacao", "")
    data_criacao = request.json.get("data_criacao", "")
    id = request.json.get("id", "")
    info_contato = request.json.get("info_contato", {})
    presidente = request.json.get("presidente", "")
    projetos = request.json.get("projetos", [])
    vice_presidente = request.json.get("vice_presidente", "")
    # Verificar se os campos obrigatórios foram fornecidos
    if not nome or not email or not password or not apresentacao or not area_atuacao or not data_criacao or not id or not presidente or not vice_presidente:
        return {"error": "Nome, email, password, apresentacao, area_atuacao, data_criacao, id, presidente e vice_presidente são obrigatórios"}, 400
    # Verificar se o nome já existe no banco de dados
    if mongo.db.entidades.find_one(filter={"nome": nome}):
        return {"error": "Esse nome já existe"}, 409
    # Criar um dicionário contendo os dados da entidade
    entidade = {
            "email": email,
            "password": password,
            "nome": nome,
            "apresentacao": apresentacao,
            "area_atuacao": area_atuacao,
            "data_criacao": data_criacao,
            "id": id,
            "info_contato": info_contato,
            "presidente": presidente,
            "projetos": projetos,
            "vice_presidente": vice_presidente
        }
    # Insere a entidade no banco de dados MongoDB
    mongo.db.entidades.insert_one(entidade)
    # Retorna uma mensagem de sucesso e o código de status 201 (Criado)
    return {"mensagem": "Entidade adicionada com sucesso"}, 201

#não funciona e não faz sentido
@app.route('/senha', methods=['GET'])
def solicitar_recuperacao():
    # Obter o e-mail do corpo da solicitação
    email_usuario = request.args.get('email', '')
  
    if not email_usuario:
       return {"erro": "Nenhum e-mail fornecido"}, 400
    
    if not mongo.db.usuarios.find_one({"email": email_usuario}):
        return {"error": "Usuário não existe"}, 404

    # Enviar e-mail através do endpoint enviar_email
    try:
        usuario = list(mongo.db.usuarios.find_one({"email": email_usuario}))
        return usuario, 200
    except Exception as e:
        return {"erro": "Erro ao enviar e-mail"}, 500

# Rota pública que não requer autenticação
@app.route('/')
def public_route():
    """Rota pública que não requer autenticação."""
    return {"msg": "Página pública"}

# Rota protegida que requer autenticação
@app.route('/secret')
@requires_auth
def secret_page():
    """Rota protegida que requer autenticação."""
    return {"msg": "Você está autenticado e pode acessar esta página protegida"}

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
