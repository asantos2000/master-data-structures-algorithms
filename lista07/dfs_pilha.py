class lista_adjacente:
    """
    Classe que representa um grafo com lista de adjacência.
    """
    def __init__(self, n):
        """
        Construtor da classe.
        """
        self.n = n
        self.adj = [[] for i in range(n)]

    def adiciona_aresta(self, u, v):
        """
        Adiciona uma aresta no grafo.
        """
        self.adj[u].append(v)

    def imprime(self):
        """
        Imprime o grafo.
        """
        for i in range(self.n):
            print(i, ":", self.adj[i])
    

    def dfs_pilha(self, no):
        """
        Função que percorre um grafo em profundidade usando pilha explícita.
        """
        visitado = [False] * self.n
        pilha = []
        pilha.append(no)
        visitado[no] = True
        visitou = False
        while len(pilha) > 0:
            no = pilha.pop()
            self.adj[no].reverse()
            while len(self.adj[no]) > 0 and not visitou:
                v = self.adj[no].pop()
                if visitado[v] == False:
                    pilha.append(v)
                    visitado[v] = True
                    visitou = True
            visitou = False
        
        print(pilha)

if __name__ == "__main__":
    G = lista_adjacente(9)
    G.adiciona_aresta(0, 1)
    G.adiciona_aresta(0, 3)
    G.adiciona_aresta(0, 6)
    G.adiciona_aresta(1, 0)
    G.adiciona_aresta(1, 2)
    G.adiciona_aresta(1, 4)
    G.adiciona_aresta(1, 7)
    G.adiciona_aresta(2, 1)
    G.adiciona_aresta(2, 7)
    G.adiciona_aresta(3, 0)
    G.adiciona_aresta(3, 4)
    G.adiciona_aresta(4, 1)
    G.adiciona_aresta(4, 3)
    G.adiciona_aresta(4, 5)
    G.adiciona_aresta(5, 4)
    G.adiciona_aresta(5, 6)
    G.adiciona_aresta(5, 8)
    G.adiciona_aresta(6, 0)
    G.adiciona_aresta(6, 5)
    G.adiciona_aresta(6, 7)
    G.adiciona_aresta(6, 8)
    G.adiciona_aresta(7, 1)
    G.adiciona_aresta(7, 2)
    G.adiciona_aresta(7, 6)
    G.adiciona_aresta(7, 8)
    G.adiciona_aresta(8, 5)
    G.adiciona_aresta(8, 6)
    G.adiciona_aresta(8, 7)

    print("Grafo:")
    G.imprime()

    G.dfs_pilha(0)
