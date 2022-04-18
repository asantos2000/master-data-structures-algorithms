# Function for DFS_Traversal traversal
def DFS_Traversal(graph, v, visited, parent_node=-1):
    
    # assign current node as
    visited[v] = True

    # loop for every edge (v, u)
    for u in graph[v]:
        # if u is not visited
        if not visited[u]:
            if DFS_Traversal(graph, u, visited, v):
                return True

        # if u is visited, and u is not a parent_node
        elif u != parent_node:
            # found a back-edge 
            return True

    # No back-edges were found 
    return False


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
