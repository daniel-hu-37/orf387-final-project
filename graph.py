import random


class Graph:
    """
    Build a graph in two ways:
    (1): If a file is provided, using the edgelist "file"
    (2): No file is provided; build a graph with "n" nodes and edge probability "p"
    such that 0 <= p <= 1
    """

    def __init__(self, **kwargs):
        file = kwargs.get("file")
        self.graph = {}
        self.nodes, self.edges = 0, 0

        def add_directed_edge(graph, v1, v2):
            if v1 in graph:
                graph[v1].add(v2)
            else:
                graph[v1] = {v2}

        def add_undirected_edge(graph, v1, v2):
            add_directed_edge(graph, v1, v2)
            add_directed_edge(graph, v2, v1)

        if file:
            with open(file) as f:
                for line in f.readlines():
                    v1, v2 = [int(v) for v in line.split()]
                    add_undirected_edge(self.graph, v1, v2)
                    self.edges += 1

        else:
            n, p = kwargs.get("n"), kwargs.get("p")

            for v1 in range(n):
                for v2 in range(v1 + 1, n):
                    draw = random.random()
                    if draw <= p:
                        add_undirected_edge(self.graph, v1, v2)
                        self.edges += 1

        self.nodes = len(self.graph)

    def __str__(self):
        return str(self.graph)

    def node_count(self):
        return self.nodes

    def edge_count(self):
        return self.edges

    def graph_dict(self):
        return self.graph
