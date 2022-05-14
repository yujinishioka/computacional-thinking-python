def verifica_primo(numero):
    primo = True
    i = 2

    while i < numero:
        aux = numero % i
        i += 1

        if aux == 0:
            primo = False
            break

    if numero == 1 or numero == 0:
        primo = False

    return primo

def cem_primos():
    array = []
    teste = 2
    while len(array) < 100:
        if(verifica_primo(teste)):
            array.append(teste)
        
        teste += 1
        
    return array

print(cem_primos())
