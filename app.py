from flask import Flask, request
from flask_pymongo import PyMongo
from datetime import date
from flask_mail import Mail, Message
import os

# Aplicação Flask e Mongo
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://gabrielprady1:lR6RItI2wEsXkTeY@cluster0.do8a1uo.mongodb.net/biblioteca_db"
mongo = PyMongo(app)

# Author: João Pedro Queiroz Viana
# Co-author: Pedro Oliviere
# Configurando Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.getenv("email_projeto_hub")
app.config['MAIL_PASSWORD'] = os.getenv("senha_projeto_hub")

# Inicialize o Mail
mail = Mail(app)

# Funçaõ de enviar email
def enviar_email(email, assunto, mensagem):
    destinatario = email
    assunto = assunto
    mensagem = mensagem

    msg = Message(
        subject=assunto,
        sender=app.config['MAIL_USERNAME'],
        recipients=[destinatario],
        body=mensagem,
    )

    mail.send(msg)


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

# Função que busca usuarios através do campo "nome"
@app.route('/usuarios/<string:nome>', methods=['GET'])
def get_user_by_name(nome):
    # Define um filtro para encontrar o usuário com o nome especificado
    filtro = {
        "nome": nome
    }
    # Define uma projeção para não incluir o campo "_id" nos resultados
    projecao = {"_id": 0}
    # Recupera os dados do usuário do banco de dados MongoDB usando o filtro e a projeção definidos
    dados_usuarios = mongo.db.usuarios_proj_agil.find(filtro, projecao)
    # Cria uma resposta JSON contendo o usuário encontrado
    resp = {
        "usuario": list(dados_usuarios),
    }
    # Retorna a resposta JSON e o código de status 200 (OK)
    return resp, 200
# Função que busca entidades através do campo "nome"
@app.route('/entidades/<string:nome>', methods=['GET'])
def get_entidade_by_name(nome):
    # Define um filtro para encontrar a entidade com o nome especificado
    filtro = {
        "nome": nome
    }
    # Define uma projeção para não incluir o campo "_id" nos resultados
    projecao = {"_id": 0}
    # Recupera os dados da entidade do banco de dados MongoDB usando o filtro e a projeção definidos
    dados_entidades = mongo.db.entidades_proj_agil.find(filtro, projecao)
    # Cria uma resposta JSON contendo a entidade encontrada
    resp = {
        "entidade": list(dados_entidades),
    }
    # Retorna a resposta JSON e o código de status 200 (OK)
    return resp, 200

# Função que busca empresas através do campo "nome"
@app.route('/empresas/<string:nome>', methods=['GET'])
def get_empresa_by_name(nome):
    # Define um filtro para encontrar a empresa com o nome especificado
    filtro = {
        "nome": nome
    }
    # Define uma projeção para não incluir o campo "_id" nos resultados
    projecao = {"_id": 0}
    # Recupera os dados da empresa do banco de dados MongoDB usando o filtro e a projeção definidos
    dados_empresas = mongo.db.recrutadores_proj_agil.find(filtro, projecao)
    # Cria uma resposta JSON contendo a empresa encontrada
    resp = {
        "empresa": list(dados_empresas),
    }
    # Retorna a resposta JSON e o código de status 200 (OK)
    return resp, 200

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
print('hahahahahahahahaha')

@app.route('/empresas/<string:email>', methods=['DELETE'])
def remover_empresa(email):
    # Define um filtro para encontrar a empresa com CNPJ "12345678901234"
    filtro = {
        "email": email
    }
    # Remove a empresa do banco de dados MongoDB
    mongo.db.empresas_proj_agil.delete_one(filtro)
    # Retorna uma mensagem de sucesso e o código de status 200 (OK)
    return {"mensagem": "Empresa removida com sucesso"}, 200

@app.route('/usuarios/<string:email>', methods=['PUT'])
def editar_usuario(email):
    filtro = {"email": email}

    try:
        projecao = {"_id": 0}
        dados_usuarios = list(mongo.db.usuarios_proj_agil.find(filtro, projecao))
    except:
        return {"erro": "Erro no sistma"}, 500
    else:
        if dados_usuarios["usuarios_proj_agil"] == []:
            return {"erro": "Usuário não encontrado"}, 404
        else:
            data = request.json
            novos_dados = {
                "$set": data
            }

            try:
                mongo.db.usuarios_proj_agil.update_one(filtro, novos_dados)
            except:
                return {"erro": "Dados inválidos"}, 400
            
            return {"mensagem": "Usuário atualizado com sucesso"}, 200

