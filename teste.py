from main import menu_principal # Importa a função menu_principal do arquivo main.py

# Lista de alunos para teste
alunos_teste = [
    {'nome': 'Alice', 'nota': 9.5, 'disciplina': 'Matemática'},
    {'nome': 'Bob', 'nota': 7.0, 'disciplina': 'História'},
    {'nome': 'Charlie', 'nota': 8.0, 'disciplina': 'Português'},
    {'nome': 'Diana', 'nota': 6.5, 'disciplina': 'Física'},
    {'nome': 'Eve', 'nota': 9.0, 'disciplina': 'Química'},
    {'nome': 'Frank', 'nota': 5.5, 'disciplina': 'Biologia'},
    {'nome': 'Grace', 'nota': 8.5, 'disciplina': 'Geografia'},
    {'nome': 'Hank', 'nota': 7.5, 'disciplina': 'Educação Física'},
    {'nome': 'Ivy', 'nota': 6.0, 'disciplina': 'Artes'},
    {'nome': 'Jack', 'nota': 9.2, 'disciplina': 'Informática'}
]

# Substitui a lista 'alunos' do main.py pela criada aqui
import main # Importa o módulo main para acessar a lista de alunos
main.alunos.extend(alunos_teste) # Adiciona os alunos de teste à lista existente no main.py

# Roda o menu como se fosse o programa principal
print("Teste do sistema de gerenciamento de alunos\n")
menu_principal()
