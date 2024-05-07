import networkx as nx
import matplotlib.pyplot as plt
import random
import heapq
import pickle
import time


class Centrality:
    """
    This constructor takes a graph as a dictionary and stores it for later
    centrality computations.
    """

    def __init__(self, **kwargs):
        file = kwargs.get("file")
        self.G = nx.Graph()
        self.edge_list = []

        if file:
            with open(file) as f:
                self.G = nx.read_edgelist(f)
                for line in f:
                    # generate a list of tuples that represent the edges
                    edge = line.strip().split()
                    self.edge_list.append((edge[0], edge[1]))
        else:
            n = kwargs.get("n")
            p = kwargs.get("p")
            self.G = nx.erdos_renyi_graph(n, p)
            pickle.dump(
                self.G, open("erdos_renyi_graph" + str(n) + "_" + str(p) + ".pkl", "wb")
            )
        print(file)
        print("Nodes: ", self.G.number_of_nodes())
        print("Edges: ", self.G.number_of_edges())
        print()

    def centralities(self):
        centrality_functions = {
            "degree": nx.degree_centrality,
            "closeness": nx.closeness_centrality,
            "betweenness": nx.betweenness_centrality,
            "pagerank": nx.pagerank,
        }

        centrality_dicts = {}

        start_time = time.time()
        for measure in centrality_functions:
            centrality_dict = centrality_functions[measure](self.G)
            centrality_dicts[measure] = centrality_dict
            print(measure + ":", time.time() - start_time, "seconds")
        print()
        return centrality_dicts


if __name__ == "__main__":
    prefix = "datasets/"
    files = [
        "email-Eu-core.txt",
        "collaboration.edgelist.txt",
        "phonecalls.edgelist.txt",
        "email.edgelist.txt",
    ]

    graph_sizes = [1000, 10000]

    for f in files:
        c = Centrality(file=(prefix + f))
        pickle.dump(c.centralities(), open(f + ".pkl", "wb"))

    for n in graph_sizes:
        c = Centrality(n=n, p=0.1)
        filename = "erdos_renyi_centralities" + str(n) + ".pkl"
        pickle.dump(c.centralities(), open(filename, "wb"))

    # filename = "email.edgelist.txt.pkl"
    # centrality = pickle.load(open(filename, "rb"))
    # print(centrality)
