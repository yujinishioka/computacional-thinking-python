import random

def cria_baralho():
    baralho = []
    for naipe in ('♥', '♦', '♣', '♠'):
        valor = 1
        while valor <= 13:
            if valor == 1:
                c = ('A', naipe)
            elif valor == 11:
                c = ('J', naipe)
            elif valor == 12:
                c = ('Q', naipe)
            elif valor == 13:
                c = ('K', naipe)
            else:
                c = (valor, naipe)
            
            baralho.append(c)
            valor += 1

    return baralho

def embaralha(baralho):
    for qtde in range(50):
        i = random.randint(0, len(baralho) - 1)
        j = random.randint(0, len(baralho) - 1)
        aux = baralho[i]
        baralho[i] = baralho[j]
        baralho[j] = aux

def distribui(baralho, qtde):
    mao = []
    while qtde > 0:
        c = compra(baralho)
        mao.append(c)
        qtde -= 1

    return mao

def compra(baralho):
    return baralho.pop()
