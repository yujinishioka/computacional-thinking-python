nomes = ("Ana", "Bia", "Celine", "Diana", "Eva", "Fabio")

def formar_duplas(nomes):
    i = 0
    while i < len(nomes) - 1:
        prox = i + 1

        while prox < len(nomes):
            dupla = str(nomes[i] + " e " + nomes[prox])
            print(dupla)
            prox += 1
        
        i += 1

formar_duplas(nomes)
