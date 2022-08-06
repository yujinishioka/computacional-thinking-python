def monta_tupla():
    print("Montando tupla...")
    tupla = (1, 2, 3, 4, 5, 6, 7)
    return tupla

def media_aritmetica(tupla):
    print("Calculando media aritmetica...")
    soma = i = 0

    while i < len(tupla):
        soma += tupla[i]
        i += 1
    
    media_a = soma / len(tupla)
    return media_a

print("A media aritmetica foi de", media_aritmetica(monta_tupla()))
