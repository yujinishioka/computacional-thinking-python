import Imagem

matriz = Imagem.getMatrizImagemCinza('./img/domino.png')

lin = len(matriz)
col = len(matriz[0])

x = int(col * 0.22)

teste = []
for i in range(12, 50):
    teste.append(matriz[i][14:x])

Imagem.salvaImagemCinza('./img/domino_unico.jpg', teste)
print('Finalizado.')