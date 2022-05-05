# Computacional Thinking

## Checkpoint 1

Exercício 1:
``` py
anos = int(input("Digite a quantidade de anos: "))
meses = int(input("Digite a quantidade de meses: "))
t = int(input("Digite um valor em meses para ser somado: "))

anos = ((meses + t)//12) + anos
meses = (meses + t)%12

print("Anos:", anos,"\nMeses:", meses)
```

Exercício 2:
``` py
kWh = float(input("Digite o valor de energia gasta em kWh: "))
icms = 0

if kWh <= 50:
    valor_consumo = 14
    valor_total = valor_consumo

if kWh > 50 and kWh < 100:
    valor_consumo = 14 + (kWh* 0.25)
    valor_total = valor_consumo

if kWh >= 100 and kWh <= 200:
    valor_consumo = 14 + (kWh * 0.25)
    icms = valor_consumo * 0.13
    valor_total = valor_consumo + icms

if kWh > 200:
    valor_consumo = 14 + (kWh * 0.25)
    icms = valor_consumo * 0.33
    valor_total = valor_consumo + icms

print("O consumo foi de: R$", valor_consumo, "\nICSM: R$", icms, "\nTOTAL: R$", valor_total)
```

Exercício 3:
``` py
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
```