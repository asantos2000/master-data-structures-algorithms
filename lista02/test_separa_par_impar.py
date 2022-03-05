from hypothesis import given, event, settings, strategies as st
import time
from separa_par_impar import separa_par_impar

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