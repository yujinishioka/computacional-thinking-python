from dis import disco


def hanoi(total): # total = numero de discos
    discos = []
    move = []

    if total < 2:
        print("A Torre de Hanoi precisa de pelo menos 2 Discos")
    
    else:
        for i in range(1, total + 1):
            discos.append(i)
        
        origem = "A"
        aux = "B"
        destino = "C"
        
        if total == 2:
                print("1 -> B")
                print("2 -> C")
                print("1 -> C")

        print(discos)

hanoi(1)