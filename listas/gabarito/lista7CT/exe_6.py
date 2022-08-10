tupla = (1, 2, 3, 4, 5, 6, 7)

def media_aritmetica(tupla):
    soma = i = 0

    while i < len(tupla):
        soma += tupla[i]
        i += 1
    
    media_a = soma / len(tupla)
    return media_a

def desvio_padrao(tupla):
    soma = 0
    media = media_aritmetica(tupla)
    for v in tupla:
        soma = soma + (v - media) ** 2

    dp = (soma / (len(tupla) - 1)) ** 0.5
    return dp

print("Media:", media_aritmetica(tupla))
print("Desvio Padrao:", desvio_padrao(tupla))
