# main.py

# Importa a função merge_sort do módulo ordenacao
from ordenacao import merge_sort
# Importa as funções de busca binária dos módulos busca
from busca import busca_binaria_nome, busca_binaria_nota

# Lista inicial de alunos (pode ser com dados)
alunos = []

def adicionar_aluno():
    # Solicita ao usuário quantos alunos deseja adicionar
    quantidade = int(input("Quantos alunos você deseja adicionar? "))
    for i in range(quantidade): # Para cada aluno que o usuário deseja adicionar
        print(f"\nCadastro do aluno {i + 1}:") # Exibe o número do aluno que está sendo cadastrado
        # Solicita o nome do aluno, remove espaços e coloca a primeira letra maiúscula
        nome = input("Digite o nome do aluno: ").strip().title()
        # Solicita a disciplina, remove espaços e coloca a primeira letra maiúscula
        disciplina = input("Digite a disciplina: ").strip().title()
        # Solicita a nota do aluno e converte para float
        nota = float(input("Digite a nota do aluno (0.0 a 10.0): ")) 
        # Adiciona o aluno à lista de alunos como um dicionário
        alunos.append({'nome': nome, 'nota': nota, 'disciplina': disciplina}) # Adiciona o aluno como um dicionário com nome, nota e disciplina
        print(f"✅ Aluno {nome} adicionado com sucesso")
    

# Função que exibe os alunos formatados
def exibir_alunos(lista):
    # Verifica se a lista está vazia
    if not lista: # se a lista de alunos estiver vazia exibe mensagem de erro
        print("❌ Nenhum aluno cadastrado.")
        return
    print("\nLista de Alunos:") 
    # Percorre e exibe cada aluno da lista
    for aluno in lista: # para cada aluno na lista de alunos
        print(f"Nome: {aluno['nome']}, Nota: {aluno['nota']}, Disciplina: {aluno['disciplina']}") # Exibe o nome, nota e disciplina do aluno
    print() 


# Função para excluir aluno
def excluir_aluno():
    nome = input("Digite o nome do aluno que deseja excluir: ").strip().title() #Solicita o nome do aluno a ser excluído, remove espaços e coloca a primeira letra maiúscula
    aluno_encontrado = busca_binaria_nome(alunos, nome) # Busca o aluno pelo nome usando busca_binaria_nome

    if aluno_encontrado: # Se o aluno for encontrado
        try: # Tenta remover o aluno da lista
            alunos.remove(aluno_encontrado)  # Remove o aluno da lista
            print(f"✅ Aluno '{nome}' excluído com sucesso!")
        except ValueError: # Se ocorrer um erro ao remover o aluno
            print("❌ Erro ao excluir aluno.") 
    else:# Se o aluno não for encontrado
        print("❌ Aluno não encontrado.")


# Menu para escolher critério de ordenação
def menu_ordenar():
    print("Como deseja ordenar os alunos?")
    print("1. Por nome")
    print("2. Por nota")
    # Solicita ao usuário a opção de ordenação
    opcao = input("Escolha uma opção (1 ou 2): ") # Pede ao usuário escolher entre ordenar por nome ou por nota

    if opcao == '1': # se o usuário escolher ordenar por nome
        merge_sort(alunos, chave='nome') # Ordena a lista de alunos pelo nome usando merge_sort
        print("✅ Lista ordenada por nome.")
    elif opcao == '2': # se o usuário escolher ordenar por nota
        merge_sort(alunos, chave='nota') # Ordena a lista de alunos pela nota usando merge_sort
        print("✅ Lista ordenada por nota.")
    else:
        print("❌ Opção inválida!")

# Menu para escolher tipo de busca
def menu_buscar():
    print("\nComo deseja buscar?")
    print("1. Buscar aluno por nome")
    print("2. Buscar alunos por nota")
    # Solicita ao usuário a opção de busca
    opcao = input("Escolha uma opção (1 ou 2): ") #pede ao usuário escolher entre buscar por nome ou por nota

    if opcao == '1': # se o usuário escolher buscar por nome
        # Solicita o nome do aluno a ser buscado
        nome = input("Digite o nome do aluno: ")
        # Busca o aluno pelo nome usando busca_binaria_nome
        resultado = busca_binaria_nome(alunos, nome) # Chama a função de busca binária para encontrar o aluno com o nome informado
        if resultado: # Se encontrou o aluno, exibe os dados
            print("\n✅ Aluno encontrado:")
            print(resultado) # Exibe o aluno encontrado
        else: # Caso não encontre o aluno com o nome informado
            print("❌ Aluno não encontrado.") 

    elif opcao == '2': # se o usuário escolher buscar por nota
        try:
            # Solicita a nota a ser buscada e converte para float, se falhar, cai no except
            nota = float(input("Digite a nota que deseja buscar: "))
            # Busca alunos pela nota usando busca_binaria_nota
            resultado = busca_binaria_nota(alunos, nota) # Chama a função de busca binária para encontrar alunos com a nota informada
            if resultado: # Se encontrou algum aluno com a nota, exibe a lista
                print(f"\n✅ Alunos encontrados com nota {nota}:")
                exibir_alunos(resultado)
            else:  # Caso nenhum aluno seja encontrado com a nota informada
                print("❌ Nenhum aluno encontrado com essa nota.")
        except ValueError:
            # Caso o valor digitado não seja um número válido
            print("❌ Digite uma nota válida (ex: 8.5).")

    else:
        print("❌ Opção inválida!")


# Menu principal do sistema. Onde o usuário pode escolher as opções disponíveis.
def menu_principal():
    while True:
        print("\n📚 Sistema de Gerenciamento de Notas Escolares")
        print("1. Adicionar alunos")
        print("2. Buscar alunos")
        print("3. Exibir todos os alunos")
        print("4. Ordenar aluno")
        print("5. Excluir aluno")
        print("6. Sair")
        # Solicita ao usuário a opção do menu principal
        opcao = input("Escolha uma opção (1-6): ")

        if opcao == '1':
            # Chama a função para adicionar alunos
            adicionar_aluno()

        elif opcao == '2':
            # Chama a função para buscar alunos
            menu_buscar()

        elif opcao == '3':
            # Exibe todos os alunos cadastrados
            exibir_alunos(alunos)

        elif opcao == '4':
            # Chama o menu de ordenação
            menu_ordenar()

        elif opcao == '5':
            # Chama a função para excluir aluno
            excluir_aluno()

        elif opcao == '6':
            # Sai do sistema
            print("👋 Saindo do sistema. Até mais!")
            break

        else:
            # Caso a opção seja inválida
            print("❌ Opção inválida! Tente novamente.")

menu_principal()  # Chama a função para iniciar o menu principal do sistema

