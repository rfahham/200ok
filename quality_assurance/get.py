# -- coding: utf-8 --

import requests
from colorama import Fore, Style, init

# Inicializa o Colorama
init(autoreset=True)

# Função para escrever no arquivo
def writeFile(arq, linha):
    arq.write(linha)


# Abrindo arquivos com o contexto 'with' para garantir que sejam fechados corretamente
with open('lista.txt', 'r') as arq, \
        open('200.csv', 'w') as arq_200, \
        open('404.csv', 'w') as arq_404:

    cont_200 = 0
    cont_404 = 0

    for linha in arq:
        url = linha.strip()
        if not url:  # Ignora linhas vazias
            continue

        print(url)
        try:
            r = requests.get(url)
            if r.status_code == 200:
                print(Fore.GREEN + "STATUS CODE 200" + Style.RESET_ALL)
                writeFile(arq_200, linha)
                cont_200 += 1
            elif r.status_code == 404:
                print(Fore.RED + "STATUS CODE 404" + Style.RESET_ALL)
                writeFile(arq_404, linha)
                cont_404 += 1
            else:
                print(Fore.YELLOW + f"STATUS CODE {r.status_code}" + Style.RESET_ALL)

        except requests.RequestException as e:
            print(Fore.RED + f"Erro ao acessar {url}: {e}" + Style.RESET_ALL)

    print(f"{cont_200} URLs tiveram Status Code 200 OK")
    print(f"{cont_404} URLs tiveram Status Code 404 Page Not Found")
