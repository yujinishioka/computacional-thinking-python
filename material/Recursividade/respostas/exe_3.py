def elevar(n):
    if n == 0:
        return 1
    else:
        return n * elevar(n - 1)

print(elevar(8))