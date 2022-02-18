'''
segrega_par_impar(V)
	A = A[tamanho(V)]
	j = 0
	k = tamanho(A) - 1
	para i de 0 ate tamanho(V) - 1
		se V[i] % 2 não é 0 # Par
        	A[j] = V[i]
			j = j + 1
		senao
			A[k] = V[i]
			k = k - 1
	retorna A, k + 1
'''
def segrega_par_impar(V):
    tamanho = len(V)
    A = [None]*tamanho
    j = 0
    k = tamanho - 1
    for i in range(0, tamanho):
        if V[i] % 2 == 0:
            A[j] = V[i]
            j = j + 1
        else:
            A[k] = V[i]
            k = k - 1

    return A, k + 1

# python segrega_par_impar.py
if __name__ == "__main__":
    print(segrega_par_impar([2,4,3,1,9]))
    print(segrega_par_impar([0,0,0,0]))

# pytest segrega_par_impar.py --hypothesis-show-statistics
from hypothesis import given, settings, event, strategies as st

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, unique=False))
@settings(max_examples=100)
def test_search(xs):
    L, q = segrega_par_impar(xs)
    event(f'{xs}, {L}, {q}')
    if q == len(xs):
        assert(L[0] % 2 == 0)
        assert(L[q-1] % 2 == 0)
    else:
        assert(L[q] % 2 != 0 )