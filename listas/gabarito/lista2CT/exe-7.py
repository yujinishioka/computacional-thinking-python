# Exercicio 7 - Lista 2

numero = input("digite um numero de 0 a 99: ")

def mostrarSeparando(i):
    primeiro = i//10
    segundo = i%10
    ptxt = str(primeiro)
    stxt = str(segundo)
    return("Dezena: " + ptxt, "Unidade", stxt)   

print(mostrarSeparando(numero))