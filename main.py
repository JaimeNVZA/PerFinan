# v0.1: En esta versión se diseña el programa de forma estructurada para tener una idea general

from graficos import *

print("\t\t****BILLETERA 0.1 CMD****")
archivo = open("texto.txt", "r")
linea = archivo.readline()
while linea != "":
    linea = archivo.readline()
    print(linea)
graficos()