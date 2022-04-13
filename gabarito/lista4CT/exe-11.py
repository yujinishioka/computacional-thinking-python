seq_fib = []
cont = 0

print("--- SEQUENCIA FIBONACCI ---")
qntd = int(input("Digite a qntd de valores para a sequencia: "))

while cont < qntd:
    if cont < 2:
        seq_fib.append(1)
    else:
        seq_fib.append(seq_fib[cont-1]+seq_fib[cont-2])
    cont += 1


print(seq_fib)