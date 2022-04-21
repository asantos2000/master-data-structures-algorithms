# Function for DFS_Traversal traversal
def DFS_Traversal(graph, v, visited, parent_node=-1):
    # assign current node as
    visited[v] = True
    return any(not visited[u] and DFS_Traversal(graph, u, visited, v) or visited[u] and u != parent_node for u in graph[v])


if __name__ == '__main__':
    # Graph is represented using adjacent list.
    g = {1: [2, 3],
         2: [4, 5],
         3: [5],
         4: [6],
         5: [6],
         6: [7],
         7: []}
    visited = [False] * (len(g) + 1)
    # perform DFS traversal from source_node
    if DFS_Traversal(g, 1, visited):
        print('Cycle detected')
    else:
        print('Cycle not detected')
    print(visited)

    # Graph is represented using adjacent list.
    g = {1: [2, 3],
         2: [4, 5],
         3: [5],
         4: [6],
         5: [6],
         6: [7],
         7: [4]}
    visited = [False] * (len(g) + 1)
    # perform DFS traversal from source_node
    if DFS_Traversal(g, 1, visited):
        print('Cycle detected')
    else:
        print('Cycle not detected')
    print(visited)

    # Graph is represented using adjacent list.
    g = {1: [2],
         2: [3],
         3: []}
    visited = [False] * (len(g) + 1)
    # perform DFS traversal from source_node
    if DFS_Traversal(g, 1, visited):
        print('Cycle detected')
    else:
        print('Cycle not detected')
    print(visited)
