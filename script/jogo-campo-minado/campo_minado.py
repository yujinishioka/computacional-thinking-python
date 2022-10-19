import random

def cria_campo(tam):
    # tamanho do campo e quantidade de bombas
    tamanho = tam
    campo = []

    for i in range(tamanho):
        campo.append([0] * tamanho)

    bombas = 0
    while bombas < tamanho:
        lin = random.randint(0, tamanho - 1)
        col = random.randint(0, tamanho - 1)

        if (lin != 0 or col !=0) and campo[lin][col] == 0:
            campo[lin][col] = 9
            bombas += 1

    for i in range(tamanho):
        for j in range(tamanho):
            if campo[i][j] == 9:
                aumenta_vizinho(campo, i, j)
    
    return campo

def aumenta_vizinho(campo, lin, col):
    if lin == 0:
        i = 0
        while i < 2:
            j = -1
            while j < 2:
                if (lin + i) < len(campo) and (col + i) < len(campo):
                    if campo[lin + i][col + i] != 9:
                        campo[lin + i][col + i] += 1
                j += 1
            i += 1
    
    if col == 0:
        i = -1
        while i < 2:
            j = 0
            while j < 2:
                if (lin + i) < len(campo) and (col + i) < len(campo):
                    if campo[lin + i][col + i] != 9:
                        campo[lin + i][col + i] += 1
                j += 1
            i += 1
    
    if lin > 0 and col > 0:
        i = -1
        while i < 2:
            j = -1
            while j < 2:
                if (lin + i) < len(campo) and (col + i) < len(campo):
                    if campo[lin + i][col + i] != 9:
                        campo[lin + i][col + i] += 1
                j += 1
            i += 1

print(cria_campo(10))
input("teste")