@app.route('/entidades/<string:email>', methods=['PUT'])
def editar_entidade(email):
    filtro = {"email": email}

    try:
        projecao = {"_id": 0}
        dados_entidades = list(mongo.db.entidades_proj_agil.find(filtro, projecao))
    except:
        return {"erro": "Erro no sistma"}, 500
    else:
        if dados_entidades["entidades_proj_agil"] == []:
            return {"erro": "Entidades não encontrado"}, 404
        else:
            data = request.json
            novos_dados = {
                "$set": data
            }

            try:
                mongo.db.entidades_proj_agil.update_one(filtro, novos_dados)
            except:
                return {"erro": "Dados inválidos"}, 400
            
            return {"mensagem": "Entidades atualizado com sucesso"}, 200

@app.route('/empresas/<string:email>', methods=['PUT'])
def editar_empresa(email):
    filtro = {"email": email}

    try:
        projecao = {"_id": 0}
        dados_empresas = list(mongo.db.empresas_proj_agil.find(filtro, projecao))
    except:
        return {"erro": "Erro no sistma"}, 500
    else:
        if dados_empresas["empresas_proj_agil"] == []:
            return {"erro": "Empresas não encontrado"}, 404
        else:
            data = request.json
            novos_dados = {
                "$set": data
            }

            try:
                mongo.db.empresas_proj_agil.update_one(filtro, novos_dados)
            except:
                return {"erro": "Dados inválidos"}, 404
            
            return {"mensagem": "Empresas atualizado com sucesso"}, 200

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
    entidade = {
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
    mongo.db.entidades_proj_agil.insert_one(entidade)
    # Retorna uma mensagem de sucesso e o código de status 201 (Criado)
    return {"mensagem": "Entidade adicionada com sucesso"}, 201

@app.route('/empresas', methods=['POST'])
def adicionar_empresas():
    empresa = request.json
    nome = empresa.get("nome", "")
    apresentacao = empresa.get("apresentacao", "")
    cargo = empresa.get("cargo", "")
    cnpj = empresa.get("cnpj", "")
    email = empresa.get("email", "")
    celular = empresa.get("celular", "")
    linkedin = empresa.get("linkedin ", "")
    site = empresa.get("site", "")
    data_criacao = date.today()

    if not nome or not apresentacao or not cargo or not cnpj or not email or not celular or not linkedin or not site:
        return {"error": "Nome, apresentacao, cargo, cnpj, email, celular, linkedin e site são obrigatórios"}, 400
    
    if mongo.db.usuarios_aps_5.find_one(filter={"cnpj": cnpj}):
        return {"error": "Id já existe"}, 409  
    
    empresa = {
            "nome": nome,
            "apresentacao": apresentacao,
            "cargo": cargo,
            "cnpj": cnpj,
            "email": email,
            "data_criacao": data_criacao,
            "info_contato": {
                "celular": celular,
                "linkedin": linkedin,
                "site": site
            },
        }
    try:
        # Insere o usuário no banco de dados MongoDB
        mongo.db.recrutadores_proj_agil.insert_one(empresa)
    except:
        return {"error": "Dados inválidos"}, 400
    
    # Retorna uma mensagem de sucesso e o código de status 201 (Criado)
    return {"mensagem": "Empresa adicionada com sucesso"}, 201

@app.route('/usuarios', methods=['POST'])
def solicitar_recuperacao():
   # Obter o e-mail do corpo da solicitação
   dados = request.json
   email_usuario = dados.get('email')
  
   if not email_usuario:
       return {"erro": "Nenhum e-mail fornecido"}, 400


   # Procurar usuário no banco de dados pelo e-mail
   usuario = mongo.db.usuarios.find_one({"email": email_usuario})


   if usuario:
       # Definir o assunto e a mensagem do e-mail
       assunto = "Recuperação de Senha"
       mensagem = f"Sua senha é: {usuario['senha']}"


       # Enviar e-mail através do endpoint enviar_email
       try:
           enviar_email(email_usuario, assunto, mensagem)
           return {"mensagem": "E-mail de recuperação enviado com sucesso!"}, 200
       except Exception as e:
           return {"erro": "Erro ao enviar e-mail"}, 500
   else:
       # E-mail não encontrado no banco de dados
       return {"erro": "E-mail não encontrado"}, 404

if __name__:
    app.run(debug=True)
