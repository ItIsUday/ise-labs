from collections import deque


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

    def bfs(self, root):
        if root not in self.nodes:
            return None

        queue = deque([self.nodes[root]])
        visited = set()

        while len(queue):
            node = queue.popleft()
            if node.value in visited:
                continue
            visited.add(node.value)
            yield node.value
            for adjacent in node.adjacent:
                if adjacent.value not in visited:
                    queue.append(adjacent)

    def dfs(self, root):
        if root not in self.nodes:
            return None

        stack = [self.nodes[root]]
        visited = set()

        while len(stack):
            node = stack.pop()
            if node.value in visited:
                continue
            visited.add(node.value)
            yield node.value
            for adjacent in node.adjacent:
                if adjacent.value not in visited:
                    stack.append(adjacent)

    def connectivity(self):
        def dfs_util(n):
            visited.add(n)
            for i in self.nodes[n].adjacent:
                if i.value not in visited:
                    dfs_util(i.value)

        visited = set()
        components = 0
        for node in self.nodes:
            if node not in visited:
                dfs_util(node)
                components += 1

        if components == 0:
            print("The graph does not exist")
        elif components == 1:
            print("The graph is connected")
        else:
            print(f"The graph is disconnected with {components} components")


def main():
    nodes = list(filter(bool, input("Enter the nodes: ").split(" ")))

    print("Enter adjacent nodes for each node: ")
    g = {node: list(filter(bool, input(f"\t{node}: ").split(" "))) for node in nodes}

    start_node = input("Enter the starting node: ")
    graph = Graph(g)
    print(f"BFS: {' -> '.join(list(graph.bfs(start_node)))}")
    print(f"DFS: {' -> '.join(list(graph.dfs(start_node)))}")
    graph.connectivity()


if __name__ == "__main__":
    main()
