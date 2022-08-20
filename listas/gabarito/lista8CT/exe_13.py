def arruma_portas(pessoas, portas):
    for porta in range(1, 1001):
        if porta % pessoas == 0:
            if portas[porta] == False:
                portas[porta] == True
            else:
                portas[porta] == False

portas = [False] * 1001

for person in range(1, 1001):
    arruma_portas(person, portas)

print(portas)

for num in range(1, 1001):
    if portas[num]:
        print(num)