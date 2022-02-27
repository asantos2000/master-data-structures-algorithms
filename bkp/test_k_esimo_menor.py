from k_esimo_menor import k_esimo_menor
from find_small import find_small
micro_seconds = 1000000 # microsecond
#
# Teste da função
#
from hypothesis import given, event, settings, strategies as st
import random
import time

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
    row = f'{X}; {Y}; {k}; {kv}; {tamanho}; {duracao}'
    #event(row)
    #X, Y, k, kv, tamanho, duracao
    print(row)
    assert(kv == find_small(X + Y, k))

#
# Gera log para planilha
#
import logging

LOGGER = logging.getLogger(__name__)

def test_double_k_esimo_menor():
    for j in range(1,2):
        i = 8
        while i <= 4096:
            X = random.sample(range(0, 10000), i)
            Y = random.sample(range(0, 10000), i)
            lx = 0
            rx = len(X)-1
            ly = 0
            ry = len(Y)-1
            tamanho = rx + ry + 1
            k = 1 #random.randrange(1, tamanho + 1)
            # funcao
            inicio = time.time()
            kv = k_esimo_menor(sorted(X), sorted(Y), lx, rx, ly, ry, k)
            duracao = (time.time() - inicio) * micro_seconds
            # fim funcao
            #LOGGER.warning(f'{i}, {len(X)}, {len(Y)}, {duracao}')
            print(f'{i}; {duracao}')
            f = find_small(X + Y, k)
            assert(kv == f)
            i = i*2
