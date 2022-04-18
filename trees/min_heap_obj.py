""" 
Min Heap Object é uma árvore binária quase completa, 
totalmente preenchida até o penúltimo nível e 
com todos os nós mais à esquerda no último nível
O menor elemento é a raiz da árvore e 
as subárvores possuem valores maiores ou iguais que o pai delas.
Implementada com vetor, permite armazenar qualquer tipo de dado em
um dicionário cuja a 'chave' é um atributo numérico e o 'valor' é qualquer objeto.
"""

Elemento = dict[int, object]
# p = priority, v = value
# Example: {"p": 1, "v": any_type}


class min_heap:
    def __init__(self, tamanho=0):
        self.tamanho = tamanho
        self.heap = [None for _ in range(self.tamanho)]
        self.ultimo = -1

    def insere(self, elemento: Elemento):
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

    def subir(self, filho: Elemento):
        pai = filho // 2
        if (pai >= 0):  # pai está dentro do heap
            if (self.heap[filho]["p"] < self.heap[pai]["p"]):  # troca pai e filho
                self.heap[filho], self.heap[pai] = self.heap[pai], self.heap[filho]
                self.subir(pai)

    def descer(self, pai: Elemento):
        filho = pai * 2
        if (filho <= self.ultimo):
            if (filho < self.ultimo):
                if (self.heap[filho + 1]["p"] < self.heap[filho]["p"]):
                    filho = filho + 1
            if (self.heap[pai]["p"] > self.heap[filho]["p"]):
                self.heap[filho], self.heap[pai] = self.heap[pai], self.heap[filho]
                self.descer(filho)

    def imprimeHeap(self):
        i = 0
        while i <= self.ultimo:
            print(
                f"p:{self.heap[i]['p']},v:{self.heap[i]['v']}", end=" ")
            i = i + 1


if __name__ == '__main__':
    import heapq
    g = object()
    print("Exemplo 1")
    h = min_heap(5)
    h.insere({"p": 10, "v": g})
    h.insere({"p": 20, "v": g})
    h.insere({"p": 30, "v": g})
    h.insere({"p": 40, "v": g})
    h.insere({"p": 50, "v": g})
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
    h.insere({"p": 1, "v": g})
    h.insere({"p": 2, "v": g})
    h.insere({"p": 4, "v": g})
    h.insere({"p": 3, "v": g})
    h.insere({"p": 9, "v": g})
    h.insere({"p": 7, "v": g})
    h.insere({"p": 8, "v": g})
    h.insere({"p": 10, "v": g})
    h.insere({"p": 14, "v": g})
    h.insere({"p": 16, "v": g})
    h.insere({"p": 50, "v": g})
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
