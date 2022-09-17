def menor(lista, i):
    pos_menor = i
    i = i + 1
    while i < len(lista):
        if lista[pos_menor] > lista[i]:
            pos_menor = i
        i = i + 1
    return pos_menor

def selection_sort(conj):
    for i in range(len(conj)):
        j = menor(conj, i)
        aux = conj[j]
        conj[j] = conj[i]
        conj[i] = aux

vetor = [2, 5, -7, 9, 3, 10, 15, 6]
selection_sort(vetor)
print(vetor)