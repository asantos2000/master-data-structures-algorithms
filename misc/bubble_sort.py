def bubbleSort(A):
    trocado = True
    while trocado:
        trocado = False
        for j in range(1, len(A)):
            if A[j-1] > A[j]:
                trocado = True
                A[j-1], A[j] = A[j], A[j-1]

def bubbleSort2(A):
    tamanho = len(A) - 1
    while tamanho > 0:
        for j in range(0, tamanho):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
        tamanho = tamanho - 1

if __name__ == '__main__':
    A = [3, 2, 1, 5, 4]
    bubbleSort(A)
    print(A)

    A = [1, 2, 3, 4, 5]
    bubbleSort(A)
    print(A)

    A = [5, 4, 3, 2, 1]
    bubbleSort(A)
    print(A)

    A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    bubbleSort(A)
    print(A)

    A = [10, 9, 8, 8, 6]
    bubbleSort(A)
    print(A)

    A = [3, 2, 1, 5, 4]
    bubbleSort2(A)
    print(A)

    A = [1, 2, 3, 4, 5]
    bubbleSort2(A)
    print(A)

    A = [5, 4, 3, 2, 1]
    bubbleSort2(A)
    print(A)

    A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    bubbleSort2(A)
    print(A)

    A = [10, 9, 8, 8, 6]
    bubbleSort2(A)
    print(A)