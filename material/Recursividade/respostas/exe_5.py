def soma(n):
    if n < 10:
        return n
    else:
        resto = n % 10
        return resto + soma(n // 10)

print(soma(10928940))