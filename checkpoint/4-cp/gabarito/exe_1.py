tipo = ['Titulo', 'Ano', 'Faturamento', 'Diretor', 'Classificacao Etaria']
lista = []
i = 0

while i < len(tipo):
    aux = str(input('Digite o ' + tipo[i] + ' do filme: '))
    lista.append(aux)
    i += 1

print(lista)