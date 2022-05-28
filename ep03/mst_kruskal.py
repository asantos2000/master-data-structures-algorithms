# Source https://www.ime.usp.br/~pf/analise_de_algoritmos/aulas/MST-kruskal.html#MST-Kruskal
# MST-Kruskal (G, n, m, p)
# 1  arestas := ordena-arestas (G, m, p)
# 2  resultado := { }
# 3  inicializa()
# 4  para i := 1 até m
# 5     uv := arestas[i]
# 6     r := encontra_sub_arvore(u)
# 7     s := encontra_sub_arvore(v)
# 8     se r ≠ s
# 9         resultado := resultado ∪ { uv }
# 10        conecta_sub_arvore(r, s)
# 11  retrona resultado

import sys

class Grafo:
    # inicializa
    def __init__(self, num_nos):
        self.m_num_nos = num_nos
        self.m_grafo = []

    def adiciona_aresta(self, no1, no2, custo):
        self.m_grafo.append([no1, no2, custo])

    # Encontra a raiz do no da subarvore contendo o no `i`
    # Encontra qual grupo o no `i` pertence
    def encontra_sub_arvore(self, pai, i):
        return i if pai[i] == i else self.encontra_sub_arvore(pai, pai[i])

    # Conecta subarvore contendo nos `r` e `s`
    # Merge dos grupos de nos `r` e `s`
    def conecta_sub_arvore(self, pai, sub_arvore_tamanho, r, s):
        r_raiz = self.encontra_sub_arvore(pai, r)
        s_raiz = self.encontra_sub_arvore(pai, s)
        if sub_arvore_tamanho[r_raiz] < sub_arvore_tamanho[s_raiz]:
            pai[r_raiz] = s_raiz
        elif sub_arvore_tamanho[r_raiz] > sub_arvore_tamanho[s_raiz]:
            pai[s_raiz] = r_raiz
        else:
            pai[s_raiz] = r_raiz
            sub_arvore_tamanho[r_raiz] += 1

    def mst_kruskal(self):
        # Arvore resultante
        resultado = []

        i = 0
        # Número de arestas na MST
        e = 0

        # ordena-arestas
        self.m_grafo = sorted(self.m_grafo, key=lambda item: item[2])

        pai = []
        sub_arvore_tamanho = []

        # Inicializa os vetores pai e sub_arvore_tamanho
        for no in range(self.m_num_nos):
            pai.append(no)
            sub_arvore_tamanho.append(0)

        while e < (self.m_num_nos - 1):
            # Escolhe uma aresta com custo mínimo
            no1, no2, custo = self.m_grafo[i]
            i = i + 1

            r = self.encontra_sub_arvore(pai, no1)
            s = self.encontra_sub_arvore(pai, no2)

            if r != s:
                e += 1
                resultado.append([no1, no2, custo])
                self.conecta_sub_arvore(pai, sub_arvore_tamanho, r, s)

        # Retorna a MST e custo
        return resultado, sum(map(lambda item: item[2], resultado))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Uso: python mst_kruskal.py <arquivo_grafo>')
        sys.exit(1)
    
    lines = []
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    g, u, v, w = None, None, None, None

    for count, line in enumerate(lines, start=1):
        if count == 1:
            V = int(line)
            g = Grafo(V)
        else:
            u, v, w = line.split()
            g.adiciona_aresta(int(u), int(v), int(w))

    print(f'mst, custo: {g.mst_kruskal()}')