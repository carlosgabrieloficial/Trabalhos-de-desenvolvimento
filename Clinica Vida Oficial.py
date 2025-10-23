banco_de_dados = []


def cadastro_paciente():
    paciente = {}

    paciente["Nome"] = str(input("Nome : ")).upper().strip()
    paciente["Idade"] = int(input("Idade : "))
    paciente["Telefone"] = str(input("Telefone : "))

    banco_de_dados.append(paciente)
    print("Paciente cadastrado com Sucesso")

def exibir_estatisticas() : 
    
    
    if not banco_de_dados:
        print("Nenhum paciente cadastrado\nTente novamente")
        return
    
    total_pacientes_cadastrados = len(banco_de_dados)

    soma_idades_pacientes = sum(paciente["Idade"] for paciente in banco_de_dados)

    media_idade_pacientes = soma_idades_pacientes/len(banco_de_dados)

    paciente_mais_novo = min(banco_de_dados, key=lambda pessoa:pessoa["Idade"])

    paciente_mais_velho = max(banco_de_dados, key=lambda pessoa:pessoa["Idade"])

    print(f"O total de pacientes cadastrados foi : {total_pacientes_cadastrados}")

    print(f"A média de idade dos pacientes foi de : {media_idade_pacientes}")

    print(f"O paciente mais novo cadastrado é : {paciente_mais_novo}")

    print(f"O paciente mais velhi cadastrado é : {paciente_mais_velho}")

def buscar_paciente():

    paciente = (input("Nome do paciente que deseja pesquisar : "))
    for pessoa in banco_de_dados:
        if pessoa["Nome"].upper() == paciente.upper():
            print(f"Paciente encontrado\n,{pessoa}\n")
            return
    print("Paciente não encontrado")

def exibir_lista_pacientes():
    for paciente in banco_de_dados:
        print(paciente)
        print()


def menu_clinica_vida_():

    print("=== SISTEMA CLÍNICA VIDA + ===\n" \
          
    "[1] CADASDTRAR PACIENTE\n" 
    "[2] VER ESTATÍSTICAS\n" \
    "[3] BUSCAR PACIENTE\n" \
    "[4] LISTAR OS PACIENTES\n" \
    "[5] SAIR")
    print("="*20)


while True : 

    menu_clinica_vida_()
    escolha = int(input("Escolha uma opção entre [1-5] :\n"))
            
    if escolha == 1 :
        cadastro_paciente()

    elif escolha == 2 :
        exibir_estatisticas()

    elif escolha == 3 :
        buscar_paciente()

    elif escolha == 4 : 
        exibir_lista_pacientes()

    elif escolha == 5 : 
        print("=== FIM DO PROGRAMA ===")
        break

    else:
        print("Escolha incorreta, tente novamente escolha entre [1-5]")
        

