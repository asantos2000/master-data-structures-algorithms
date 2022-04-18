import sys
sys.path.append('../trees')
sys.path.append('trees')
from trees import Node

def maior_chave_abb(A: Node):
    if A is None:
        return -1
    filho_direito = A.right
    maior = A.key
    while filho_direito is not None:
        maior = filho_direito.key
        filho_direito = filho_direito.right
	
    return maior

def menor_chave_abb(A: Node):
    if A is None or A.left is None:
        return A.key
    return menor_chave_abb(A.left)

if __name__ == '__main__':
    # True
    tree = Node(35)
    tree.left = Node(14)
    tree.right = Node(80)
    tree.left.left = Node(12)
    tree.left.right = Node(22)
    #print(maior_chave_abb(tree))
    print(menor_chave_abb(tree))

    # Limitação, o algoritmo não verifica se é uma ABB e retorna o valor do maior nó.
    tree = Node(35)
    tree.left = Node(14)
    tree.right = Node(80)
    tree.left.left = Node(15)
    tree.left.right = Node(22)
    #print(maior_chave_abb(tree))
    #print(menor_chave_abb(tree))

    # Somente root
    tree = Node(35)
    #print(maior_chave_abb(tree))
    #print(menor_chave_abb(tree))

    # Arvore nula
    tree = None
    #print(maior_chave_abb(tree))
    #print(menor_chave_abb(tree))