from collections import defaultdict
from heapq import heapify, heappop, heappush


class Graph:
    def __init__(self, source, adj_list):
        self.starting_node = source
        self.adj_list = adj_list

    def create_mst(self):
        mst = defaultdict(set)
        total_cost = 0
        visited = {self.starting_node}
        edges = [(cost, self.starting_node, dest) for dest, cost in self.adj_list[self.starting_node].items()]
        heapify(edges)

        while edges:
            cost, source, dest = heappop(edges)

            if dest not in visited:
                visited.add(dest)
                mst[source].add(dest)
                total_cost += cost
                for next_dest, cost in self.adj_list[dest].items():
                    if next_dest not in visited:
                        heappush(edges, (cost, dest, next_dest))

        return mst, total_cost


def main():
    g1 = Graph(*get_graph())
    mst, cost = g1.create_mst()
    print_mst(mst)
    print("Cost of the minimum spanning tree: " + str(cost) + "\n")


def get_graph():
    def parser(var):
        node, cost = var.split(" ")
        return node, int(cost)

    nodes = list(filter(bool, input("Enter the nodes: ").split(" ")))
    print("Enter the adjacency list in this format: \"node: node1 cost1, node2 cost2\"")
    graph = {node: dict(map(parser, input(f"{node}: ").split(", "))) for node in nodes}
    starting_node = input("Enter the starting node: ")
    return starting_node, graph


def print_mst(mst):
    print("Minimum spanning tree: ")
    for node, neighbors in mst.items():
        print(f"{node}: {' '.join(neighbors)}")


if __name__ == "__main__":
    main()
