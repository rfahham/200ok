# !/usr/bin/env python
# -- coding: utf-8 --

import requests
import urllib3
from colorama import Fore, Style, init
import json  # Importa a biblioteca json

# Inicializa o Colorama
init(autoreset=True)

# Desabilita warnings do urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# URL para requisição POST
url = "https://api-desafio-qa.onrender.com/users"

# Dados que você deseja enviar
data = {
    "name": "ricardo",
    "lastname": "fahham",
    "email": "rfahham@gmail.com"
}

# Cabeçalhos que você deseja enviar
headers = {
    'Content-Type': 'application/json',  # Corrigido para usar o formato correto de cabeçalho
    'Accept': '*/*'  # Corrigido para usar o formato correto de cabeçalho
}

try:
    # Converte os dados para JSON antes de enviar
    r = requests.post(url, headers=headers, data=json.dumps(data))  # Faz a requisição POST

    # Exibindo informações da resposta
    print(Fore.GREEN + f"Status Code: {r.status_code} - {r.reason}" + Style.RESET_ALL)
    
    # Exibindo parte do conteúdo da resposta
    print("Conteúdo da Resposta (300 primeiros caracteres):")
    print(r.text[:300] + '...')
    
except requests.RequestException as e:
    print(Fore.RED + f"Erro ao acessar {url}: {e}" + Style.RESET_ALL)


# curl -X 'POST' 'https://api-desafio-qa.onrender.com/users' -H 'Content-Type: application/json' -H 'Accept: */*' -d '{"name": "Ricardo", "lastname": "fahham", "email": "rfahham@gmail.com"}'
