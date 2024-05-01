# auth.py
from flask import request, Response, jsonify

import hashlib


def hash_password(password):
    """Gera um hash SHA-256 da senha."""
    return hashlib.sha256(password.encode()).hexdigest()



def not_authenticated():
    """Envia uma resposta que solicita autenticação ao usuário."""
    return Response(
        'Acesso negado. Por favor, autentique-se.', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})


