from exe_1 import intercala as inter

def merge_sort(vetor, p, r):
    if p >= r:
        print("Esta ordenado")

    else:
        meio = (p + r) // 2
        merge_sort(vetor, p, meio)
        merge_sort(vetor, meio + 1, r)
        inter(vetor, p, meio, r)
