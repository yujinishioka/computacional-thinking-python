import Imagem

def pinta_vizinhanca(mat, i, j):
    mat[i][j] = 255
    if i - 1 >= 0:
        mat[i-1][j] = 255
    if i + 1 < len(mat):
        mat[i+1][j] = 255
    if j - 1 >= 0:
        mat[i][j-1] = 255
    if j + 1 < len(mat[0]):
        mat[i][j+1] = 255               

def vanish(entrada, saida):
    matriz = Imagem.getMatrizImagemCinza(entrada)
    lin = len(matriz)
    col = len(matriz[0])
    resp = []
    i = 0
    while i < lin:
        resp.append([0] * col)
        i = i + 1
    for i in range(lin):
        for j in range(col):
            if matriz[i][j] == 255:
                pinta_vizinhanca(resp, i, j)    
    Imagem.salvaImagemCinza(saida, resp)

vanish('yao-ming.png', 'yao1.png')
vanish('yao1.png', 'yao2.png')
vanish('yao2.png', 'yao3.png')
print("Finalizado.")