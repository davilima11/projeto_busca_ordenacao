# busca.py
def busca_binaria_nome(lista_alunos, nome):
    """
    Busca binária por nome do aluno.
    A lista deve estar ordenada por nome.
    Retorna o dicionário do aluno ou None se não encontrado.
    """
    inicio = 0  # Índice inicial da busca
    fim = len(lista_alunos) - 1  # Índice final da busca

    while inicio <= fim:  # Enquanto houver elementos para buscar
        meio = (inicio + fim) // 2  # Calcula o índice do meio
        if lista_alunos[meio]['nome'] == nome:  # Se encontrou o nome
            return lista_alunos[meio]  # Retorna o aluno encontrado
        elif lista_alunos[meio]['nome'] < nome:  # Se o nome do meio é menor que o buscado
            inicio = meio + 1  # Busca na metade direita
        else:
            fim = meio - 1  # Busca na metade esquerda
    return None  # Retorna None se não encontrou


def busca_binaria_nota(lista_alunos, nota):
    """
    Busca binária por nota específica.
    A lista deve estar ordenada por nota.
    Retorna uma lista de alunos com essa nota (caso haja repetição).
    """
    inicio = 0  # Índice inicial da busca
    fim = len(lista_alunos) - 1  # Índice final da busca
    resultados = []  # Lista para armazenar alunos encontrados

    while inicio <= fim:  # Enquanto houver elementos para buscar
        meio = (inicio + fim) // 2  # Calcula o índice do meio
        if lista_alunos[meio]['nota'] == nota:  # Se encontrou a nota
            resultados.append(lista_alunos[meio])  # Adiciona o aluno encontrado
            # Verificar duplicados para frente e para trás
            i = meio - 1  # Verifica para trás
            while i >= inicio and lista_alunos[i]['nota'] == nota:
                resultados.append(lista_alunos[i])  # Adiciona duplicados anteriores
                i -= 1
            i = meio + 1  # Verifica para frente
            while i <= fim and lista_alunos[i]['nota'] == nota:
                resultados.append(lista_alunos[i])  # Adiciona duplicados posteriores
                i += 1
            break  # Sai do loop após encontrar todos os duplicados
        elif lista_alunos[meio]['nota'] < nota:  # Se a nota do meio é menor que a buscada
            inicio = meio + 1  # Busca na metade direita
        else:
            fim = meio - 1  # Busca na metade esquerda

    return resultados  # Retorna a lista de alunos encontrados
