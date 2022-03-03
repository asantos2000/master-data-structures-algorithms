def busca_ternaria(lista, elemento):
    """
    Função que busca um elemento em uma lista e retorna o índice
    :param lista: Lista que será buscado o elemento
    :param elemento: Elemento que será buscado
    :return: Índice do elemento
    """
    inicio = 0
    fim = len(lista) - 1
    meio = (inicio + fim) // 2
    while inicio <= fim:
        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1
        meio = (inicio + fim) // 2
    return -1

def busca_ternaria_recursiva(lista, elemento, inicio, fim):
    """
    Função que busca um elemento em uma lista e retorna o índice
    :param lista: Lista que será buscado o elemento
    :param elemento: Elemento que será buscado
    :param inicio: Índice inicial da busca
    :param fim: Índice final da busca
    :return: Índice do elemento
    """
    if inicio > fim:
        return -1
    meio = (inicio + fim) // 2
    if lista[meio] == elemento:
        return meio
    elif lista[meio] < elemento:
        return busca_ternaria_recursiva(lista, elemento, meio + 1, fim)
    else:
        return busca_ternaria_recursiva(lista, elemento, inicio, meio - 1)