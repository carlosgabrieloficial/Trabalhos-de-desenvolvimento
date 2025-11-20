banco_de_dados = []

def cadastro_paciente():
    paciente = {}

    paciente["Nome"]=str(input("Nome :")).upper().strip()

    while True:

        try:
            
            idade = int(input("Idade :"))
            if idade <= 0:
                
                print("Por favor,insira uma idade valida (maior que 0)")
                continue

            paciente["Idade"] = idade
            break

        except ValueError:
            print("Idade invalida.Por favor,insira um número inteiro")

    while True :

        telefone = str(input("Telefone: ")).strip()

        if telefone.isdigit() and len(telefone) >= 10:
            
            paciente["Telefone"] = telefone
            break
        
        else:
            print("Numero de telefone inválido. Por favor, insira um numero válido de no mínimo 10 digitos")

    banco_de_dados.append(paciente)
    print("Paciente cadastrado com sucesso")
    return paciente

def exibir_estatisticas() : 
    
    
    if not banco_de_dados:
        print("Nenhum paciente cadastrado\nTente novamente")
        return
    
    total_pacientes_cadastrados = len(banco_de_dados)

    soma_idades_pacientes = sum(paciente["Idade"] for paciente in banco_de_dados)

    media_idade_pacientes = soma_idades_pacientes/total_pacientes_cadastrados

    paciente_mais_novo = min(banco_de_dados, key=lambda pessoa:pessoa["Idade"])

    paciente_mais_velho = max(banco_de_dados, key=lambda pessoa:pessoa["Idade"])

    print(f"O total de pacientes cadastrados foi : {total_pacientes_cadastrados}")

    print(f"A idade média dos pacientes foi de  : {media_idade_pacientes:.2f}")

    print(f"O paciente mais novo cadastrado é : {paciente_mais_novo["Nome"]} com {paciente_mais_novo["Idade"]} anos.")

    print(f"O paciente mais velho cadastrado é : {paciente_mais_velho["Nome"]} com {paciente_mais_velho["Idade"]} anos.")

def buscar_paciente():

    paciente_nome = (input("Nome do paciente que deseja pesquisar : ")).upper().strip()

    for pessoa in banco_de_dados:
        
        if pessoa["Nome"].upper() == paciente_nome.upper():
            print(f"=== PACIENTE ENCONTRADO ===")
            print(f"Nome : {pessoa["Nome"]}")
            print(f"Idade : {pessoa["Idade"]}")
            print(f"Telefone : {pessoa["Telefone"]}")
            return
    print("=== Paciente não encontrado ===")

def exibir_lista_pacientes():

    if not banco_de_dados:
        print("Nenhum paciente cadastrado\nTente novamente")
        return

    for paciente in banco_de_dados:
        print(f"Nome :{paciente["Nome"]}")
        print(f"Idade :{paciente["Idade"]}")
        print(f"Telefone :{paciente["Telefone"]}")
        print("="*30)
        

def menu():
    print("=== SISTEMA CLÍNICA VIDA + ===")
    print("[1] CADASTRAR PACIENTE")
    print("[2] VER ESTATÍSTICAS")
    print("[3] BUSCAR PACIENTE")
    print("[4] LISTAR PACIENTES")
    print("[5] SAIR")
    print("="*30)


while True:
    
    menu()

    escolha = input("Escolha uma opção entre [1-5] :\n")
                
    if escolha == "1" :
            cadastro_paciente()

    elif escolha == "2" :
            exibir_estatisticas()

    elif escolha == "3" :
            buscar_paciente()

    elif escolha == "4" : 
            exibir_lista_pacientes()

    elif escolha == "5" : 
            print("=== FIM DO PROGRAMA ===")
            break

    else:
            print("Escolha incorreta, tente novamente escolha entre [1-5]")
        
