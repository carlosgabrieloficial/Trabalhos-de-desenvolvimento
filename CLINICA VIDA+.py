

escolha = 0
while escolha != 5:

    print("""
    [1] Cadastrar Paciente
    [2] Ver estatísticas
    [3] Buscar pacientes
    [4] Listar todos os pacientes     
    [5] Sair do sistema              
""")
   
    escolha = int(input("Por Favor, escolha uma das opção : "))
   
    if escolha == 1   :
        print("Opção [1] Cadastrar Paciente ")

    elif escolha == 2 :
        print("Opção [2] Ver estatísticas ")
    
    elif escolha == 3 :
        print("Opção [3] Buscar pacientes")
    
    elif escolha == 4 :
        print("Opção [4] Listar todos os pacientes")

    elif escolha == 5 :
        print('=== SAINDO DO SISTEMA')

    else:
        print("Opção invalida \nTente novamente :")