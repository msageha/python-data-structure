class AdjacencyList:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, u, v, directed=False):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        if not directed:
            self.graph[v].append(u)

    def remove_edge(self, u, v, directed=False):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
        if not directed and v in self.graph and u in self.graph[v]:
            self.graph[v].remove(u)

    def remove_node(self, node):
        if node in self.graph:
            for nbr in self.graph[node]:
                if node in self.graph[nbr]:
                    self.graph[nbr].remove(node)
            del self.graph[node]
            for k in self.graph:
                if node in self.graph[k]:
                    self.graph[k].remove(node)

    def neighbors(self, node):
        return self.graph[node] if node in self.graph else []

    def nodes(self):
        return list(self.graph.keys())

    def edges(self):
        e = []
        for u in self.graph:
            for v in self.graph[u]:
                e.append((u, v))
        return e
