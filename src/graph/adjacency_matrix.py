class AdjacencyMatrix:
    def __init__(self):
        self.nodes_list = []
        self.node_index = {}
        self.matrix = []

    def add_node(self, node):
        if node not in self.node_index:
            idx = len(self.nodes_list)
            self.nodes_list.append(node)
            self.node_index[node] = idx
            for row in self.matrix:
                row.append(0)
            self.matrix.append([0] * (idx + 1))

    def add_edge(self, u, v, directed=False):
        if u not in self.node_index:
            self.add_node(u)
        if v not in self.node_index:
            self.add_node(v)
        ui = self.node_index[u]
        vi = self.node_index[v]
        self.matrix[ui][vi] = 1
        if not directed:
            self.matrix[vi][ui] = 1

    def remove_edge(self, u, v, directed=False):
        if u in self.node_index and v in self.node_index:
            ui = self.node_index[u]
            vi = self.node_index[v]
            self.matrix[ui][vi] = 0
            if not directed:
                self.matrix[vi][ui] = 0

    def remove_node(self, node):
        if node in self.node_index:
            idx = self.node_index[node]
            for i in range(len(self.matrix)):
                self.matrix[i].pop(idx)
            self.matrix.pop(idx)
            removed = self.nodes_list.pop(idx)
            del self.node_index[removed]
            for i, n in enumerate(self.nodes_list):
                self.node_index[n] = i

    def neighbors(self, node):
        if node not in self.node_index:
            return []
        idx = self.node_index[node]
        return [
            self.nodes_list[i] for i, val in enumerate(self.matrix[idx]) if val != 0
        ]

    def nodes(self):
        return self.nodes_list[:]

    def edges(self):
        e = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] != 0:
                    e.append((self.nodes_list[i], self.nodes_list[j]))
        return e
