# !/usr/bin/env python
# -- coding: utf-8 --

import requests
import urllib3
import certifi
import time
import datetime

tempo = input("Insira o tempo de execução em segundos: ")

arq = open('lista.txt', 'r') # arquivo com a lista de urls

def abrirPlanilhas():
    arq_200 = open('200.csv', 'w')
    arq_401 = open('401.csv', 'w')
    arq_404 = open('404.csv', 'w')
    arq_500 = open('500.csv', 'w')
    arq_503 = open('503.csv', 'w')
    return arq_200, arq_401, arq_404, arq_500, arq_503

urllib3.disable_warnings()

def writeFile(arq, linha):
    arq.write(linha)

def lendoLista(arq):
    linha = "a"
    listaArquivo = []
    while linha != "":
        linha = arq.readline()
        url = linha.strip()
        # print url
        listaArquivo.append(url)
    return listaArquivo

def executaRequests(listaUrl, arq_200, arq_401, arq_404, arq_500, arq_503):
    cont_200 = 0
    cont_401 = 0
    cont_404 = 0
    cont_500 = 0
    cont_503 = 0
    for i in range(0, len(listaUrl)-1):
        r = requests.get(listaUrl[i], verify=False)
        
        if (r.status_code == 200):
            writeFile(arq_200, listaUrl[i])
            cont_200 += 1
        elif (r.status_code == 404):
            writeFile(arq_404, listaUrl[i])
            cont_401 += 1
        elif (r.status_code == 401):
            writeFile(arq_401, listaUrl[i])
            cont_404 += 1
        elif (r.status_code == 500):
            writeFile(arq_500, listaUrl[i])
            cont_500 += 1
        elif (r.status_code == 503):
            writeFile(arq_503, listaUrl[i])
            cont_503 += 1
        else: 
            print('Status Code desconhecido ')
    return(cont_200, cont_401, cont_404, cont_500, cont_503)
    
    # print("Status code " + str(r.status_code))


def conta_request():


def printQtdStatusCode(cont_200, cont_401, cont_404, cont_500, cont_503):
    print 'Sumary'
    print '---------------------------'
    print 'Total de urls verificadas:', (cont_200 + cont_401 + cont_404 + cont_500  + cont_503)
    print 'Total de requests:', ()
    print 'Páginas Status Code 200:', (cont_200)
    print 'Páginas Status Code 401:', (cont_401)
    print 'Páginas Status Code 404:', (cont_404)
    print 'Páginas Status Code 500:', (cont_500)
    print 'Páginas Status Code 503:', (cont_503)
    # print 'Protocolo:'()
    print '---------------------------'

listaUrl = []
listaUrl = lendoLista(arq)

arq_200, arq_401, arq_404, arq_500, arq_503 = abrirPlanilhas()


inicio = time.time()
fim = time.time()
total = fim - inicio
while (total) < tempo :
    cont_200, cont_401, cont_404, cont_500, cont_503 = executaRequests(listaUrl, arq_200, arq_401, arq_404, arq_500, arq_503)    
    fim = time.time()
    total = fim - inicio
printQtdStatusCode(cont_200, cont_401, cont_404, cont_500, cont_503)

timestamp_inicio = datetime.datetime.fromtimestamp(inicio)
print("Inicio do teste: " + timestamp_inicio.strftime('%d-%m-%Y - %H:%M:%S'))

timestamp_fim = datetime.datetime.fromtimestamp(fim)
print("Fim do teste:    " + timestamp_fim.strftime('%d-%m-%Y - %H:%M:%S'))

timestamp_total = datetime.datetime.fromtimestamp(total)
print("Tempo de duração do teste:      " + timestamp_total.strftime(':%M:%S'))

arq.close()
arq_200.close()
arq_401.close()
arq_404.close()
arq_500.close()
arq_503.close()
