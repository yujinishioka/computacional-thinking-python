import baralho.baralho as baralho

def soma_pontos(mao):
    soma = 0
    for carta in mao:
        if carta[0] == 10 or carta[0] == 'J' or carta[0] == 'Q' or carta[0] == 'K':
            soma = soma + 10
        elif carta[0] == 'A':
            soma += 1
        else:
            soma = soma + carta[0]
    return soma  

deck = baralho.cria_baralho()
baralho.embaralha(deck)
mao_jogador = baralho.distribui(deck, 2)
mao_cpu = baralho.distribui(deck, 2)

print(mao_jogador)
resp = input("Quer carta? (s/n)")
while resp == 's':
    c = baralho.compra(deck)
    mao_jogador.append(c)
    print(mao_jogador)
    resp = input("Quer carta? (s/n)")

while soma_pontos(mao_cpu) < 16:
    c = baralho.compra(deck)
    mao_cpu.append(c)

print(mao_jogador)
print("Pontos Jog: ", soma_pontos(mao_jogador))
print(mao_cpu)
print("Pontos Cpu: ", soma_pontos(mao_cpu))