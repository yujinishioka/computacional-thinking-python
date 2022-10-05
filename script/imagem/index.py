# # Alterando imagem cinza
#
# import Imagem

# matriz = Imagem.getMatrizImagemCinza('./img/olhos.jpg')

# print("Linhas: ", len(matriz))
# print("Colunas: ", len(matriz[0]))

# for i in range(len(matriz)):
#   for j in range(len(matriz[0])):
#     if matriz[i][j] > 128:
#       matriz[i][j] = 255
#     else:
#       matriz[i][j] -= 64
#       if matriz[i][j] < 0:
#         matriz[i][j] = 0

# Imagem.salvaImagemCinza('./img/olhos_novo.jpg', matriz)
# print("Finalizado")
#

# # Alterando imagem colorida
#
import Imagem

matrizes = Imagem.getMatrizImagemColorida('./img/lago_canada.jpg')

matrizR = matrizes[0]
matrizG = matrizes[1]
matrizB = matrizes[2]

for i in range(len(matrizes)):
  for j in range(len(matrizes[0])//2):
    matrizR[i][j] = matrizR[i][j] * 50
    matrizG[i][j] = matrizG[i][j] * 50
    matrizB[i][j] = matrizB[i][j] * 50

Imagem.salvaImagemColorida('./img/lago_canada_novo.jpg', matrizR, matrizG, matrizB)
print('Finalizado')