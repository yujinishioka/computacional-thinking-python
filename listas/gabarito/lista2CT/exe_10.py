# Exercicio 10 - Lista 2

aux = input("Digite a distancia percorrida: ")
distancia = float(aux)

aux = input("Digite o tempo levado para percorrer a distancia: ")
tempo = float(aux)

velocidadeMs = distancia/tempo
velocidadeKh = velocidadeMs * 3.6

print(velocidadeMs, "m/s")
print(velocidadeKh, "Km/h")