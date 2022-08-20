import funcao.funcao_velha as jogo

tabuleiro = jogo.cria_tabuleiro()
jogador = 'X'

while jogo.espaco_branco(tabuleiro) and not jogo.existe_ganhador(tabuleiro):
    jogo.imprime(tabuleiro)

    print("Vez do Jogador:", jogador)
    lin = int(input("Linha: "))
    col = int(input("Coluna: "))
    resp = jogo.joga(tabuleiro, lin, col, jogador)

    if resp == True:
        jogador = jogo.troca_jogador(jogador)
    else:
        print("Jogada Invalida.")

jogador = jogo.troca_jogador(jogador)

if jogo.existe_ganhador(tabuleiro):
    print(jogador + " Ganhou!")
else:
    print("Deu Velha!")
