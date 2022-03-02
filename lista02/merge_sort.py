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

def merge_sort(A):
    tamanho = len(A)
    meio = tamanho // 2
    if tamanho <= 1:
        return A
    B = merge_sort(A[:meio])
    C = merge_sort(A[meio:])
    return intercala(B,C)

if __name__ == "__main__":
    print(merge_sort([4,3,7,2,1]))
    print(merge_sort([6, 7, 8, 3, 4, 5, 1, 2, 3]))
    print(intercala([3,4],[1,2,7]))
    print(intercala([3,4,5],[1,2]))
    print(intercala([3],[1,2]))
    print(intercala([3,4],[1]))
    print(intercala([3],[1]))

from hypothesis import given, event, settings, strategies as st
import time

@settings(max_examples=100)
@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, unique=False))
def test_merge_sort(A):
    inicio = time.time()
    S = merge_sort(A)
    duracao = time.time() - inicio
    PS = sorted(A)
    T = len(A)
    event(f'{A}, {S}, {PS}, {T}, {duracao}')
    assert(S == PS)
