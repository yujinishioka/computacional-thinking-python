import exe_1

def inverte_lista(lista):
    print("lista inversa:")
    i = len(lista) - 1

    while i >= 0:
        print(lista[i])
        i -= 1

lista = armazena_texto()
inverte_lista(lista)