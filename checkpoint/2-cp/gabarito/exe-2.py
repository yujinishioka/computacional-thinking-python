qntd_produtos = int(input("Digite a quantidade de produtos: "))

while qntd_produtos < 1:
    qntd_produtos = int(input("A quantidade de produtos precisa ser maior do que 0. Digite outro valor: "))

i = 0

while i < qntd_produtos:
    i += 1
    n_produto = str(i)
    txt = "Digite o valor inicial do Produto " + n_produto + ": R$ "
    preco_i = float(input(txt))
    txt = "Agora o valor final do Produto " + n_produto + ": R$ "
    preco_f = float(input(txt))

    aum_reais = preco_f - preco_i
    aum_perce = ((preco_f / preco_i) * 100) - 100

    if i == 1:
        max_reais = aum_reais
        max_perce = aum_perce
        produto_reais = produto_perce = i
    
    if i > 1:
        if max_reais < aum_reais:
            max_reais = aum_reais
            produto_reais = i
        
        if max_perce < aum_perce:
            max_perce = aum_perce
            produto_perce = i

print("-----------------------------------")

if max_reais < 0:
    print("Não tivemos aumento no preço dos produtos.")
else:
    print("Maior aumento em reais: R$", max_reais)
    print("no produto:", produto_reais)
    print("")

if max_perce > 0:
    print("Maior aumento porcentual: R$", max_perce, "%")
    print("no produto:", produto_perce)