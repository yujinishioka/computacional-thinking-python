def hanoi(discos, origem, aux, destino):
    if discos == 2:
        print("1 -> ", aux)
        print("2 -> ", destino)
        print("1 -> ", destino)
    else:
        hanoi(discos - 1, origem, destino, aux)
        print(discos, "->", destino)
        hanoi(discos - 1, aux, origem, destino)

hanoi(4, 'A', 'B', 'C')
