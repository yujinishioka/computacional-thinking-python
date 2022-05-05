numero = int(input("Digite a quantidade de numeros: "))
i = cont = 0
array = []

while i < numero:
    aux = int(input("Adicione o numero: "))
    array.append(aux)

    if i == 0:
        cont += 1

    if i > 0:
        if array[i-1] != array[i]:
            cont += 1
        
    i += 1

print("Numeros digitados:", array)
print("Segmentos de numeros iguais:", cont)