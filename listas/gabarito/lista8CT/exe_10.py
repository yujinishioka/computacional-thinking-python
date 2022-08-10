def intercala(a, b):
    resultado = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            resultado.append(a[i])
            i += 1
        else:
            resultado.append(b[j])
            j += 1

    while i < len(a):
        resultado.append(a[i])
        i += 1
    
    while j < len(b):
        resultado.append(b[j])
        j += 1
    
    print(resultado)

intercala([1, 4, 7, 9], [2, 8, 11, 13])