def busca_soma(vet, x):
    lista = []

    for i in vet:
        j = i + 1
        while j < len(vet):
            if (i + j) == x:
                aux_i = str(i)
                aux_j = str(j)
                lista.append("(" + aux_i + " e " + aux_j + ")")
            j += 1
        i += 1
    
    if lista == []:
        aux = str(x)
        return ("Nao existe valores que somados resultam em " + aux)
    
    if lista != []:
        texto = "Possibilidades: " + lista[0]
        
        for i in lista:
            if (i != lista[0]):
                texto += (" ou " + i)
        
        return texto

print(busca_soma([1,2,3,4,5,6,7,8], 9))