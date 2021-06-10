from collections import defaultdict, deque


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

    def topological_sort_source_removal(self):
        in_degree = defaultdict(int)
        for node in self.nodes:
            for adjacent in self.nodes[node].adjacent:
                in_degree[adjacent.value] += 1

        queue = deque()
        for node in self.nodes:
            if in_degree[node] == 0:
                queue.append(node)

        top_order = []
        while queue:
            popped_node = queue.popleft()
            top_order.append(popped_node)
            for node in self.nodes[popped_node].adjacent:
                in_degree[node.value] -= 1
                if in_degree[node.value] == 0:
                    queue.append(node.value)

        return top_order

    def topological_sort_dfs(self):
        def dfs_util(n):
            visited.add(n)
            for i in self.nodes[n].adjacent:
                if i.value not in visited:
                    dfs_util(i.value)
            top_order.insert(0, n)

        visited = set()
        top_order = []
        for node in self.nodes:
            if node not in visited:
                dfs_util(node)

        return top_order


def main():
    nodes = list(filter(bool, input("Enter the nodes: ").split(" ")))
    print("Enter adjacent nodes for each node: ")
    g = {node: list(filter(bool, input(f"\t{node}: ").split(" "))) for node in nodes}
    graph = Graph(g)
    print(f"Sorted using DFS: {' -> '.join(graph.topological_sort_dfs())}")
    print(f"Sorted using kahn's algorithm: {' -> '.join(graph.topological_sort_source_removal())}")


if __name__ == "__main__":
    main()
