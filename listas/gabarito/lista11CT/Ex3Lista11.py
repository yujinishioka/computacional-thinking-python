def insertion_sort(lista):
    for i in range(1, len(lista)):
        aux = lista[i]
        while i > 0 and lista[i - 1].lower() < aux.lower():
            lista[i] = lista[i - 1]
            i = i - 1
        
        lista[i] = aux


lst = ['yona', 'tais', 'sergio', 'gui', 'ana', 'jose', 'nair', 'Ana', 'Tais', 'Joao']

insertion_sort(lst)
print(lst)
