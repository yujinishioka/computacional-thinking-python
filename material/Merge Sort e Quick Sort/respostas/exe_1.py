def intercala(vetor, p, q, r):
    aux = []
    i = p
    j = q + 1

    while i <= q and j <= r:
        if vetor[i] < vetor[j]:
            aux.append(vetor[i])
            i += 1
        
        else:
            aux.append(vetor[j])
            j += 1
        
    while j <= r:
        aux.append(vetor[j])
        j += 1
    
    while i <= q:
        aux.append(vetor[i])
        i += i

    for valor in aux:
        vetor[p] = valor
        p += 1

lista = [-5, 7, 9, 13, 14, 2, 3, 18, 20, 41]

intercala(lista, 0, 4, 9)
print(lista)