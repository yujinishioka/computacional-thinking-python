def particao(lst):
    pos = len(lst) - 1
    pivo = lst[pos]
    j = 0
    for i in range(len(lst)):
        if lst[i] < pivo:
            aux = lst[j]
            lst[j] = lst[i]
            lst[i] = aux
            j = j + 1
    aux = lst[j]
    lst[j] = lst[pos]
    lst[pos] = aux
    return j

v = [10, 9, 1, 20, 34, 89, 7, 15, 35, 25]
pos_pivo = particao(v)
#v = [10, 9, 1, 20, 7, 15, 25, 34, 89, 35]
print(v)
print("Posicao pivo ", pos_pivo)

