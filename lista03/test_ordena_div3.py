from hypothesis import given, event, settings, strategies as st
import time
from ordena_div3 import ordena 

MICRO_SECOND = 1000000
@settings(max_examples=100)
@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, unique=False))
def test_ordena_div3(A):
    inicio = time.time()
    S = ordena(A)
    duracao = time.time() - inicio
    PS = sorted(A)
    T = len(A)
    event(f'{A}, {S}, {PS}, {T}, {duracao*MICRO_SECOND}')
    assert(S == PS)