#enquanto haCasasEmBranco(matriz):
#    pega uma casa em branco
#    resp = tentaColocarNumero(matriz, casa, num)
#    if resp == True:
#       guarda na pilha essa casa 
#       e vai para a proxima
#    else:
#       volta para casa anterior
#       limpa o numero do jogo do sudoku
#       tenta colocar outro numero nessa casa    
    
from pilha import Pilha

def verifica_linha(mat, l, num):
    for c in range(9):
        if mat[l][c] == num:
            return False

    return True

def verifica_coluna(mat, c, num):
    for l in range(9):
        if mat[l][c] == num:
            return False

    return True

def verifica_quadrante(mat, l, c, num):
    ini_lin = (l // 3) * 3
    ini_col = (c // 3) * 3

    for lin in range(ini_lin, ini_lin + 3):
        for col in range(ini_col, ini_col + 3):
            if mat[lin][col] == num:
                return False

    return True

def tentaColocarNumero(mat, l, c, num):
    if num > 9:
        return False

    resp_linha = verifica_linha(mat, l, num)
    resp_coluna = verifica_coluna(mat, c, num)
    resp_quad = verifica_quadrante(mat, l, c, num)

    if resp_linha and resp_coluna and resp_quad:
        mat[l][c] = num
        return True

    else:
        return False

def imprime(matriz):
    for lin in matriz:
        print(lin)

matriz = []
matriz.append([3, 0, 6, 5, 0, 8, 4, 0, 0])
matriz.append([5, 2, 0, 0, 0, 0, 0, 0, 0])
matriz.append([0, 8, 7, 0, 0, 0, 0, 3, 1])
matriz.append([0, 0, 3, 0, 1, 0, 0, 8, 0])
matriz.append([9, 0, 0, 8, 6, 3, 0, 0, 5])
matriz.append([0, 5, 0, 0, 9, 0, 6, 0, 0])
matriz.append([1, 3, 0, 0, 0, 0, 2, 5, 0])
matriz.append([0, 0, 0, 0, 0, 0, 0, 7, 4])
matriz.append([0, 0, 5, 2, 0, 6, 3, 0, 0])    

imprime(matriz)

p = Pilha()
lin = 0
col = 0
num = 1

while lin != 8 or col != 8:
    if matriz[lin][col] == 0:
        resp = tentaColocarNumero(matriz, lin, col, num)

        if resp == True:
            p.put([lin, col])
            col = col + 1

            if col == 9:
                col = 0
                lin = lin + 1
            num = 1

        else: #nao consegui colocar o num na posicao lin, col
            num = num + 1
            matriz[lin][col] = 0

            if num >= 10:
                pos = p.pop()
                lin = pos[0]
                col = pos[1]
                num = matriz[lin][col] + 1
                matriz[lin][col] = 0

    else:
        col = col + 1

        if col == 9:
            col = 0
            lin = lin + 1

print("***************************")            
imprime(matriz)