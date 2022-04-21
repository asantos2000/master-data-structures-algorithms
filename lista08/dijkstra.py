def dijkstra(grafo, origem):
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[origem] = 0
    vertices_visitados = []

    while vertices_visitados != grafo:
        vertice_atual = min(distancias, key=distancias.get)
        vertices_visitados.append(vertice_atual)
        for vizinho in grafo[vertice_atual]:
            if vizinho not in vertices_visitados:
                distancia_atual = distancias[vertice_atual] + grafo[vertice_atual][vizinho]
                if distancia_atual < distancias[vizinho]:
                    distancias[vizinho] = distancia_atual

    return distancias

if __name__ == "__main__":
    grafo = {'A': {'B': 2, 'C': 3},
             'B': {'A': 2, 'C': 1, 'D': 3},
             'C': {'A': 3, 'B': 1, 'D': 4, 'E': 3},
             'D': {'B': 3, 'C': 4, 'E': 1, 'F': 1},
             'E': {'C': 3, 'D': 1, 'F': 4},
             'F': {'D': 1, 'E': 4}}
    print(dijkstra(grafo, 'A'))