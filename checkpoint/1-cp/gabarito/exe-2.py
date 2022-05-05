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