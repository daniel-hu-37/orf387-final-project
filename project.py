from centrality import *
from graph import *

filenames = [
    "collaboration.edgelist.txt",
    "email-Eu-core.txt",
    "email.edgelist.txt",
    "phonecalls.edgelist.txt",
]


def print_stats():
    for fn in filenames:
        new_fn = "datasets/" + fn
        graph = Graph(file=new_fn)
        print(fn)
        print(graph.node_count(), graph.edge_count())
        print()


def main():
    print_stats()


if __name__ == "__main__":
    main()
