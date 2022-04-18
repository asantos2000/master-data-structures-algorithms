def bfs(ma, vis):
    dimensao = len(ma)
    visitado = [False] * dimensao
    t = [0] * dimensao
    fila = [vis]
    visitado[vis] = True
    a = [[0, 0]]

    while fila:
        vis = fila.pop(0)
        for i, n in enumerate(ma[vis]):
            if (n == 1 and (not visitado[i])):
                fila.append(i)
                visitado[i] = True
                t[i] = t[vis] + 1
                a.append([i, t[i]])
    return a, max(t)

if __name__ == "__main__":
    # m is representing using adjacent matrix.
    #     1  2  3  4  5  6  7
    g = [[0, 1, 1, 0, 0, 0, 0], # 1
         [1, 0, 0, 1, 1, 0, 0], # 2
         [1, 0, 0, 0, 1, 0, 0], # 3
         [0, 1, 0, 0, 0, 1, 0], # 4
         [0, 1, 1, 0, 0, 1, 0], # 5
         [0, 0, 0, 1, 1, 0, 1], # 6
         [0, 0, 0, 0, 0, 1, 0]] # 7

    print(bfs(g, 0))

    #     0  1  2  3  4
    g = [[0, 1, 1, 0, 0], # 0
         [1, 0, 0, 1, 0], # 1
         [1, 0, 0, 0, 1], # 2
         [0, 1, 0, 0, 0], # 3
         [0, 0, 1, 0, 0]] # 4

    print(bfs(g, 0))

    #     A  B  C  D  E  F  G  H
    g = [[0, 1, 0, 1, 0, 0, 1, 0], # A
         [0, 0, 0, 0, 1, 0, 1, 0], # B
         [0, 1, 0, 0, 1, 0, 0, 1], # C
         [0, 0, 0, 0, 0, 1, 1, 0], # D
         [0, 0, 0, 0, 0, 0, 1, 0], # E
         [1, 0, 0, 0, 0, 0, 0, 0], # F
         [0, 0, 0, 0, 0, 1, 0, 0], # G
         [0, 0, 0, 0, 0, 0, 1, 0]] # H

    print(bfs(g, 0))
    # ([[0, 0], [1, 1], [3, 1], [6, 1], [4, 2], [5, 2]], 2)
    # A, B, D, H, E, G
