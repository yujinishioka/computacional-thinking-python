n_alunos = int(input("Digite a qntd de alunos: "))
notas=[]
i=0
total=0
alto = 0
baixo = 0

for i in range(n_alunos):
    notas.append(float(input("Digite as notas: ")))
    if notas[i] >= 5:
        alto += 1
    else:
        baixo += 1

    i+=1

for x in notas:
    total+=x

total = total/n_alunos

print("A media da sala é de:", total)
print("Notas acima ou igual à 5:", alto)
print("Notas abaixo de 5:", baixo)