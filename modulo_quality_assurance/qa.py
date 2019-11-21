# !/usr/bin/env python
# -- coding: utf-8 --

import funcoes form funcoes
import time
import datetime

tempo = input("Insira o tempo de execução em segundos: ")

arq = open('lista.txt', 'r')  # arquivo com a lista de urls


listaUrl = []
listaUrl = lendoLista(arq)

arq_200, arq_401, arq_404, arq_500, arq_503 = abrirPlanilhas()

inicio = time.time()
fim = time.time()
total = fim - inicio
cont_request = 0
while (total) < tempo:
    cont_200, cont_401, cont_404, cont_500, cont_503 = executaRequests(listaUrl, arq_200, arq_401, arq_404, arq_500,
                                                                       arq_503)
    cont_request += 1
    fim = time.time()
    total = fim - inicio
tr = cont_request / tempo
printQtdStatusCode(tr, cont_request, cont_200, cont_401, cont_404, cont_500, cont_503)

timestamp_inicio = datetime.datetime.fromtimestamp(inicio)
print("Inicio do teste: " + timestamp_inicio.strftime('%d-%m-%Y - %H:%M:%S'))

timestamp_fim = datetime.datetime.fromtimestamp(fim)
print("Fim do teste:    " + timestamp_fim.strftime('%d-%m-%Y - %H:%M:%S'))

timestamp_total = datetime.datetime.fromtimestamp(total)
print("Tempo de duração do teste:      " + timestamp_total.strftime(':%M:%S'))
print
print

arq.close()
arq_200.close()
arq_401.close()
arq_404.close()
arq_500.close()
arq_503.close()
