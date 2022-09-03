def par_de_soma(vet, x):
    first_load = True
    c = []
    item = []

    for i in vet:
        if(not first_load):
            for j in c:
                if(i == j):
                    aux1 = str(x - i)
                    aux2 = str(i)
                    item.append("[" + aux1 + " e " + aux2 + "]")
            c.append(x - i)
        
        if(first_load):
            c.append(x - i)
            first_load = False

    if item == []:
        aux = str(x)
        return ("Nao existe valores que somados resultam em " + aux)
    
    if item != []:
        texto = "Possibilidades: " + item[0]
        
        for i in item:
            if (i != item[0]):
                texto += (" ou " + i)
        
        return texto

print(par_de_soma([1,2,3,4,5,6,7], 9))