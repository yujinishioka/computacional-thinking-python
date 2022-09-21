import funcionalidades as f

txt_op = "Digite uma opção: "
txt_voltar = "Opção voltar selecionada"
txt_inv = "Por favor, digitar as opções disponíveis!!!"

f.mostrar_opcao()
ce = int(input(txt_op))

while ce != 0:

    if ce == 1:
        print("Opção candidato selecionada!")
        f.mostrar_opcao_candidato()
        op = int(input(txt_op))

        while op != 0:
            if op == 1:
                f.cadastrar_candidato()

            elif op == 2:
                f.buscar_candidato()

            elif op == 3:
                f.mostrar_resultados()

            elif op == 4:
                f.plataforma_vagas()

            elif op == 5:
                f.cursos_recomendados()

            elif op == 6:
                f.feedback()

            else:
                print(txt_inv)

            f.mostrar_opcao_candidato()
            op = int(input(txt_op))
        
        print(txt_voltar)
    
    elif ce == 2:
        print("Opção empresa selecionada!")
        f.mostrar_opcao_empresa()
        op = int(input(txt_op))

        while op != 0:
            if op == 1:
                f.cadastrar_empresa()
            
            elif op == 2:
                f.cadastrar_vagas()
            
            elif op == 3:
                f.cadastrar_teste()
            
            elif op == 4:
                f.buscar_candidato()
            
            elif op == 5:
                f.plataforma_filtragem()
            
            else:
                print(txt_inv)
            
            f.mostrar_opcao_empresa()
            op = int(input(txt_op))

    elif ce == 3:
        print("Opção sistema selecionada!")
        f.mostrar_opcao_sistema()
        op = int(input(txt_op))

        while op != 0:
            if op == 1:
                f.cadastrar_curso()
            
            else:
                print(txt_inv)
            
            f.mostrar_opcao_sistema()
            op = int(input(txt_op))

    else:
        print(txt_inv)
    
    f.mostrar_opcao()
    ce = int(input(txt_op))
       
print("Opção sair selecionada!")