def busca_binaria(vetor, elem, inicio, fim):
    if fim < inicio:
        return -1
    else:
        meio = (inicio + fim) // 2
        if vetor[meio] < elem:
            return busca_binaria(vetor, elem, meio + 1, fim)
        elif vetor[meio] > elem:
            return busca_binaria(vetor, elem, inicio, meio - 1)
        else:
            return meio

