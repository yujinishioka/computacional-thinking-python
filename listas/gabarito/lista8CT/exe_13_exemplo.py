def arruma_portas(pes, portas):
    for num_porta in range(1, 1001):
        if num_porta % pes == 0:
            #mudando o estado da porta
            #portas[num_porta] = not portas[num_porta]
            if portas[num_porta] == False:
                portas[num_porta] = True
            else:
                portas[num_porta] = False


doors = [False] * 1001
for person in range(1, 1001):
    arruma_portas(person, doors)

for num in range(1, 1001):
    if doors[num]:
        print(num)