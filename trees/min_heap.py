""" 
Min Heap é uma árvore binária quase completa, 
totalmente preenchida até o penúltimo nível e 
com todos os nós mais à esquerda no último nível
O menor elemento é a raiz da árvore e 
as subárvores possuem valores maiores ou iguais que o pai delas.
"""

class min_heap:
    def __init__(self, tamanho=0):
        self.tamanho = tamanho
        self.heap = [None for i in range(self.tamanho+1)]
        self.ultimo = -1

    def insere(self, elemento):
        self.ultimo = self.ultimo + 1
        self.heap[self.ultimo] = elemento
        self.subir(self.ultimo)

    def remove(self):
        maior = self.heap[0]
        self.heap[0] = self.heap[self.ultimo]
        self.ultimo = self.ultimo - 1
        self.descer(0)
        return maior

    def obterMenor(self):
        return self.heap[0]

    def subir(self, filho):
        pai = filho // 2
        if (pai >= 0):  # pai está dentro do heap
            if (self.heap[filho] < self.heap[pai]):  # troca pai e filho
                self.heap[filho], self.heap[pai] = self.heap[pai], self.heap[filho]
                self.subir(pai)

    def descer(self, pai):
        filho = pai * 2
        if (filho <= self.ultimo):
            if (filho < self.ultimo):
                if (self.heap[filho + 1] < self.heap[filho]):
                    filho = filho + 1
            if (self.heap[pai] > self.heap[filho]):
                self.heap[filho], self.heap[pai] = self.heap[pai], self.heap[filho]
                self.descer(filho)

    def constroiHeapDescendo(self, arvore, heap):
        """
        Constroi a heap descendo a partir da raiz da árvore.
        """
        if self.arvore is None:
            return
        else:
            self.constroiHeapDescendo(arvore.esquerda, heap)
            self.constroiHeapDescendo(arvore.direita, heap)
            self.heap.append(self.arvore)

    # def imprimeHeap(self, p):
    #     if (p <= self.ultimo):
    #         print(self.heap[p])
    #         self.imprimeHeap(2 * p)
    #         self.imprimeHeap(2 * p + 1)

    def imprimeHeap(self):
        i = 0
        while i <= self.ultimo:
            print(self.heap[i], end=" ")
            i = i + 1


if __name__ == '__main__':
    import heapq

    print("Exemplo 1")
    print("Heapq python")
    a = [10, 20, 30, 40, 50]
    heapq.heapify(a)
    print(a)
    h = min_heap(10)
    h.insere(10)
    h.insere(20)
    h.insere(30)
    h.insere(40)
    h.insere(50)
    print("heap:", end=" ")
    h.imprimeHeap()
    print("")
    print("Minimo")
    print(f"Menor (sem remover): {h.obterMenor()}")
    print(f"Remover menor: {h.remove()}")
    print(f"Remover menor: {h.remove()}")
    print(f"Remover menor: {h.remove()}")
    print(f"Menor (sem remover): {h.obterMenor()}")
    print("heap:", end=" ")
    h.imprimeHeap()

    print("\nExemplo 2")
    print("Heapq python")
    a = [1, 2, 4, 3, 9, 7, 8, 10, 14, 16, 50]
    heapq.heapify(a)
    print(a)
    h = min_heap(11)
    h.insere(1)
    h.insere(2)
    h.insere(4)
    h.insere(3)
    h.insere(9)
    h.insere(7)
    h.insere(8)
    h.insere(10)
    h.insere(14)
    h.insere(16)
    h.insere(50)
    print("heap:", end=" ")
    h.imprimeHeap()
    print("")
    print("Minimo")
    print(f"Menor (sem remover): {h.obterMenor()}")
    print(f"Remover menor: {h.remove()}")
    print(f"Remover menor: {h.remove()}")
    print(f"Remover menor: {h.remove()}")
    print(f"Menor (sem remover): {h.obterMenor()}")
    print("heap:", end=" ")
    h.imprimeHeap()
