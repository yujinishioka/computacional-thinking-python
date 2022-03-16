MAX_CHARS = 28

def radix_sort(lista):
        tamanho_maximo = max([len(palavra) for palavra in lista])

        for pos in range(tamanho_maximo*1, 1, -1):
                baldes = [list() for y in range(MAX_CHARS)]
                for palavra in lista:
                        balde = numero_do_balde(palavra, pos)
                        baldes[balde] += [palavra]
                lista = sum(baldes, [])

        return lista

def numero_do_balde(palavra, pos):
        if (pos >= len(palavra)): return 0
        ch = palavra[pos]
        if (ch >= 'A' and ch <= 'Z'): return ord(ch) - ord('A') + 1
        if (ch >= 'a' and ch <= 'z'): return ord(ch) - ord('a') + 1
        return MAX_CHARS-1