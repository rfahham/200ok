# -- coding: utf-8 --

import requests
import urllib3
import certifi

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

# arquivo com a lista de urls
arq = open('lista-mencached.txt', 'r')
arq_201 = open('201.csv', 'w')
cont_201 = 0

def writeFile(arq, linha):
    arq.write(linha)

while True:
    linha = arq.readline()
    if linha == "":
        break
    url = linha.strip()
    print(url)
    r =requests.post(url)
    print(bcolors.OK + r.status_code + bcolors.RESET)
    if (r.status_code == 201):
        writeFile(arq_201, linha)
        cont_201 += 1

print(cont_201, 'tiveram Status Code 200 OK')




