# 1º Checkpoint

Data: 05/04/2022

* Entrada e Saída de Dados
* Variáveis
* Operadores Aritméticos
* Comandos de Decisão

## Material de Estudo

---

### **Entrada e Saída de Dados**

Entrada: São os dados que fornecemos para o programa

Saída: São os resultados q o programa nos devolve

Tipo | Python
--- | ---
output | print("...")
input | variavel = input("texto")

---

### **Variáveis**

As variáveis armazenam informações dentro do programa, e ficam guardadas dentro da memória RAM. Podendo ser números inteiros/reais, caracteres ou booleanos (verdadeiro/falso)

Entrada de dados costumam ser armazenadas em variáveis

Variáveis podem ser iniciadas

**conversores**

Python | Conversão
--- | ---
int(numero) | transforma o texto em numero inteiro
float(numero) | transforma o texto em numero real
str(texto) | transforma o numero em uma string

---

### **Operadores Aritméticos**

Operador | Python
--- | ---
soma | +
subtração | -
multiplicação | *
divisão real | /
potência | **
resto da divisão | %
divisão inteira | //

``` python

# entrada de dados
numA = int(input(" Digite um numero: "))
numB = int(input(" Digite outro numero: "))

# calculos
soma = numA + numB
sub = numA - numB
prod = numA * numB
divr = numA / numB
pot = numA ** numB
resto = numA % numB
divi = numA // numB

# mostra na tela
print(" Soma: ", soma)
print(" Subtracao: ", sub)
print(" Produto: ", prod)
print(" Divisao real: ", divr)
print(" Potencia: ", pot)
print(" Resto: ", resto)
print(" Divisao inteira: ", divi)

```

---

### **Comandos de Decisão**

Significado | Python
--- | ---
igual | ==
menor | <
maior | >
diferente | !=
menor ou igual | <=
maior ou igual | >=

Uso do if/else:

``` python

# comando if/else
if <condição>:
    <instrucao>
    ...
else:
    <instrucao>

```

Exemplo:

``` python

# entrada de dados
placarA = int ( input (" Gols dotime A: "))
placarB = int ( input (" Gols dotime B: "))

# decidindo resultado
if placarA == placarB:
    print (" Empate ")
else:
    if placarA > placarB:
        print (" Time A vencedor")
    else:
        print (" Time B vencedor")

print (" Fim do programa ")

```

---

## Erros:

Em caso de erro "Non-ASCII character", inserir o comando no início do código.

```
# -*- coding: utf-8 -*-
```

Esse erro ocorre por conta de acentuações e podem ocorrer com Python 2, sendo resolvido com a formatação UTF-8.

---