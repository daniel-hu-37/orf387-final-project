from centrality import *
from graph import *


def main():
    test_graph = Graph(file="datasets/email.edgelist.txt")
    test_centrality = Centrality(test_graph)


if __name__ == "__main__":
    main()
