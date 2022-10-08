def imprime(vetor, pos):
    if pos == len(vetor) - 1:
        print(vetor[pos])
    else:
        imprime(vetor, pos + 1)
        print(vetor[pos])

lst = [3, 10, -4, 16, 19, 7, 2, -5, 10, 2]
imprime(lst, 0)

