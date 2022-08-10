import random

def numeros_aleatorios(n):
    cont = 0
    conj = []

    while cont < n:
        numero = random.randint(1, 1000)
        conj.append(numero)
        cont += 1

    print(conj)

numeros_aleatorios(20)