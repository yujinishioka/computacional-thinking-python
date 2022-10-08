def somatoria(lst, pos):
    if pos == len(lst) - 1:
        return lst[pos]
    else:
        return lst[pos] + somatoria(lst, pos + 1)

l = [12, 54, 90, -43, 10]
print(somatoria(l, 0))
