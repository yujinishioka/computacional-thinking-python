import random

matriz = []

for i in range(4):
    matriz.append([0] * 5)

for i in range(4):
    for j in range(5):
        matriz[i][j] = random.randint(0, 9)

for linha in matriz:
    print(linha)