'''
majoritario(V)
    n = tamanho(V)
    m = piso(n/2)+1
    E = dicionario(V[0]:1)
    para i = 1 ate tamanho(A)
        tente
            E[V[i]] = E[V[i]] + 1
        senao
            E[V[i]] = 1
    
    para chave, valor em E
        se valor >= m
            retorna k

    retorna None
'''
import logging

LOGGER = logging.getLogger(__name__)

def majoritario(V):
    n = len(V)
    m = (n // 2) + 1
    E = {V[0]:1}
    for i in range(1, n):
        try:
            E[V[i]] = E[V[i]] + 1
        except KeyError:
            E[V[i]] = 1

    return next((k for k, v in E.items() if v >= m), -1)

# python majoritario.py
if __name__ == "__main__":
    # # Case 1
    V=[2,2,3,2,9,2]
    print(majoritario(V))
    print(max(set(V), key=V.count))
    # # # python: 
    # # # set(V)={9, 2, 3}
    # # # V.count funcao que conta item na lista
    # # # max - maior elemento da lista de count
    #print(V.count(2)) # python count ocurrences

    # # Case 2
    V=[0, 1]
    print(majoritario(V))
    print(max(set(V), key=V.count))
    #print(V.count(-1))

    # # Case 3
    V=[3, 3, 3, 3, 3, 3]
    print(majoritario(V))
    print(max(set(V), key=V.count))
    #print(V.count(3))

    # # Case 4
    V=[1, 1, 4, 1, 1, 4, 1, 1, 4, 1, 1, 4, 1, 1, 4]
    print(majoritario(V))
    print(max(set(V), key=V.count))
    #print(V.count(1))

    # Case 5
    V=[3, 3, 0, 3, 3, 0, 3, 3, 0, 3, 3, 0, 3, 3, 0]
    print(majoritario(V))
    print(max(set(V), key=V.count))

# python -m pytest majoritario.py
import random
import time

def test_majoritario():
    for _ in range(10):
        V=5*[random.randrange(0,5),random.randrange(0,5),random.randrange(0,5)]
        # funcao
        inicio = time.time()
        e = majoritario(V)
        duracao = time.time() - inicio
        # fim funcao
        ne = V.count(e)
        m = (len(V) // 2) + 1 # metade + 1
        te = max(set(V), key=V.count)
        LOGGER.warning(f'{V}, {e}, {te}, {ne}, {m}, {duracao}')
        if e >= 0:
            assert(e == te) # confere que eh majoritario