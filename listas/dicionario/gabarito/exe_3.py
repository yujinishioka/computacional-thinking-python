import re

livro = "alice.txt"
resp = "palavras_em_alice.txt"

dic = {}

with open(livro, "r") as arquivo:
    for linha in arquivo:
        linha = re.sub(r'[^ a-zA-Z0-9\']', '', linha)
        min = linha.lower()
        palavras = min.split(" ")

        for palavra in palavras:
            if palavra in dic:
                dic[palavra] = dic[palavra] + 1
            else:
                dic[palavra] = 1

lista = []
for palavra in dic:
    lista.append(palavra)

lista.sort()

with open(resp, "w") as n_arquivo:
    for palavra in lista:
        num = str(dic[palavra])
        aux = str(palavra + ' = ' + num + '\n')
        n_arquivo.write(aux)

print("Finalizado")