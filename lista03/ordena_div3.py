'''
Ordena dividindo o vetor em 3 partes
'''
import math

def intercala(B,C):
    H = []
    i, j = 0, 0
    tamanho_B = len(B)
    tamanho_C = len(C)
    while (i < tamanho_B) and (j < tamanho_C):
        if B[i] < C[j]:
            #B.pop(i)
            H.append(B[i])
            i += 1
        else:
            #C.pop(j)
            H.append(C[j])
            j += 1
    
    #if i < tamanho_B:
    while (i < tamanho_B):
        H.append(B[i])
        i += 1
    #else:
    while (j < tamanho_C):
        H.append(C[j])
        j += 1

    return H

def ordena(A):
    tamanho = len(A)
    if tamanho <= 1:
        return A
    terco = math.ceil(tamanho / 3)
    A1 = ordena(A[:terco])
    A2 = ordena(A[terco: 2*terco])
    A3 = ordena(A[2*terco:])
    return intercala(intercala(A1, A2), A3)

if __name__ == "__main__":
    # Case 1 - intercala
    A = [1,2,3]
    B = [3,4,5]
    C = [6,7,8]
    print(intercala(intercala(A, B),C))
    # Case 2 - intercala
    A = [6,7,8]
    B = [3,4,5]
    C = [1,2,3]
    print(intercala(intercala(A, B),C))
    # Case 3 - intercala
    A = [6,7,8]
    B = [3,4,5]
    C = [1,2]
    print(intercala(intercala(A, B),C))
    # Case 4 - ordena
    A = [6, 7, 8, 3, 4, 5, 1, 2, 3]
    print(ordena(A))
    # Case 5 - ordena
    A = [8, 3]
    print(ordena(A))
    # Case 6 - ordena
    A = [6, 7, 8, 3, 4, 5, 1, 2]
    print(ordena(A))
