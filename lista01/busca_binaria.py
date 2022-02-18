'''
Busca binária iterativa
Exercício: Lista 1.1

Requerido: python 3+, pip install -r requirements.txt
Executar: python busca_binaria.py
'''

from numpy import integer
#import logging

#LOGGER = logging.getLogger(__name__)

def busca_binaria(lista, valor):
    '''
    Dada uma lista de números e um número, retorna o índice do número na lista
    ou -1 se o número não estiver na lista.

      :param lista: a lista que você deseja pesquisar
      :param valor: o valor que está procurando

      Issue:
      Return rightmost, not leftmost
      https://en.wikipedia.org/wiki/Binary_search_algorithm#Duplicate_elements

    Run: pytest busca_binaria.py --hypothesis-show-statistics
    '''
    tamanho = len(lista)
    fim = tamanho - 1
    inicio = 0
    #chute = tamanho // 2
    #print(chute)
    #print((inicio + fim) // 2)
    #while (fim - inicio) >= 0:
    while fim >= inicio:
        chute = (inicio + fim) // 2
        if valor == lista[chute]:
            return chute
        if valor > lista[chute]:
            inicio = chute + 1
        else:
            fim = chute - 1
        #chute = (inicio + fim) // 2
    return -1

if __name__ == "__main__":
    assert(busca_binaria([1, 2, 3, 4, 5, 6], 4) == 3)
    assert(busca_binaria([1, 2, 3, 4, 5, 6], 1) == 0)
    assert(busca_binaria([1, 2, 3, 4, 5, 6], 6) == 5)
    assert(busca_binaria([23, 32, 44, 45, 45, 60], 44) == 2)
    assert(busca_binaria([23, 32, 44, 45, 45, 60], 45) == 3)
    assert(busca_binaria([23, 32, 44, 45, 45, 60], 100) == -1)
    assert(busca_binaria([23, 32, 44, 45, 45, 60], 23) == 0)
    assert(busca_binaria([23, 32, 44, 45, 45, 60], 60) == 5)
    assert(busca_binaria([23, 32, 44, 45, 45, 60], 32) == 1)
    assert(busca_binaria([0, 0], 0) == 0)

# https://learning.oreilly.com/library/view/robust-python/9781098100650/ch23.html
from hypothesis import given, event, strategies as st
import random

@given(st.lists(st.integers(min_value=0, max_value=1000), min_size=1, unique=True).map(sorted))
def test_search(xs):
    #test_list = [23, 32, 44, 45, 45, 60]
    element_to_search = random.choice(xs)
    #LOGGER.warning(f'{xs}, {element_to_search}')
    event(f'{xs}, {element_to_search}')
    assert(busca_binaria(xs, element_to_search) == xs.index(element_to_search))
