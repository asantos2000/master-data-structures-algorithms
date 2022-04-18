"""
Função que percorre a árvore em ordem usando pilha explícita.
"""
import sys
sys.path.append('../trees')
sys.path.append('trees')
from avl2 import No

if __name__ == "__main__":
    v = [10, 5, 15, 3, 7, 13, 17, 18, 20, 25, 30]
    avl = No(v.pop())
    for i in v:
        avl.insere(i)
    print("AVL:")
    avl.imprime_arvore()
    print("\nPercurso em in-ordem (vetor ordenado):")
    avl.percurso_in_ordem()
