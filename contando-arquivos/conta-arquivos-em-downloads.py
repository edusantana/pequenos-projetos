#!/usr/bin/env python3

"""
Projeto conta os arquivos em download.

Baseado em https://www.mkyong.com/python/python-how-to-list-all-files-in-a-directory/
"""

import os
from datetime import date
from datetime import datetime

CAMINHO_DO_DIRETORIO = os.environ['HOME'] + '/Downloads'

def imprimeNome():
    # imprimir seu nome aqui.
    pass

def imprimeHorario():
    data_atual = date.today()
    print(data_atual)
    print(datetime.now())

def verificaOsArquivos(caminho):

    print("Pesquisando arquivos em: ", caminho)

    arquivos = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(caminho):
        for file in f:
            arquivos.append(f)
    return arquivos


imprimeNome()
imprimeHorario()
arquivos = verificaOsArquivos(CAMINHO_DO_DIRETORIO)
print("Total de arquivos: ", len(arquivos))

relatorio = open(os.environ['HOME'] + "/relatorio.txt", "a")

relatorio.writeln(datetime.now())
relatorio.write("Total de arquivos: ")
relatorio.write(str(len(arquivos)))
relatorio.close()
