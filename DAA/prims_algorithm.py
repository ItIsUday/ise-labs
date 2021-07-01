class Node:
    def __init__(self, value, adjacent=None):
        self.value = value
        self.adjacent = adjacent if adjacent else []

    def add_adjacent(self, child):
        self.adjacent.append(child)


class WeightedGraph:
    class Node(Node):
        def add_adjacent(self, child, weight=0):
            self.adjacent.append((child, weight))

    def __init__(self, nodes=None):
        self.nodes = {}
        if nodes:
            self.add_all_nodes(nodes)

    def add_node(self, value):
        self.nodes[value] = WeightedGraph.Node(value)

    def add_all_nodes(self, nodes):
        for i in nodes:
            self.add_node(i)
        for i, adjacent in nodes.items():
            for j in adjacent:
                self.nodes[i].add_adjacent(self.nodes[j[0]], j[1])


class Tree:
    pass


class MinHeap:
    pass


def main():
    pass


if __name__ == "__main__":
    main()
