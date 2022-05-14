palavra = str(input('Digite uma palavra: '))

def inserir(palavra):
    nova = ''
    i = 0
    while i < len(palavra):
        nova += palavra[i] + ' '
        i += 1
    return nova

resp = inserir(palavra)
print(resp)