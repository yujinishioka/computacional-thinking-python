import random as r
import fila as f

lista = []

for i in range(10):
    f.put(lista, r.randint(0, 1000))

print(lista)

while not f.isEmpty(lista):
    f.get(lista)
    print(lista)