def bfs(g, v):
    visited = [False] * (len(g) + 1)
    queue = [v]
    visited[v] = True
    while queue:
        v = queue.pop(0)
        print(g[v])
        print(visited)
        for u in g[v]:
            if not visited[u]:
                queue.append(u)
                visited[u] = True
    return visited

if __name__ == "__main__":
    # Graph is representing using adjacent matrix.
    # #     1  2  3  4  5  6  7
    # g = [[0, 1, 1, 0, 0, 0, 0], # 1
    #      [1, 0, 0, 1, 1, 0, 0], # 2
    #      [1, 0, 0, 0, 1, 0, 0], # 3
    #      [0, 1, 0, 0, 0, 1, 0], # 4
    #      [0, 1, 1, 0, 0, 1, 0], # 5
    #      [0, 0, 0, 1, 1, 0, 1], # 6
    #      [0, 0, 0, 0, 0, 1, 0]] # 7

    g = [[0, 1, 1, 0, 0], [1, 0, 0, 1, 0], [1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0]]

    bfs(g, 0)
    
    