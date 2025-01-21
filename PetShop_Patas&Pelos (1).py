usuariosA = [['Julya', '123','A']]
usuariosC =[]
usuariosD =[]
pets =[]
atendimento =[]
servicos =[]
print(usuariosA)
while True:
    login = False
    if len(usuariosA) == 0:
        print('Não há usuários cadastrados.\nCadastre um usuário')
        nomeUsuario = input("Nome de login: ")
        senha = input("Digite uma senha forte:")
        usuariosA.append([nomeUsuario,senha,'A'])
        login = True
    else:
        nomeUsuario = input('Digite o nome de usuário:')
        senha = input("Digite uma senha forte:")
        for i in range(len(usuariosA)):
            if nomeUsuario == usuariosA[i][0]:
                if senha == usuariosA[i][1]:
                    print("Usuario Autenticado!\n")
                    login = True
                    break
    if login:
        break
    else:
        print("Usuário ou senha inválidos!\n")
while True:
    print("PET SHOP PATAS & PÊLOS.\n")
    print("1.Cadastros")
    print("2.Atendimentos")
    print("3-Consultas/Relatorios")
    print("4.Sair")

    opcao = input("\nSelecione uma opção:")

    if opcao == '1':
        while True:
            print("\nCadastros:\n")
            print("1.Usuarios (Administrador)")
            print("2.Clientes")
            print("3.Pets")
            print("4.Serviços (Administrador)")
            print("5.Voltar ao Menu Principal")

            opcao = input("\nSelecione uma opção:")

            if opcao == '1':
                    print("\nUsuarios (Administrador)\n")
                    print("1.Cadastrar novo Administrador")
                    print("2.Atualizar")
                    print("3.Apagar")
                    print("4.Consultar")
                    print("5.Voltar ao 'Menu Cadastros'\n")

                    opcao = input("\nSelecione uma opção:")
                    if opcao == '1':
                        nomeUsuario = input("Nome de login: ")
                        senha = input("Digite uma senha forte:")
                        usuariosA.append([nomeUsuario,senha,'A'])
                        print("Usuario Cadastrado!")

                    elif opcao == '2':  # Atualizar usuário
                        atualizar = input("Digite o nome de login do usuário que deseja atualizar: ")

                        # Encontrar o usuário na lista
                        usuario_encontrado = False
                        for usuario in usuariosA:
                            if usuario[0] == atualizar:
                                usuario_encontrado = True
                                
                                # Solicita novos dados ao usuário
                                novo_nome = input(f"Digite o novo nome de login (ou pressione Enter para manter '{usuario[0]}'): ")
                                nova_senha = input("Digite a nova senha (ou pressione Enter para manter a senha atual): ")
                                
                                # Atualiza os dados conforme necessário
                                if novo_nome:
                                    usuario[0] = novo_nome
                                if nova_senha:
                                    usuario[1] = nova_senha
                                    
                                print(f"Usuário '{atualizar}' atualizado com sucesso!")
                                break

                        if not usuario_encontrado:
                            print("Usuário não encontrado.")

                        print("Lista atualizada de usuários:", usuariosA)

                    elif opcao == '3':  # Apagar usuário
                        apagar = input("Digite o nome de login que deseja apagar: ")

                        # Encontrar o usuário na lista
                        usuario_encontrado = False
                        for usuario in usuariosA:
                            if usuario[0] == apagar:
                                usuariosA.remove(usuario)
                                usuario_encontrado = True
                                print(f"\nUsuário '{apagar}' removido com sucesso!")
                                break

                        if not usuario_encontrado:
                            print("Usuário não encontrado.")

                        #print("\nLista atualizada de usuários:", usuariosA)
                    elif opcao == '4':
                         print(usuariosA)

                    elif opcao == '5':
                         break

            elif opcao == '2':
                    print("\nClientes\n")
                    print("1.Cadastrar novo Cliente")
                    print("2.Atualizar")
                    print("3.Apagar (Administrador)")
                    print("4.Consultar")
                    print("5.Voltar ao 'Menu Cadastros'\n")

                    opcao = input("\nSelecione uma opção:")
                    if opcao == '1':
                        nomeUsuario = input("Digite o nome do cliente: ")
                        email = input("Digite email:")
                        celular = input("Digite um telefeno/celular:")
                        usuariosC.append([nomeUsuario,email,celular,'C'])
                        print("Cliente Cadastrado!")

                    elif opcao == '2':
                        atualizar = input("Digite o nome do cliente que deseja atualizar: ")

                        usuario_encontrado = False
                        for usuario in usuariosC:
                            if usuario[0] == atualizar:
                                usuario_encontrado = True
                                
                                novo_nome = input(f"Digite o novo nome do Cliente (ou pressione Enter para manter '{usuario[0]}'):")
                                novo_email = input("Digite o novo nome do Cliente (ou pressione Enter para manter): ")
                                novo_celular = input("Digite o novo nuemro de telefone do Cliente (ou pressione Enter para manter): ")
                                
                                if novo_nome:
                                    usuario[0] = novo_nome
                                if novo_email:
                                    usuario[1] = novo_email
                                if novo_celular:
                                    usuario[2] = novo_celular
                                    
                                print(f"Usuário '{atualizar}' atualizado com sucesso!")
                                break
                        if not usuario_encontrado:
                            print("\nUsuário não encontrado.")
                            
                    elif opcao == '3':
                         apagar = input("Digite a ficha do cliente que deseja apagar: ")
                         
                         usuario_encontrado = False
                         for usuario in usuariosC:
                             usuariosC.remove(usuario)
                             usuario_encontrado = True
                             print(f"\nCliente '{apagar}' removido com sucesso!")
                             break
                         
                         if not usuario_encontrado:
                             print("\nUsuário não encontrado.")

                    elif opcao == '4':
                         print(usuariosC)
                        
                    elif opcao == '5':
                         break

                
            elif opcao == '3':
                 while True:
                        print("\nPets\n")
                        print("1 .Cadastrar novo Pet")
                        print("2 .Atualizar")
                        print("3 .Apagar (Administrador)")
                        print("4 .Consultar")
                        print("5 .Voltar ao 'Menu Cadastros'")
                        
                        opcao = input("\nSelecione uma opção: ")
                        if opcao == '1':
                            nomepet = input("Digite o nome do pet: ")
                            datanascimento= input("Digite a data de nascimento:")
                            celular = input("Digite um telefeno/celular do Tutor:")
                            pets.append([nomepet,datanascimento,celular])
                            print("Pet Cadastrado!")

                        elif opcao == '4':
                            print(pets)

                        elif opcao == "5":
                            break
                
            elif opcao == '4':
                    print("\nServiços (Administrador)\n")
                    print("1.Cadastrar novo Serviço (Administradores)")
                    print("2.Atualizar")
                    print("3.Apagar (Administrador)")
                    print("4.Consultar")
                    print("5.Voltar ao 'Menu Cadastros'")
                
            elif opcao == '5':
                break
            
    elif opcao == '2':
        while True:
            print("\nAtendimentos\n")
            print("1.Iniciar")
            print("2.Agendar")#Aula passada o senhor falou que nao iria cobrar agendamento
            print("3.Remarcar")
            print("4.Voltar ao menu principal")

            opcao = input("\nSelecione uma opção:")
        
            if opcao == '1':
                find = input("Digite o nome do cliente que deseja marcar: ")
                usuario_encontrado = False
                
                if len(usuariosC) == 0:
                    print('Não há usuários cadastrados.\nCadastre um usuário')
                    login = True
                    break
                        
                for i in range(len(usuariosC)):
                    if nomeUsuario == usuariosC[i][0]:
                        print("Usuario Autenticado!\n")         
           
                consulta = input("Qual o motivo para o atendimento do pet? exe: banho,vacina...:")
                comportamento = input("Comportamento do pet:")
                cuidados = input("Algum cuidado especial? alergico...:")
                atendimento.append([consulta, comportamento, cuidados, usuariosC,usuariosD])
                print("\nFinalizado com sucesso!!\n")

                print("Deseja mudar algo? por favor, se direcione ao 'Consultas e relatorios 2")
                
            elif opcao == '2':
                    find = input("Digite o nome do cliente que deseja marcar: ")
                    usuario_encontrado = False
                
                    if len(usuariosC) == 0:
                        print('Não há usuários cadastrados.\nCadastre um usuário')
                        login = True
                        break
                        
                    for i in range(len(usuariosC)):
                        if nomeUsuario == usuariosC[i][0]:
                            print("Usuario Autenticado!\n") 
                             
                    data = input("Digite a data desejada:")
                    usuariosD.append([data])
                    print("Consulta marcada!")

            elif opcao == '3':
                atualizar = input("Digite a data que deseja remarcar: ")
                data_encontrado = False
                                
                if len(usuariosD) == 0:
                    print('Data não esta cadastrada.\nCadastre uma data')
                    login = True
                    break
                        
                for i in range(len(usuariosD)):
                    if nomeUsuario == usuariosD[i][0]:
                        print("Data confirmada!\n") 
                
                usuario_encontrado = True
                                
                # Solicita novos dados ao usuário
                novo_data = input(f"Digite a nova data (ou pressione Enter para manter '{usuario[1]}'): ")
                                
                # Atualiza os dados conforme necessário
                if novo_data:
                    usuario[0] = novo_data
                                    
                usuariosD.append([data,'D'])
                print(f"Data '{atualizar}' atualizada com sucesso!")
                break    
                    
            elif opcao == '4':
                 break 

    elif opcao == '3':
        while True:
            print("\nConsultas/Relatorios\n")
            print("1.Consultas")
            print("2.Relatorios")
            print("3.Voltar ao menu principal")

            opcao = input("\nSelecione uma opção:")
    
            if opcao == '1':
                print(usuariosD)
                
            elif opcao =='2':
                print(atendimento)
            
            if opcao == '3':
                 break

    elif opcao == '4':
        break

    else:
        print("\nOpção invalida!! Selecione novamente\n")

       


