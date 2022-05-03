import random

sorteado = random.randint(1,1001)

chute = int(input("Digite um valor: "))
tentativas = 1

while chute != sorteado:
    if chute > sorteado:
        print("Tente um numero MENOR")
    if chute < sorteado:
        print("Tente um numero MAIOR")
    chute = int(input("Chute: "))
    tentativas += 1

print("Parabens, voce acertou em", tentativas, "tentativas! Numero sorteado foi o", sorteado)