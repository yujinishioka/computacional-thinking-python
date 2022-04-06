ano_ant = float(input("Digite o valor médio de consumo de agua do ano passado em m3: "))
mes_vig = float(input("Digite a quantidade de agua desse mes em m3: "))

if mes_vig <= 20:
    valor = mes_vig * 2

if mes_vig > 20 and mes_vig <= 35:
    valor = mes_vig * 3.5

if mes_vig > 35 and mes_vig <= 50:
    valor = mes_vig * 5.5

if mes_vig > 50:
    valor = mes_vig * 7

if mes_vig < ano_ant:
    desconto = valor * 0.2
    valor = valor - desconto
    print("O desconto foi de:", desconto)
    
if mes_vig > ano_ant * 1.1:
    multa = valor * 0.3
    valor = valor + multa
    print("A multa foi de: R$", multa)

print("O valor a pagar é de: R$", valor)