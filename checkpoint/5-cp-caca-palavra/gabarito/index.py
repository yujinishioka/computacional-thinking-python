# D:/GitHub/FIAP/computacional-thinking-python/checkpoint/5-cp-caca-palavra/gabarito/

# rota do arquivo para ser lido (IMPORTANTE!!)
caminho = "cacapalavra.txt"

# rota para o diagrama de letras (arquivo gerado)
diagrama = "diagrama.txt"

# rota para as palavras buscadas (arquivo gerado)
lista = "lista.txt"

# rota para as respostas do Caca Palavra (arquivo gerado)
resposta = "resposta.txt"

with open(caminho, "r", encoding="utf-8") as arquivo:
    palavras = []
    textos = []
    i = 0

    for linha in arquivo:
        if i == 0:
            tamanho = int(linha)

            # pos_qp = posicao da quantidade de palavras
            pos_qp = tamanho + 1

            # criando a matriz
            matriz = []

            for linha_matriz in range(0, tamanho):
                lm = []
                for item in range(0, tamanho):
                    lm.append('x')
                matriz.append(lm)
        
        if i > 0 and i < pos_qp:
            mi = i - 1
            mj = 0
            aux = linha.replace("\n", "")

            for letra in aux:
                matriz[mi][mj] = letra
                mj += 1

        if i == pos_qp:
            quantidade_palavras = int(linha)
        
        if i > pos_qp and i <= pos_qp + quantidade_palavras:
            aux = linha.replace("\n", "")
            palavras.append(aux)
        
        i = i + 1
    
    for palavra in palavras:
        encontrado = False
        i = 0

        while i < tamanho and not encontrado:
            j = 0

            while j < tamanho and not encontrado:
                
                if palavra[0] == matriz[i][j]:
                    ajuste_i = i + 1
                    ajuste_j = j + 1
                    i_str = str(ajuste_i)
                    j_str = str(ajuste_j)
                    prox = 1

                    # validar tamanho (coluna)
                    if j + len(palavra) < tamanho:

                        # horizontal para frente
                        while palavra[prox] == matriz[i][j+prox] and not encontrado:

                            if prox == len(palavra) - 1:

                                aux_string = str(palavra + " se encontra na linha " + i_str + " e coluna " + j_str + " na horizontal.")
                                textos.append(aux_string)
                                encontrado = True
                                break
                    
                            prox += 1
                        
                        # validar tamanho (linha)
                        if i - len(palavra) + 1 >= 0:

                            # diagonal direita e para cima
                            while palavra[prox] == matriz[i - prox][j + prox] and not encontrado:

                                if prox == len(palavra) - 1:

                                    aux_string = str(palavra + " se encontra na linha " + i_str + " e coluna " + j_str + " na diagonal a direita e para cima.")
                                    textos.append(aux_string)
                                    encontrado = True
                                    break
                                
                                prox += 1
                        
                        # validar tamanho (linha)
                        if i + len(palavra) < tamanho:

                            # diagonal direita e para baixo
                            while palavra[prox] == matriz[i + prox][j + prox] and not encontrado:

                                if prox == len(palavra) - 1:

                                    aux_string = str(palavra + " se encontra na linha " + i_str + " e coluna " + j_str + " na diagonal a direita e para baixo.")
                                    textos.append(aux_string)
                                    encontrado = True
                                    break
                                
                                prox += 1

                    # validar tamanho (coluna)
                    if j - len(palavra) + 1 >= 0:

                        # horizontal de trás pra frente
                        while palavra[prox] == matriz[i][j-prox] and not encontrado:

                            if prox == len(palavra) - 1:

                                aux_string = str(palavra + " se encontra na linha " + i_str + " e coluna " + j_str + " na horizontal invertida.")
                                textos.append(aux_string)
                                encontrado = True
                                break
                    
                            prox += 1
                        
                        # validar tamanho (linha)
                        if i - len(palavra) + 1 >= 0:

                            # diagonal esquerda e para cima
                            while palavra[prox] == matriz[i - prox][j - prox] and not encontrado:

                                if prox == len(palavra) - 1:

                                    aux_string = str(palavra + " se encontra na linha " + i_str + " e coluna " + j_str + " na diagonal a esquerda e para cima.")
                                    textos.append(aux_string)
                                    encontrado = True
                                    break
                                
                                prox += 1
                        
                        # validar tamanho (linha)
                        if i + len(palavra) < tamanho:

                            # diagonal esquerda e para baixo
                            while palavra[prox] == matriz[i + prox][j - prox] and not encontrado:

                                if prox == len(palavra) - 1:

                                    aux_string = str(palavra + " se encontra na linha " + i_str + " e coluna " + j_str + " na diagonal a esquerda e para baixo.")
                                    textos.append(aux_string)
                                    encontrado = True
                                    break
                                
                                prox += 1

                    # validar tamanho (linha)
                    if i + len(palavra) < tamanho:

                        # vertical para baixo
                        while palavra[prox] == matriz[i+prox][j] and not encontrado:

                            if prox == len(palavra) - 1:

                                aux_string = str(palavra + " se encontra na linha " + i_str + " e coluna " + j_str + " na vertical.")
                                textos.append(aux_string)
                                encontrado = True
                                break
                    
                            prox += 1

                    # validar tamanho (linha)
                    if i - len(palavra) + 1 >= 0:

                        # vertical para cima
                        while palavra[prox] == matriz[i-prox][j] and not encontrado:

                            if prox == len(palavra) - 1:

                                aux_string = str(palavra + " se encontra na linha " + i_str + " e coluna " + j_str + " na vertical invertida.")
                                textos.append(aux_string)
                                encontrado = True
                                break
                                
                            prox += 1

                j += 1

            i += 1

    arquivo.close()

# arquivo do diagrama
with open(diagrama, "w", encoding="utf-8") as dia:
    cont = 1

    dia.write("Diagrama:\n\n")

    for linha in matriz:
        aux = str(cont)

        if len(aux)  == 1:
            aux += '.  '
        
        if len(aux) == 2:
            aux += '. '
        
        dia.write(aux)

        for letra in linha:
            dia.write(letra)
            dia.write(" ")

        dia.write("\n")
        cont += 1

    dia.close()

# arquivo da lista
with open(lista, "w", encoding="utf-8") as lista:
    cont = 1

    lista.write("Palavras:\n\n")

    for palavra in palavras:
        aux = str(cont)
        aux += ". "
        lista.write(aux)
        lista.write(palavra)
        lista.write("\n")
        cont += 1

    lista.close()

# arquivo das respostas
with open(resposta, "w", encoding="utf-8") as res:
    cont = 1

    res.write("Resposta do Cacao Palavra:\n\n")

    for texto in textos:
        aux = str(cont)
        aux += '. '
        res.write(aux)
        res.write(texto)
        res.write("\n")
        cont += 1

    res.close()

print("Finalizado com sucesso.")