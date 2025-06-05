#Ordena uma lista de dicionários pela chave especificada para a pessoa escolher entre ordenar por nota ou por nome.
def merge_sort(lista, chave):
    # Se a lista tiver mais de um item, bora dividir pra conquistar
    if len(lista) > 1:
        meio = len(lista) // 2  # Pega o meio da lista
        esquerda = lista[:meio]  # Pega a parte da esquerda
        direita = lista[meio:]   # Pega a parte da direita

        # Chama o merge_sort de novo pra cada metade
        merge_sort(esquerda, chave)
        merge_sort(direita, chave)

        i = j = k = 0  # Índices pra controlar onde tá em cada lista

        # Agora junta tudo de novo, mas já deixando em ordem
        while i < len(esquerda) and j < len(direita):
            if esquerda[i][chave] <= direita[j][chave]:
                lista[k] = esquerda[i]  # Coloca o menor na lista principal
                i += 1  # Vai pro próximo da esquerda
            else:
                lista[k] = direita[j]  # Coloca o menor da direita
                j += 1  # Vai pro próximo da direita
            k += 1  # Vai pro próximo da lista principal

        # Enquanto ainda houver elementos não inseridos da metade esquerda
        while i < len(esquerda):
            lista[k] = esquerda[i]  # Coloca o elemento da esquerda na posição correta da lista principal
            i += 1  # Avança para o próximo elemento da esquerda
            k += 1  # Avança para a próxima posição da lista principal

        # Enquanto ainda houver elementos não inseridos da metade direita
        while j < len(direita):
            lista[k] = direita[j]  # Coloca o elemento da direita na posição correta da lista principal
            j += 1  # Avança para o próximo elemento da direita
            k += 1  # Avança para a próxima posição da lista principal
