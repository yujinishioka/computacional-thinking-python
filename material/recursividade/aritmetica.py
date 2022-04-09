acumulador = 0
i = 1

print("------- SOMADOR -------")
numero = int(input("Digite um numero: "))

while numero <= 0:
    numero = int(input("Número inválido (menor ou igual a 0), digite outro numero: "))

while i <= numero:
    acumulador += i
    i = i + 1

print("A soma de 1 até", numero, "é igual a", acumulador)