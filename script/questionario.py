nome = input("informe o seu nome: ")
idade = input("informe a sua idade: ")
curso = input("Ja fez algum curso superior (mesmo que nao tenha concluido)?  Qual?")
escolha = input ("Por que escolheu Tecnologia da Informacao (TI)?")
trabalho = input ("Dentro de TI, ja sabe no que voce gostaria de trabalhar?")
hobbie = input ("Quais sao seus hobbies")

arquivo = open("questionario.txt", mode='w')
arquivo.write(nome + "\n")
arquivo.write(idade + "\n")
arquivo.write(curso + "\n")
arquivo.write(escolha + "\n")
arquivo.write(trabalho + "\n")
arquivo.write(hobbie + "\n")
arquivo.close()