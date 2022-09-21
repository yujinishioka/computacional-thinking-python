lista_candidatos = []
lista_empresas = []
lista_vagas = []
lista_testes = []
lista_cursos = []

# Lista de informações para o cadastro de candidato
# E-mail e CPF como segundo e terceiro parametros para comparação (ainda não implementado)
info_cadastro = ['Nome', 'E-mail', 'CPF', 'Senha', 'Hardskills', 'Interesses']
# Lista de informações para o cadastro da empresa
info_empresa = ['Nome da Empresa', 'CNPJ', 'Senha']
# Lista de informações para vagas
# ID precisa ser o primeiro parametro
info_vaga = ['ID', 'Nome da Empresa', 'Cargo', 'Cidade', 'Endereço', 'Salário', "Requisitos"]
# Lista de informações para testes
# ID precisa ser o primeiro parametro
info_teste = ['ID da Vaga', 'Enunciado', 'Alternativa A', 'Alternativa B', 'Alternativa C', 'Alternativa D', 'Resposta']
# Lista de informações para cursos
info_curso = ['Nome', 'Sobre', 'Horas', 'Valor']

def mostrar_opcao():
    print("------------ MENU --------------")
    print("Opção 1 - Candidato")
    print("Opção 2 - Empresa")
    print("Opção 3 - Sistema")
    print("Opcão 0 - Sair")
    print("******************************")

def mostrar_opcao_candidato():
    print("------------ MENU --------------")
    print("Opção 1 - Cadastro de candidato") # done
    print("Opção 2 - Buscar candidato") # done
    print("Opção 3 - Visualizar etapas e resultados do candidato")
    print("Opção 4 - Acessar plataforma de vagas que se encaixam no perfil do candidato") # done
    print("Opção 5 - Acessar cursos recomendados") # done
    print("Opção 6 - Visualizar feedback enviado para os candidatos eliminados")
    print("Opção 0 - Voltar")
    print("******************************")

def mostrar_opcao_empresa():
    print("------------ MENU --------------")
    print("Opção 1 - Cadastro de empresa") # done
    print("Opção 2 - Cadastrar vagas") # done
    print("Opção 3 - Cadastrar testes da empresa") # done
    print("Opção 4 - Buscar candidato") # done
    print("Opção 5 - Plataforma de filtragem (percentual das aprovações e reprovações dos candidatos)")
    print("Opção 0 - Voltar")
    print("******************************")

def mostrar_opcao_sistema():
    print("------------ MENU --------------")
    print("Opção 1 - Cadastrar cursos") # done
    print("Opção 0 - Voltar")
    print("******************************")

def mostrar_opcao_teste():
    print("- QUER SE CANDIDATAR A UMA VAGA? -")
    print("Opção 1 - Sim")
    print("Opção 2 - Não")
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
    def encontrar_vaga(vaga):
        encontrado = False

        for v in lista_vagas:
            if vaga == v:
                encontrado = True

        if encontrado:
            return True
        
        else:
            return False

    print("Opção plataforma de vagas selecionada!")

    if lista_vagas != []:
        for vaga in lista_vagas:
            cont = 0
            print("------------------------------")

            for item in vaga:
                print(info_vaga[cont], ":", item)
                cont += 1
        
        print("")
        mostrar_opcao_teste()
        op = int(input("Digite uma opção: "))

        while op != 2:
            if op == 1:
                id = int(input("Digite o ID da Vaga: "))
                encontrado = False

                # Falta implementação
                for vaga in lista_vagas:
                    print('vaga: ', vaga)
                    print('vaga[0]: ', vaga[0])
                    if id == vaga[0]:
                        for teste in lista_testes:
                            print('teste: ', teste)
                            print('teste[0]: ', teste[0])
                            if id == teste[0]:
                                print(teste)
                            
                        encontrado = True
                
                if not encontrado:
                    print("Vaga não encontrada.\nTente outro ID.")
            
            else:
                print("Por favor, digitar as opções disponíveis!!!")
            
            print("")
            mostrar_opcao_teste()
            op = int(input("Digite uma opção: "))
    
    else:
        print('Não há vagas cadastradas no momento.')

def cursos_recomendados():
    print("Opção cursos recomendados selecionada!")

    if lista_cursos != []:
        for curso in lista_cursos:
            print(curso)
    
    else:
        print('Não há cursos cadastrados no momento.')

def feedback():
    print("Opção feedback selecionada!")

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

    teste = []

    for i in info_teste:
        txt_tela = (i + ": ")
        teste.append(input(txt_tela))
    
    lista_testes.append(teste)
    print("Teste cadastrado com sucesso!\n")

def plataforma_filtragem():
    print("Opção de filtragem selecionada!")

def cadastrar_curso():
    print("Opção cadastrar curso selecionada!")

    curso = []

    for i in info_curso:
        txt_tela = (i + ": ")
        curso.append(input(txt_tela))
    
    lista_cursos.append(curso)
    print("Curso cadastrado com sucesso!\n")