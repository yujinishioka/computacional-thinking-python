cedula = int(input("Digite o valor da cédula: "))
moeda_a = float(input("Digite o valor da primeira moeda: "))
moeda_b = float(input("Digite o valor da segunda moeda: "))

cont_a = sum = 0
divisivel = False

while sum <= cedula:
    cont_b = 0
    while sum <= cedula:
        if sum == cedula:
            divisivel = True
            break

        sum += moeda_b
        cont_b += 1

    if sum == cedula:
        divisivel = True
        break
    
    cont_a += 1
    sum = cont_a * moeda_a

if divisivel:
    print("É possível fazer a conversão de", cedula, "com")
    print(cont_a, "Moedas de", moeda_a)
    print(cont_b, "Moedas de", moeda_b)

else:
    print("Não foi possível fazer a conversão")