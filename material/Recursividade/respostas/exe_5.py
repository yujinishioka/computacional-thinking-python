def somar(n):
    resto = n % 10
    if n / 10 < 1:
        return n
    else:
        return resto + somar(n // 10)

print(somar(10928940))