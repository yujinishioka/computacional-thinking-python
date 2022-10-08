def inverte(num):
    if num < 10:
        return str(num)
    else:
        un = num % 10
        return str(un) + inverte(num // 10)

print(inverte(3209))