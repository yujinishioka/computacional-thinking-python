# Exercicio 12 - Lista 2

rm = int(input("RM: "))

soma = rm%10
soma += (rm//10)%10
soma += (rm//100)%10
soma += (rm//1000)%10
soma += (rm//10000)

print(soma)