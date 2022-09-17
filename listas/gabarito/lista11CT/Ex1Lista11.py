def esta_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i+1]:
            return False
    return True

    