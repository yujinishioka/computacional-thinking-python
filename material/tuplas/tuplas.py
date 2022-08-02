tupla = ("azul", "vermelho", "amarelo")

print("tupla:", tupla)
print("tamanho:", len(tupla))

print()
print("for in:")
for cor in tupla:
    print(cor)

print()
print("imprime de tras para frente:")
i = len(tupla) - 1
while i >= 0:
    print(tupla[i])
    i = i - 1

