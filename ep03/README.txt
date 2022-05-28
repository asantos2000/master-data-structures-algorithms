# Algoritmo kruskal

Para executar:

Formato do arquivo que representa que grafo:

Linha 1 - quantidade de vértices
Lina 2..n - relação nó1 - nó2 e custo. Exemplo: Nó 0 conecta com nó 1 e com custo 2: 0 1 2

grafo1.txt

```txt
7
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
```

> Nós iniciam em zero.

![grafo1](mst.png)

Figura 1: Árvore geradora mínima (arestas ressaltadas) do grafo1.txt

```bash
python mst_kruskal.py grafo1.txt
# mst, custo: ([[0, 3, 5], [2, 4, 5], [3, 5, 6], [0, 1, 7], [1, 4, 7], [4, 6, 9]], 39)
```
