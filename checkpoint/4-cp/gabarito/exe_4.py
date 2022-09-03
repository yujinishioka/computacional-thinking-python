def exclusivos(a, b):
    i = 0

    while i < len(a):
        j = 0

        while j < len(b):
            if a[i] == b[j]:
                a.pop(i)
                b.pop(j)
                i -= 1

            j+= 1

        i += 1
        
    c = []

    for item in a:
        c.append(item)
    
    for item in b:
        c.append(item)
    
    return (c)

a = [3, 6, -4, 19, 5, 1, -10, 9]
b = [2, -1, 0, 5, 6, 9, 7, 3]

print(exclusivos(a, b))