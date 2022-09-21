lista_candidatos = []
lista_empresas = []
lista_vagas = []
lista_testes = []

# Lista das informações para o cadastro de candidato
# E-mail como segundo parametro para comparação
info_cadastro = ['Nome', 'E-mail', 'CPF', 'Senha', 'Hardskills', 'Interesses']

# Lista das informações para o cadastro da empresa
info_empresa = ['Nome da Empresa', 'CNPJ', 'Senha']

info_vaga = ['Nome da Empresa', 'Cargo', 'Cidade', 'Endereço', 'Salário', "Requisitos"]

info_teste = ['Enunciado', 'Alternativa A', 'Alternativa B', 'Alternativa C', 'Alternativa D', 'Alternativa E']

def mostrar_opcao():
    print("------------ MENU --------------")
    print("Opção 1 - Candidato")
    print("Opção 2 - Empresa")
    print("Opcão 0 - Sair")
    print("******************************")

def mostrar_opcao_candidato():
    print("------------ MENU --------------")
    print("Opção 1 - Cadastro de candidato")
    print("Opção 2 - Perfil do candidato")
    print("Opção 3 - Buscar candidato")
    print("Opção 4 - Visualizar etapas e resultados do candidato")
    print("Opção 5 - Acessar plataforma de vagas que se encaixam no perfil do candidato")
    print("Opção 6 - Acessar cursos recomendados")
    print("Opção 7 - Visualizar feedback enviado para os candidatos eliminados")
    print("Opção 0 - Voltar")
    print("******************************")

def mostrar_opcao_empresa():
    print("------------ MENU --------------")
    print("Opção 1 - Cadastro de empresa")
    print("Opção 2 - Cadastrar vagas")
    print("Opção 3 - Cadastrar testes da empresa")
    print("Opção 4 - Buscar candidato")
    print("Opção 5 - Plataforma de filtragem (percentual das aprovações e reprovações dos candidatos)")
    print("Opção 0 - Voltar")
    print("******************************")

def cadastrar_candidato():
    print("Opção cadastro de candidato selecionada! ")

    candidato = []

    for i in info_cadastro:
        txt_tela = (i + ": ")
        aux = str(input(txt_tela))

        # Teste de e-mail e CPF unico
        # Precisa implementar mais
        # if i == "E-mail" or i == "CPF":
        #     for c in lista_candidatos:
        #         if aux == c[1] or aux == c[2]:
        #             print(i + " ja cadastrado!\nTente novamente.")
        #             break

        candidato.append(aux)

    lista_candidatos.append(candidato)
    print("Cadastro realizado com sucesso!\n")

def perfil_candidato():
    print("Opção perfil do candidato selecionada!")

def buscar_candidato():
    print("Opção buscar candidato selecionada!")

    busca = str(input("Digite o nome do candidato: "))
    encontrado = False

    for candidato in lista_candidatos:
        if(busca == candidato[0]):
            i = 0
            print("******************************")

            while i < len(info_cadastro):
                if info_cadastro[i] != 'Senha':
                    print(info_cadastro[i] + ": "+ candidato[i])
                    encontrado = True
                    i += 1

                else:
                    i += 1
        
    if not encontrado:
        print("Candidato não encontrado.\n")

def mostrar_resultados():
    print("Opção visualizar etapas e resultados selecionada!")

def plataforma_vagas():
    print("Opção plataforma de vagas selecionada!")

    if lista_vagas != []:
        for vaga in lista_vagas:
            print(vaga)
    
    else:
        print('Não há vagas cadastradas no momento.')

def cursos_recomendados():
    print("Opção cursos recomendados selecionada!")

def feedback():
    print("Opção feedback sleecionada!")

def cadastrar_empresa():
    print("Opção cadastro de empresa selecionada!")

    empresa = []
    
    for i in info_empresa:
        txt_tela = (i + ": ")
        empresa.append(input(txt_tela))
    
    lista_empresas.append(empresa)
    print("Empresa cadastrada com sucesso!\n")

def cadastrar_vagas():
    print("Opção cadastrar vagas selecionada!")

    vaga = []

    for i in info_vaga:
        txt_tela = (i + ": ")
        vaga.append(input(txt_tela))
    
    lista_vagas.append(vaga)
    print("Vaga cadastrada com sucesso!\n")

def cadastrar_teste():
    print("Opção cadastrar testes selecionada!")

def plataforma_filtragem():
    print("Opção de filtragem selecionada!")