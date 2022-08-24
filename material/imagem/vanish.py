import Imagem

matriz = Imagem.getMatrizImagemCinza('./img/yao-ming.png')

for i in range(len(matriz)-1):
  for j in range(len(matriz[0])-1):
    if matriz[i][j] == 255:
      x = -1
      while x < 2:
        matriz[i+x][j] = 255
        matriz[i][j+x] = 255
        matriz[i+x][j+x] = 255
        x += 1

Imagem.salvaImagemCinza('./img/yao-ming_novo1.png', matriz)
print('Finalizado')