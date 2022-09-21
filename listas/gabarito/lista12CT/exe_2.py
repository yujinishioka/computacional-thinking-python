import random as r
import fila as f

lista = []

for i in range(100):
    f.put(lista, r.randint(0, 1000))

i = 0
pares = []
impares = []

while i < len(lista):
    if (lista[i]%2 == 0):
        pares.append(lista[i])
    else:
        impares.append(lista[i])
    
    i = i + 1

print('pares: ', pares, '\nimpares: ', impares)