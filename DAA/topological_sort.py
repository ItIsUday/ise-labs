class Graph:
    class Node:
        def __init__(self, value, adjacent=None):
            self.value = value
            self.adjacent = adjacent if adjacent else []

        def add_adjacent(self, child):
            self.adjacent.append(child)

    def __init__(self, nodes=None):
        self.nodes = {}
        if nodes:
            self.add_all_nodes(nodes)

    def add_node(self, value):
        self.nodes[value] = Graph.Node(value)

    def add_all_nodes(self, nodes):
        for i in nodes:
            self.add_node(i)
        for i, adjacent in nodes.items():
            for j in adjacent:
                self.nodes[i].add_adjacent(self.nodes[j])

    def topological_sort_source_removal(self, root):
        pass

    def topological_sort_dfs(self):
        def dfs_util(n):
            visited.add(n)
            for i in self.nodes[n].adjacent:
                if i.value not in visited:
                    dfs_util(i.value)
            arr.insert(0, n)

        visited = set()
        arr = []
        for node in self.nodes:
            if node not in visited:
                dfs_util(node)

        return arr


def main():
    nodes = list(filter(bool, input("Enter the nodes: ").split(" ")))
    print("Enter adjacent nodes for each node: ")
    g = {node: list(filter(bool, input(f"\t{node}: ").split(" "))) for node in nodes}
    graph = Graph(g)
    print(f"Topological sorting using DFS: {' -> '.join(graph.topological_sort_dfs())}")


if __name__ == "__main__":
    main()
