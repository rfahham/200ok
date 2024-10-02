#!/usr/bin/env python
# -- coding: utf-8 --

import requests
import urllib3
import time
import datetime

# Solicita ao usuário o tempo de execução em segundos
tempo = float(input("Insira o tempo de execução em segundos: "))

# Desabilita avisos do urllib3
urllib3.disable_warnings()

def writeFile(arq, linha):
    """Escreve uma linha no arquivo."""
    try:
        arq.write(linha + '\n')
    except Exception as e:
        print(f"Erro ao escrever no arquivo: {e}")

def lendoLista(arq):
    """Lê URLs de um arquivo e retorna uma lista."""
    return [linha.strip() for linha in arq if linha.strip()]

def executaRequests(listaUrl, arq_200, arq_401, arq_404, arq_500, arq_503):
    """Executa requisições HTTP e conta os status codes."""
    cont_200 = cont_401 = cont_404 = cont_500 = cont_503 = 0
    total_requisicoes = 0

    for url in listaUrl:
        try:
            r = requests.get(url, verify=False)
            total_requisicoes += 1  # Contar cada requisição
            if r.status_code == 200:
                writeFile(arq_200, url)
                cont_200 += 1
            elif r.status_code == 401:
                writeFile(arq_401, url)
                cont_401 += 1
            elif r.status_code == 404:
                writeFile(arq_404, url)
                cont_404 += 1
            elif r.status_code == 500:
                writeFile(arq_500, url)
                cont_500 += 1
            elif r.status_code == 503:
                writeFile(arq_503, url)
                cont_503 += 1
            else: 
                print(f'Status Code desconhecido para {url}: {r.status_code}')
        except requests.RequestException as e:
            print(f'Erro ao fazer requisição para {url}: {e}')

    return cont_200, cont_401, cont_404, cont_500, cont_503, total_requisicoes

def calcular_media_tempo(total_requisicoes, tempo_total):
    """Calcula a média de tempo por requisição."""
    if total_requisicoes > 0:
        media = tempo_total / total_requisicoes
        return media
    else:
        return 0  # Para evitar divisão por zero

def printQtdStatusCode(cont_200, cont_401, cont_404, cont_500, cont_503):
    """Imprime um resumo dos códigos de status."""
    total_urls = cont_200 + cont_401 + cont_404 + cont_500 + cont_503
    print("-"*50)
    print(" "*20, "Summary", " "*20)
    print("-"*50)
    print(f"Total de URLs verificadas: {total_urls}")
    print(f"Páginas com Status Code 200: {cont_200}")
    print(f"Páginas com Status Code 401: {cont_401}")
    print(f"Páginas com Status Code 404: {cont_404}")
    print(f"Páginas com Status Code 500: {cont_500}")
    print(f"Páginas com Status Code 503: {cont_503}")
    print("-"*50)

# Abrindo os arquivos de forma segura usando 'with'
with open('lista.txt', 'r') as arq:
    listaUrl = lendoLista(arq)

with open('200.csv', 'w') as arq_200, \
     open('401.csv', 'w') as arq_401, \
     open('404.csv', 'w') as arq_404, \
     open('500.csv', 'w') as arq_500, \
     open('503.csv', 'w') as arq_503:

    inicio = time.time()
    total = 0  # Inicialize total
    total_requisicoes = 0

    while total < tempo:
        cont_200, cont_401, cont_404, cont_500, cont_503, requisicoes = executaRequests(listaUrl, arq_200, arq_401, arq_404, arq_500, arq_503)    
        total_requisicoes += requisicoes  # Acumula o total de requisições
        fim = time.time()
        total = fim - inicio

    # Chama a função para imprimir os status codes
    printQtdStatusCode(cont_200, cont_401, cont_404, cont_500, cont_503)

    # Calcular e imprimir a média de tempo
    media_tempo = calcular_media_tempo(total_requisicoes, total)
    print(f"Média de tempo por requisição: {media_tempo:.2f} segundos")

    # Timestamp de início e fim
    print("Início do teste: " + datetime.datetime.fromtimestamp(inicio).strftime('%d-%m-%Y - %H:%M:%S'))
    print("Fim do teste:    " + datetime.datetime.fromtimestamp(fim).strftime('%d-%m-%Y - %H:%M:%S'))

    # Cálculo e formatação do tempo total
    total_minutos, total_segundos = divmod(int(total), 60)
    print(f"Tempo de duração do teste: {total_minutos} minuto(s) e {total_segundos} segundo(s)")
