# @app.route('/empresas', methods=['POST'])
# def adicionar_empresas():
#     empresa = request.json
#     nome = empresa.get("nome", "")
#     email = empresa.get("email", "")
#     password = empresa.get("password", "")
#     apresentacao = empresa.get("apresentacao", "")
#     cargo = empresa.get("cargo", "")
#     cnpj = empresa.get("cnpj", "")
#     email = empresa.get("email", "")
#     celular = empresa.get("celular", "")
#     linkedin = empresa.get("linkedin ", "")
#     site = empresa.get("site", "")
#     data_criacao = date.today()

#     if not nome or not apresentacao or not cargo or not cnpj or not email or not celular or not linkedin or not site:
#         return {"error": "Nome, apresentacao, cargo, cnpj, email, celular, linkedin e site são obrigatórios"}, 400
    
#     if mongo.db.usuarios_aps_5.find_one(filter={"cnpj": cnpj}):
#         return {"error": "Id já existe"}, 409  
    
#     empresa = {
#             "email": email,
#             "password": password,
#             "nome": nome,
#             "apresentacao": apresentacao,
#             "cargo": cargo,
#             "cnpj": cnpj,
#             "email": email,
#             "data_criacao": data_criacao,
#             "info_contato": {
#                 "celular": celular,
#                 "linkedin": linkedin,
#                 "site": site
#             },
#         }
#     try:
#         # Insere o usuário no banco de dados MongoDB
#         mongo.db.recrutadores_proj_agil.insert_one(empresa)
#     except:
#         return {"error": "Dados inválidos"}, 400
    
#     # Retorna uma mensagem de sucesso e o código de status 201 (Criado)
#     return {"mensagem": "Empresa adicionada com sucesso"}, 201

# @app.route('/empresas/<string:email>', methods=['PUT'])
# def editar_empresa(email):
#     current_user = get_current_user()
#     if current_user['email'] != email:
#         return {"erro": "Acesso não autorizado"}, 403
    
#     filtro = {"email": email}

#     try:
#         projecao = {"_id": 0}
#         dados_empresas = list(mongo.db.empresas_proj_agil.find(filtro, projecao))
#     except:
#         return {"erro": "Erro no sistma"}, 500
#     else:
#         if dados_empresas["empresas_proj_agil"] == []:
#             return {"erro": "Empresas não encontrado"}, 404
#         else:
#             data = request.json
#             novos_dados = {
#                 "$set": data
#             }

#             try:
#                 mongo.db.empresas_proj_agil.update_one(filtro, novos_dados)
#             except:
#                 return {"erro": "Dados inválidos"}, 404
            
#             return {"mensagem": "Empresas atualizado com sucesso"}, 200

# @app.route('/empresas/<string:email>', methods=['DELETE'])
# def remover_empresa(email):
#     # Define um filtro para encontrar a empresa com CNPJ "12345678901234"
#     filtro = {
#         "email": email
#     }
#     # Remove a empresa do banco de dados MongoDB
#     mongo.db.empresas_proj_agil.delete_one(filtro)
#     # Retorna uma mensagem de sucesso e o código de status 200 (OK)
#     return {"mensagem": "Empresa removida com sucesso"}, 200

# Função que busca empresas através do campo "nome"
# @app.route('/empresas/<string:nome>', methods=['GET'])
# def get_empresa_by_name(nome):
#     # Define um filtro para encontrar a empresa com o nome especificado
#     filtro = {
#         "nome": nome
#     }
#     # Define uma projeção para não incluir o campo "_id" nos resultados
#     projecao = {"_id": 0}
#     # Recupera os dados da empresa do banco de dados MongoDB usando o filtro e a projeção definidos
#     dados_empresas = mongo.db.recrutadores_proj_agil.find(filtro, projecao)
#     # Cria uma resposta JSON contendo a empresa encontrada
#     resp = {
#         "empresa": list(dados_empresas),
#     }
#     # Retorna a resposta JSON e o código de status 200 (OK)
#     return resp, 200

# @app.route('/empresas', methods=['GET'])
# def get_all_recrutadores():
#     filtro = {
#     }
#     # Define uma projeção para não incluir o campo "_id" nos resultados
#     projecao = {"_id": 0}
#     # Recupera os dados dos usuários do banco de dados MongoDB usando o filtro e a projeção definidos
#     dados_empresas = mongo.db.recrutadores_proj_agil.find(filtro, projecao)
#     # Cria uma resposta JSON contendo os usuários encontrados
#     resp = {
#         "usuarios": list(dados_empresas),
#     }
#     # Retorna a resposta JSON e o código de status 200 (OK)
#     return resp, 200
