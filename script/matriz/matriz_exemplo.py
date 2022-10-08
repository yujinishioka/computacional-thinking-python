def soma(ma, mb):
    if len(ma) != len(mb) or len(ma[0]) != len(mb[0]):
        return "Tamanho de matarizes são diferentes"

    else:
        lin = len(ma)
        col = len(ma[0])
        resp = []

        for i in range(lin):
            resp.append([0] * col)
        
        for i in range(lin):
            for j in range(col):
                resp[i][j] = ma[i][j] + mb[i][j]
        
        return resp

a = [[1,2,3], [4,5,6], [7,8,9]]
b = [[1,2,3], [4,5,6], [7,8,9]]

matriz = soma(a, b)
print(matriz)