# -- coding: utf-8 --

import requests


class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

# arquivo com a lista de urls
arq = open('lista.txt', 'r')
arq_200 = open('200.csv', 'w')
arq_404 = open('404.csv', 'w')
cont_200 = 0
cont_404 = 0

def writeFile(arq, linha):
    arq.write(linha)

while True:
    linha = arq.readline()
    if linha == "":
        break
    url = linha.strip()
    print(url)
    r =requests.get(url)
    
    if (r.status_code == 200):
        print(bcolors.OK + "STATUS CODE 200" + bcolors.RESET)
        writeFile(arq_200, linha)
        cont_200 += 1
    elif (r.status_code == 404):
        print(bcolors.FAIL + "STATUS CODE 404" + bcolors.RESET)
        writeFile(arq_404, linha)
        cont_404 += 1


print(cont_200, 'tiveram Status Code 200 OK')
print(cont_404, 'tiveram Status Code 404 Page Not Found')

arq.close()
arq_200.close()
arq_404.close()