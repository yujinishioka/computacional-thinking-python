l = [1, 14, 3 ,17, 5, 28, 71, 12, 2, 55, 44, 13, 91]

def separa(l, x):
    maior = []
    menor = []
    i = 0

    while i < len(l):
        if l[i] <= x:
            menor.append(l[i])

        else:
            maior.append(l[i])

        i += 1
    
    return(menor, maior)

print(separa(l, 25))