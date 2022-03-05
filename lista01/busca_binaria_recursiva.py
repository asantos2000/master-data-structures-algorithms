def pesquisa_binaria_recursiva(A, esquerda, direita, item):
    """Implementa pesquisa binária recursivamente."""
    # 1. Caso base: o elemento não está presente. 
    if direita < esquerda:
        return -1
    meio = (esquerda + direita) // 2
    # 2. Nosso palpite estava certo: o elemento está no meio do arranjo. 
    if A[meio] == item:
        return meio
    # 3. O palpite estava errado: atualizamos os limites e continuamos a busca. 
    elif A[meio] > item:
        return pesquisa_binaria_recursiva(A, esquerda, meio - 1, item)
    else: # A[meio] < item
        return pesquisa_binaria_recursiva(A, meio + 1, direita, item)


if __name__ == "__main__":
    A = [1,2,3,4,5,6,7,8,9,10]
    print(pesquisa_binaria_recursiva(A, 0, len(A) - 1, 5))  # 4
    print(pesquisa_binaria_recursiva(A, 0, len(A) - 1, 1))  # 0
    print(pesquisa_binaria_recursiva(A, 0, len(A) - 1, 10)) # 9
    print(pesquisa_binaria_recursiva(A, 0, len(A) - 1, 2))  # 1