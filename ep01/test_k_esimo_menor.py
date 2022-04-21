import time
import random
from hypothesis import given, event, settings, strategies as st
from k_esimo_menor import k_esimo_menor
from find_small import find_small

micro_seconds = 1000000  # microsecond
#
# Teste da função
#


@settings(max_examples=1000)
@given(st.lists(st.integers(min_value=0, max_value=1000), min_size=50, unique=True).map(sorted),
       st.lists(st.integers(min_value=0, max_value=1000), min_size=50, unique=True).map(sorted))
def test_k_esimo_menor(X, Y):
    lx = 0
    rx = len(X)-1
    ly = 0
    ry = len(Y)-1
    tamanho = rx + ry + 1
    k = random.randrange(1, tamanho + 1)
    inicio = time.time()
    kv = k_esimo_menor(X, Y, lx, rx, ly, ry, k)
    duracao = round((time.time() - inicio) * micro_seconds, 2)
    #X, Y, k, kv, tamanho, duracao
    row = f'{X}; {Y}; {k}; {kv}; {tamanho}; {duracao}'
    # event(row)
    # print(row) # Descomentar para pytest -s > result.txt
    assert(kv == find_small(X + Y, k))

#
# Gera log para planilha
#


def test_double_k_esimo_menor():
    lx = 0
    ly = 0
    for _ in range(1, 10):
        i = 8
        while i <= 8192:
            X = random.sample(range(10000), i)
            Y = random.sample(range(10000), i)
            rx = len(X)-1
            ry = len(Y)-1
            tamanho = rx + ry + 1
            k = random.randrange(1, tamanho + 1)
            # funcao
            inicio = time.time()
            kv = k_esimo_menor(sorted(X), sorted(Y), lx, rx, ly, ry, k)
            duracao = (time.time() - inicio) * micro_seconds
            # fim funcao
            # Descomentar para pytest -s > result2.txt
            print(f'{i}; {duracao}')
            f = find_small(X + Y, k)
            assert(kv == f)
            i *= 2
