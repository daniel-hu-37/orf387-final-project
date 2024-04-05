class Centrality:
    """
    This constructor takes a graph as a dictionary and stores it for later
    centrality computations.
    """

    def __init__(self, graph):
        self.graph = graph.graph_dict()
        # self.degree_nodes = []
        # self.closeness_nodes = []
        # self.betweenness_nodes = []
        # self.eigenvector_nodes = []
        # self.pagerank_nodes = []
        # self.katz_nodes = []

    def degree(self):
        keys = sorted(
            list(self.graph.keys()), key=lambda x: len(self.graph[x]), reverse=True
        )
        return keys

    def closeness(self):
        pass

    def betweenness(self):
        pass

    def eigenvector(self):
        pass

    def pagerank(self):
        pass

    def katz(self):
        pass
