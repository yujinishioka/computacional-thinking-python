import Imagem

matriz = Imagem.getMatrizImagemCinza('./img/naturezaMorta_cinza.jpg')

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] <= 127:
            matriz[i][j] = 0
        else:
            matriz[i][j] = 255

Imagem.salvaImagemCinza('./img/natureza_morta_black.jpg', matriz)
print('Finalizado.')