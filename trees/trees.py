class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.left = None
        self.right = None
        self.data = data

    def imprime_arvore(self):
        print("(", end="")
        print(self.key, end="")
        if self.left:
            self.left.imprime_arvore()
        if self.right:
            self.right.imprime_arvore()
        print(")", end="")

    # O(n) tanto no pior quanto no melhor caso
    def nivel(self, no, k, nivel=0):
        if (no is None):
            return -1
        else:
            if no.key == k:
                return nivel
            else:
                nivelEsq = self.nivel(no.left, k, nivel + 1)
                if nivelEsq >= 0:
                    return nivelEsq
                else:
                    return self.nivel(no.right, k, nivel + 1)

    # O(h), O(n) no pior caso e O(lg n) no caso médio
    def insere(self, val):
        if self.key:
            if val <= self.key:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insere(val)
            else:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insere(val)
        else:
            self.val = val

    # O(h), O(n) no pior caso e O(lg n) no caso médio
    def busca(self, k):
        if (self == None) or (self.key == k):  # árvore vazia ou achou k
            return self
        if (k < self.key):  # pesquisa na subárvore esquerda
            return self.left.busca(k)
        else:  # pesquisa na subárvore direita
            return self.right.busca(k)

    def minimo(self):
        if self.left is None:
            return self.key
        else:
            return self.left.minimo()

    def remove(self, k):
        if self.key == k:
            if self.left is None and self.right is None:
                self = None
            elif self.left is None:
                self = self.right
            elif self.right is None:
                self = self.left
            else:
                self.key = self.right.minimo()
        elif self.key > k:
            self.left.remove(k)
        else:
            self.right.remove(k)

    def percurso_pre_ordem(self):
        if self is not None:
            print(self.key, end=",")
            if self.left is not None:
                self.left.percurso_pre_ordem()
            if self.right is not None:
                self.right.percurso_pre_ordem()

    def percurso_in_ordem(self):
        if self is not None:
            if self.left is not None:
                self.left.percurso_in_ordem()
            print(self.key, end=",")
            if self.right is not None:
                self.right.percurso_in_ordem()

    def percurso_pos_ordem(self):
        if self is not None:
            if self.left is not None:
                self.left.percurso_pos_ordem()
            if self.right is not None:
                self.right.percurso_pos_ordem()
            print(self.key, end=",")

    def percurso_em_largura(self):
        if self is not None:
            fila = []
            fila.append(self)
            while len(fila) > 0:
                no = fila.pop(0)
                print(no.key, end=",")
                if no.left is not None:
                    fila.append(no.left)
                if no.right is not None:
                    fila.append(no.right)

if __name__ == "__main__":
    root = Node(35)
    root.left = Node(14)
    root.right = Node(80)
    root.left.left = Node(12)
    root.left.right = Node(22)

    #root.insere(root, Node(48))
    root.insere(48)

    print(root.nivel(root, 35, 0))
    print(root.nivel(root, 14, 0))
    print(root.nivel(root, 80, 0))
    print(root.nivel(root, 12, 0))
    print(root.nivel(root, 22, 0))
    print(root.nivel(root, 48, 0))
    print(root.nivel(root.left, 14, 0))
    root.imprime_arvore()
    print("\n")

    b = root.busca(80)
    print(b.left, b.right, b.key)

    b = root.busca(35)
    print(b.left, b.right, b.key)

    b = root.busca(48)
    print(b.left, b.right, b.key)

    root.remove(48)
    root.imprime_arvore()
    print("\n")

    print('Pre-ordem:')
    root.percurso_pre_ordem()
    print("\n")

    print('In-ordem:')
    root.percurso_in_ordem()
    print("\n")

    print('Pos-ordem:')
    root.percurso_pos_ordem()
    print("\n")

    print('Largura:')
    root.percurso_em_largura()
    print("\n")
