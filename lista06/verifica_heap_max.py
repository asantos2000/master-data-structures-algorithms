def verifica_heap_max(A: list) -> bool:
    """
    Verifica se o array A é um heap max.
    """
    for i in range(len(A), 2, -1):
        pai = (i-1) // 2
        print(len(A), i, i-1, pai)
        if A[i-1] < A[pai]:
            return False
    return True

def verifica_heap_max_2(A: list) -> bool:
    """
    Verifica se o array A é um heap max.
    """
    max_pais = len(A) // 2
    for i in range(1, max_pais + 1):
        pai = i
        filho_esq = 2 * i
        filho_dir = 2 * i + 1
        if A[filho_esq] < A[pai]:
            return False
        if (filho_dir) < len(A) and A[filho_dir] < A[i]:
            return False
    return True

if __name__ == '__main__':
    A = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(verifica_heap_max(A))
    #print(verifica_heap_max_2(A))

    A = [None, 9, 4, 5, 1, 3, 2]
    #print(verifica_heap_max(A))
    #print(verifica_heap_max_2(A))