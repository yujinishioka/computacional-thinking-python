dia = int(input(" Digite o dia: "))
mes = int(input(" Digite o mes: "))

if mes == 2 and dia <= 28 and dia > 0:
    print(" Data Valida")
else:

    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 and dia <= 31 and dia > 0:
        print(" Data Valida")
    else:

        if mes == 4 or mes == 6 or mes == 9 or mes == 11 and dia <= 30 and dia > 0:
            print(" Data Valida")
        else:
            print("Data Invalida")