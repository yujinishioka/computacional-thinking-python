
def armazena_texto():
    i = 0
    lista = []

    while(i < 10):
        aux = str(input("Digite um texto para armazenar: "))
        lista.append(aux)
        i += 1

    return lista

print(armazena_texto())