tupla = ('a', 'b', 'abc', 'mel', 'onde', 'como', 'papel', 'pedra')

aux = int(input('Digite um numero: '))

def separa(tupla):
    cont = 0

    while cont < len(tupla):
        if(len(tupla[cont]) == aux):
            print(tupla[cont])
        
        cont += 1

separa(tupla)
print('São as palavras com', aux, 'letras')