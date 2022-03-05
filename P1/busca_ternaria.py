def busca(inicio, fim, elemento, A):

    if (fim >= inicio):
        terco1 = inicio + (fim - inicio) // 3
        terco2 = fim - (fim - inicio) // 3

        if (A[terco1] == elemento):
            return terco1

        if (A[terco2] == elemento):
            return terco2

        if (elemento < A[terco1]):
            return busca(inicio, terco1 - 1, elemento, A)
        elif (elemento > A[terco2]):
            return busca(terco2 + 1, fim, elemento, A)
        else:
            return busca(terco1 + 1, terco2 - 1, elemento, A)

    return -1

if __name__ == "__main__":
    # Driver code
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = len(A)
    elemento = 5
    print(busca(0, n - 1, elemento, A)) # 4
    elemento = 1
    print(busca(0, n - 1, elemento, A)) # 0
    elemento = 10
    print(busca(0, n - 1, elemento, A)) # 9