def dfs_iterative(graph, start):
    stack = [start]
    path = []

    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        stack.extend(iter(graph[vertex][::-1]))
    return path

def verificar_ciclos(graph, start):
    stack = [start]
    visited = []

    while stack:
        vertex = stack.pop()
        if vertex in visited:
            return True
        visited.append(vertex)
        stack.extend(iter(graph[vertex][::-1]))
    return False


if __name__ == "__main__":
    g = {1: [2, 3], 
         2: [4, 5],
         3: [5], 
         4: [6], 
         5: [6],
         6: [7], 
         7: []}

    print(dfs_iterative(g, 1))
    # [1, 3, 5, 6, 7, 2, 4]
    print(verificar_ciclos(g, 1))
    # False

    g = {1: [2, 3], 
         2: [1, 4, 5],
         3: [1, 5], 
         4: [2, 6], 
         5: [2, 3, 6],
         6: [4, 5, 7], 
         7: [6]}

    print(dfs_iterative(g, 1))
    # [1, 2, 4, 6, 5, 3, 7]
    print(verificar_ciclos(g, 1))
    # True

    g = {1: [2], 
         2: [3],
         3: []}

    print(dfs_iterative(g, 1))
    # [1, 2, 3]
    print(verificar_ciclos(g, 1))
    # False