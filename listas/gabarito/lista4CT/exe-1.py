soma = 0

print("0 para parar")
numero = int(input("Digite numero: "))

while numero != 0:
    if numero %2 == 0:
        soma += numero
    if numero == 0:
        break
    print("0 para parar")
    numero = int(input("Digite numero: "))

print("O total é", soma)