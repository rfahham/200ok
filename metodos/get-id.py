# !/usr/bin/env python
# -- coding: utf-8 --

import requests
import urllib3
from colorama import Fore, Style, init

# Inicializa o Colorama
init(autoreset=True)

# Desabilita warnings do urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# URL para requisição
url = "https://api-desafio-qa.onrender.com/users/6"

# Cabeçalhos que você deseja enviar
headers = {
    'Content-Type': 'application/json',  # Corrigido para usar o formato correto de cabeçalho
    'Accept': '*/*'  # Corrigido para usar o formato correto de cabeçalho
}

try:
    r = requests.get(url, headers=headers, verify=False)  # Ignorando SSL

    # Exibindo informações da resposta
    print(Fore.GREEN + f"Status Code: {r.status_code} - {r.reason}" + Style.RESET_ALL)
    
    # Exibindo parte do conteúdo da resposta
    print("------------------------------------------------")
    print("Conteúdo da Resposta (300 primeiros caracteres):")
    print("------------------------------------------------")
    print(r.text[:500] + '...')
    
    # Exibindo os cabeçalhos da resposta
    print("-----------------------")
    print("Cabeçalhos da Resposta:")
    print("-----------------------")
    for key, value in r.headers.items():
        print(f"{key}: {value}")

except requests.RequestException as e:
    print(Fore.RED + f"Erro ao acessar {url}: {e}" + Style.RESET_ALL)

# curl -X 'GET' 'https://api-desafio-qa.onrender.com/users/6' -H 'accept: */*'