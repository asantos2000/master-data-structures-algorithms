import sys
sys.path.append('../trees')
sys.path.append('trees')
from trees import Node

def verifica_abb(tree: Node) -> bool:
    """
    Verifica se a lista ligada é uma árvore binária de busca.
    """
    if tree is not None:
        if tree.left is not None:
            if tree.left.key > tree.key:
                return False
            if not verifica_abb(tree.left):
                return False
        if tree.right is not None:
            if tree.right.key < tree.key:
                return False
            if not verifica_abb(tree.right):
                return False

    return True

if __name__ == '__main__':
    # True
    tree = Node(35)
    tree.left = Node(14)
    tree.right = Node(80)
    tree.left.left = Node(12)
    tree.left.right = Node(22)
    print(verifica_abb(tree))

    # False
    tree = Node(35)
    tree.left = Node(14)
    tree.right = Node(80)
    tree.left.left = Node(15)
    tree.left.right = Node(22)
    print(verifica_abb(tree))