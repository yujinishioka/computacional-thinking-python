cedula = int(input("Digite o valor da cédula: "))
moeda_a = float(input("Digite o valor da primeira moeda: "))
moeda_b = float(input("Digite o valor da segunda moeda: "))

cont_a = acumulador = 0
divisivel = False

while acumulador <= cedula:
    cont_b = 0
    while acumulador <= cedula:
        if acumulador == cedula:
            divisivel = True
            break

        acumulador += moeda_b
        cont_b += 1

    if acumulador == cedula:
        divisivel = True
        break
    
    cont_a += 1
    acumulador = cont_a * moeda_a

if divisivel:
    print("É possível fazer a conversão de", cedula, "com")
    print(cont_a, "Moedas de", moeda_a)
    print(cont_b, "Moedas de", moeda_b)

else:
    print("Não foi possível fazer a conversão")