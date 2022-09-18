def cacaPalavra (tamanho_matriz: int, matriz, qtd_palavras: int, palavras: list):
    pos_i = 0

    for i in matriz:
        pos_j = 0

        for j in matriz:
            print(matriz[pos_i][pos_j])
            pos_j += 1
            
        pos_i += 1

cacaPalavra(3, [['a','b','c'], ['d','e','f'], ['g','h','i']], 2, ['a','b', 'c'])