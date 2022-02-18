'''
majoritario(V):
    E = merge_sort(V)
    conte = 0
    metade = V.tamanho div 2
    item_anterior = E[0]
    para item em E
        se item == item_anterior
            conte 1
            se conte > metade
                retorna item
        senao
            conte 0
            item_anterior = item
    retorna -1
'''
import logging
from merge_sort import merge_sort

LOGGER = logging.getLogger(__name__)

def majoritario(V):
    E = merge_sort(V)
    conte = 0
    m = len(V) // 2
    ea = E[0]
    for e in E:
        if e == ea:
            conte += 1
            if conte > m:
                return e
        else:
            conte = 0
            ea = e
    return -1

# python majoritario_2.py
if __name__ == "__main__":
    # Case 1
    V=[2,2,3,2,9,2]
    print(majoritario(V))
    print(max(set(V), key=V.count))
    # # python: 
    # # set(V)={9, 2, 3}
    # # V.count funcao que conta item na lista
    # # max - maior elemento da lista de count
    #print(V.count(2)) # python count ocurrences

    # Case 2
    V=[0, 1]
    print(majoritario(V))
    print(max(set(V), key=V.count))
    #print(V.count(-1))

    # Case 3
    V=[3, 3, 3, 3, 3, 3]
    print(majoritario(V))
    print(max(set(V), key=V.count))
    #print(V.count(3))

    # Case 4
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
    for i in range(0,10):
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

# @given(st.lists(st.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), min_size=3))
# def test_elections_are_transitive(X):
#     flat_list = [item for sublist in X for item in sublist]
#     event(f'{flat_list}')