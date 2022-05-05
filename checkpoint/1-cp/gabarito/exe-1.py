anos = int(input("Digite a quantidade de anos: "))
meses = int(input("Digite a quantidade de meses: "))
t = int(input("Digite um valor em meses para ser somado: "))

anos = ((meses + t)//12) + anos
meses = (meses + t)%12

print("Anos:", anos,"\nMeses:", meses)