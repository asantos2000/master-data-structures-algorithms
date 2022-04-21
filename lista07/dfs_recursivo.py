def dfs_recursive(graph, vertex, path = None):
    if path is None:
        path = []
    path += [vertex]

    for neighbor in graph[vertex]:
        if neighbor not in path:
            path = dfs_recursive(graph, neighbor, path)

    return path


g = {1: [2, 3], 2: [4, 5],
     3: [5], 4: [6], 5: [6],
     6: [7], 7: []}

print(dfs_recursive(g, 1))
# [1, 2, 4, 6, 7, 5, 3]
