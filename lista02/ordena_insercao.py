'''
ordenacao_insercao(A)
	para i de 1 até tamanho(A), i++
		eleito = i + 1
		para j de i até 1, j--
			se A[eleito] < A[j]
				troca A[eleito], A[j]
                eleito = j

call: pytest ordena_insercao.py --hypothesis-show-statistics
'''

def ordena_insercao(A):
    print(len(A))
    for i in range(len(A)-1):
        print(i)
        eleito = i + 1
        #print(i, A[eleito])
        for j in range(i, -1, -1):
            #print(A[eleito], A[j])
            if A[eleito] < A[j]:
                #print(A[eleito], A[j])
                A[eleito], A[j] = A[j], A[eleito]
                eleito = j
    return A

from hypothesis import given, settings, event, strategies as st

@given(st.lists(st.integers(min_value=0, max_value=1000), min_size=1, unique=False))
@settings(max_examples=10)
def test_search(xs):
    list_sorted = sorted(xs)
    event(f'{xs}, {list_sorted}')
    assert(ordena_insercao(xs) == list_sorted)

if __name__ == "__main__":
    print(ordena_insercao([2,8,4,3]))