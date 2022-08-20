def cria_tabuleiro():
    matriz = []
    for i in range(3):
        lin = []
        for j in range(3):
            lin.append('_')
        matriz.append(lin)

    return matriz

def troca_jogador(jog):
    if jog == 'X':
        return 'O'
    else:
        return 'X'

def espaco_branco(matriz):
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == '_':
                return True
    return False

def existe_ganhador(matriz):
    for x in range(3):
        if matriz[x][0] == matriz[x][1] and matriz[x][1] == matriz[x][2] and matriz[x][0] != '_':
            return True

        if matriz[0][x] == matriz[1][x] and matriz[1][x] == matriz[2][x] and matriz[0][x] != '_':
            return True
    
    if matriz[0][0] == matriz[1][1] and matriz[1][1] == matriz[2][2] and matriz[0][0] != '_':
        return True
    
    if matriz[0][2] == matriz[1][1] and matriz[1][1] == matriz[2][0] and matriz[0][2] != '_':
        return True
    
    return False
    
def joga(matriz, lin, col, jogador):
    if lin < 0 or lin > 2 or col < 0 or col > 2:
        return False
    
    if matriz[lin][col] != '_':
        return False
    
    matriz[lin][col] = jogador
    return True

def imprime(matriz):
    cont = 0
    print("Jogo da Velha")
    print("['0']['1']['2'][-]")
    for lin in matriz:
        if len(lin) < 4:
            lin.append(cont)
            
        print(lin)
        cont += 1
