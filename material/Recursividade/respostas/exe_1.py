def maximo(lista, pos):
    if pos == len(lista) - 1:
        return lista[pos]
    else:
        valor = maximo(lista, pos + 1)
        if valor > lista[pos]:
            return valor
        else:
            return lista[pos]

lst = [3, 10, -4, 16, 19, 7, 2, -5, 10, 2]
m = maximo(lst, 0)
print(m)

