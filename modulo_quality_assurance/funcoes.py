import requests
import urllib3


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

    for i in range(0, len(listaUrl) - 1):
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
    return (cont_200, cont_401, cont_404, cont_500, cont_503)


def printQtdStatusCode(tr, cont_request, cont_200, cont_401, cont_404, cont_500, cont_503):
    print
    print
    'Sumary'
    print
    '---------------------------'
    print
    print
    'Total de urls verificadas:', (cont_200 + cont_401 + cont_404 + cont_500 + cont_503)
    print
    print
    'Páginas Status Code 200:', (cont_200)
    print
    'Páginas Status Code 401:', (cont_401)
    print
    'Páginas Status Code 404:', (cont_404)
    print
    'Páginas Status Code 500:', (cont_500)
    print
    'Páginas Status Code 503:', (cont_503)
    print
    print
    '---------------------------'
    print
    print
    'Total de Requests:', (cont_request)
    print
    print
    'Tempo Médio de Resposta(sec):', (tr), 'requests por segundo'
    print
    print