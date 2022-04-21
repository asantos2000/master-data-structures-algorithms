'''
Busca maior valor por divisão e conquista
Exercício: Lista 1.2

Requerido: python 3+, pip install -r requirements.txt
Executar: python maior_valor.py
'''

def maior_valor(A):
    '''
    Retorna o maior valor em uma lista
    
    :param A: A lista para procura
    :return: O maior valor na lista.
    '''
    # Base
    if len(A) == 1:
        return A[0]

    if len(A) == 2:
        return A[0] if A[0] > A[1] else A[1]

    meio = len(A) // 2
    a = maior_valor(A[:meio])
    b = maior_valor(A[meio:])

    return a if a > b else b


def rand_list(num_elements, min, max):
    '''
    Gera uma lista randomica de inteiros
    
    :param num_elements: Tamanho da lista
    :param min: Valor do menor elemento randomico
    :param max: Valor do máximo elemento randomico
    :return: Lista de inteiros.
    '''
    import random
    randomlist = []
    for _ in range(num_elements):
        n = random.randint(min, max)
        randomlist.append(n)
    return randomlist


if __name__ == "__main__":
    # Test
    assert(maior_valor([1, 2, 3, 4, 5, 6]) == 6)
    assert(maior_valor([1, 2, 3, 4, 5, 6, 7]) == 7)
    assert(maior_valor([1, 2, 3, 4, 5, 6, 7, 8]) == 8)
    assert(maior_valor([10, 20, 30, 40, 50, 60, 70, 80, 90]) == 90)
    assert(maior_valor([10, 5, 64, 40, 23, 12, 5, 99, 11]) == 99)
    assert(maior_valor([10, 5, 64, 64, 23, 12, 5, 99, 11]) == 99)
    assert(maior_valor([99, 5, 64, 64, 23, 12, 5, 99, 11]) == 99)

    # Random test
    for _ in range(20):
        L = rand_list(5, 0, 100)
        print(L, maior_valor(L))
