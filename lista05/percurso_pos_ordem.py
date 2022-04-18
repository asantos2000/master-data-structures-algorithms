"""
Função que percorre a árvore em ordem usando pilha explícita.
"""
import sys
sys.path.append('../trees')
sys.path.append('trees')
from trees import Node

def percurso_pos_ordem(A: Node):
    pilha = [A]
    while len(pilha) > 0:
        A = pilha.pop()
        print(A.key)
        if A.right is not None:
            pilha.append(A.right)
        if A.left is not None:
            pilha.append(A.left)

if __name__ == '__main__':
    A = Node(50)
    A.left = Node(40)
    A.right = Node(60)
    A.left.left = Node(35)
    A.left.right = Node(45)
    A.right.left = Node(55)
    A.right.right = Node(65)
    percurso_pos_ordem(A)