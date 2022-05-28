class Grafo:
    def __init__(self, num_nos):
        self.m_num_nos = num_nos
        self.m_grafo = []

    def adiciona_aresta(self, node1, node2, weight):
        self.m_grafo.append([node1, node2, weight])

    # Finds the root node of a subtree containing node `i`
    def find_subtree(self, parent, i):
        return i if parent[i] == i else self.find_subtree(parent, parent[i])

    # Connects subtrees containing nodes `x` and `y`
    def connect_subtrees(self, parent, subtree_sizes, x, y):
        xroot = self.find_subtree(parent, x)
        yroot = self.find_subtree(parent, y)
        if subtree_sizes[xroot] < subtree_sizes[yroot]:
            parent[xroot] = yroot
        elif subtree_sizes[xroot] > subtree_sizes[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            subtree_sizes[xroot] += 1

    def kruskals_mst(self):
        # Resulting tree
        result = []

        # Iterator
        i = 0
        # Number of edges in MST
        e = 0

        # Sort edges by their weight
        self.m_grafo = sorted(self.m_grafo, key=lambda item: item[2])

        # Auxiliary arrays
        parent = []
        subtree_sizes = []

        # Initialize `parent` and `subtree_sizes` arrays
        for node in range(self.m_num_nos):
            parent.append(node)
            subtree_sizes.append(0)

        # Important property of MSTs
        # number of egdes in a MST is 
        # equal to (m_num_nos - 1)
        while e < (self.m_num_nos - 1):
            # Pick an edge with the minimal weight
            node1, node2, weight = self.m_grafo[i]
            i = i + 1

            x = self.find_subtree(parent, node1)
            y = self.find_subtree(parent, node2)

            if x != y:
                e += 1
                result.append([node1, node2, weight])
                self.connect_subtrees(parent, subtree_sizes, x, y)

        # Print the resulting MST
        for node1, node2, weight in result:
            print("%d - %d: %d" % (node1+1, node2+1, weight))

if __name__ == '__main__':
    lines = []
    with open('grafo1.txt') as f:
        lines = f.readlines()

    g, u, v, w = None, None, None, None

    for count, line in enumerate(lines, start=1):
        if count == 1:
            V = int(line)
            g = Grafo(V)
        else:
            u, v, w = line.split()
            print(f'>> {count}: {u}, {v}, {w}')
            g.adiciona_aresta(int(u), int(v), int(w))

    g.kruskals_mst()