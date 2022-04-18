"""
Função que percorre a árvore em ordem usando pilha explícita.
"""
import sys
sys.path.append('../trees')
sys.path.append('trees')
from trees import Node

def percurso_in_ordem(A: Node):
    pilha = []
    while A is not None or len(pilha) > 0:
        if A is not None:
            pilha.append(A)
            A = A.left
        else:
            A = pilha.pop()
            print(A.key)
            A = A.right

if __name__ == '__main__':
    # Caso 1
    tree = Node(35)
    tree.left = Node(14)
    tree.right = Node(80)
    tree.left.left = Node(12)
    tree.left.right = Node(22)
    percurso_in_ordem(tree)

    print("")

    # Somente root
    tree = Node(35)
    percurso_in_ordem(tree)

    print("")

    # Arvore nula
    tree = None
    percurso_in_ordem(tree)

    print("")

    # Caso 2
    tree = Node(50)
    tree.left = Node(40)
    tree.right = Node(60)
    tree.left.left = Node(35)
    tree.left.right = Node(45)
    tree.right.left = Node(55)
    tree.right.right = Node(65)
    percurso_in_ordem(tree)

    print("")

    # Caso 2
    tree = Node(0) # +
    tree.left = Node(1) # *
    tree.right = Node(2) # -
    tree.left.left = Node(3) # A
    tree.left.right = Node(4) # B
    tree.right.left = Node(5) # C
    tree.right.right = Node(6) # /
    tree.right.right.left = Node(7) # D
    tree.right.right.right = Node(8) # E
    percurso_in_ordem(tree)

    print("")