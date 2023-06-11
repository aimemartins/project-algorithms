def is_anagram(first_string, second_string):
    # Verificar se as palavras são vazias
    if len(first_string) == 0 or len(second_string) == 0:
        return (
            ordenar_palavra(first_string),
            ordenar_palavra(second_string),
            False,
        )
    # Transformar as palavras em minúsculas
    first_string = first_string.lower()
    second_string = second_string.lower()

    # Verificar se as palavras tem o mesmo tamanho

    if len(first_string) != len(second_string):
        return (
            ordenar_palavra(first_string),
            ordenar_palavra(second_string),
            False,
        )

    # Ordenar as letras das palavras
    first_string = ordenar_palavra(first_string)
    second_string = ordenar_palavra(second_string)

    # Verificar se as palavras ordenadas  são iguais
    for i in range(len(first_string)):
        if first_string[i] != second_string[i]:
            return (
                ordenar_palavra(first_string),
                ordenar_palavra(second_string),
                False,
            )
    return (
        ordenar_palavra(first_string),
        ordenar_palavra(second_string),
        True,
    )


def ordenar_palavra(word):
    lista = list(word)
    # # Usar o algoritmo Quicksort para ordenar a lista
    quicksort(lista, 0, len(lista) - 1)
    # # Transformar a lista em string
    word_ordenada = "".join(lista)
    return word_ordenada


def quicksort(lista, inicio, fim):
    if inicio < fim:
        # # obter o índice da partição
        p = partition(lista, inicio, fim)
        # # classificar os elementos à esquerda da partição
        quicksort(lista, inicio, p - 1)
        # # classificar os elementos à direita da partição
        quicksort(lista, p + 1, fim)


def partition(lista, inicio, fim):
    # # selecionar o elemento do meio como pivô
    meio = (inicio + fim) // 2
    pivo = lista[meio]
    # # mover o pivô para o início da lista
    lista[meio] = lista[inicio]
    lista[inicio] = pivo
    # # estabelecer a fronteira
    fronteira = inicio
    # # reorganizar os elementos
    for i in range(inicio, fim + 1):
        if lista[i] < pivo:
            fronteira += 1
            temp = lista[i]
            lista[i] = lista[fronteira]
            lista[fronteira] = temp
    # # colocar o pivô em sua posição final
    temp = lista[inicio]
    lista[inicio] = lista[fronteira]
    lista[fronteira] = temp
    # # retornar a posição do pivô
    return fronteira


# print(is_anagram("amor", "roma"))
# print(is_anagram("pedra", "perda"))
# print(is_anagram("amor", "amora"))
# print(is_anagram("coxinha", "empada"))
# print(is_anagram("roma", ""))

# raise NotImplementedError
