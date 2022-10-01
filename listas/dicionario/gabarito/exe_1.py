frase = input("informe uma frase: ")

dic = {}

for letra in frase.lower():
    if letra in dic:
        dic[letra] = dic[letra] + 1
    else:
        dic[letra] = 1

lista = []
for letra in dic:
    lista.append(letra)

lista.sort()
for a in lista:
    print(a, "=", dic[a])