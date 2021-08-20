from heapq import heappop, heappush


class Graph:
    def __init__(self, source, adj_list):
        self.starting_node = source
        self.adj_list = adj_list

    def find_shortest_paths(self):
        distances = {vertex: float("infinity") for vertex in self.adj_list}
        distances[self.starting_node] = 0

        pq = [(0, self.starting_node)]
        while pq:
            current_distance, current_vertex = heappop(pq)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.adj_list[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heappush(pq, (distance, neighbor))

        return distances


def main():
    graph = Graph(*get_graph())
    print_shortest_paths(graph.starting_node, graph.find_shortest_paths())


def get_graph():
    def parser(var):
        node, cost = var.split(" ")
        return node, int(cost)

    nodes = list(filter(bool, input("Enter the nodes: ").split(" ")))
    print("Enter the adjacency list in this format: \"node: node1 cost1, node2 cost2\"")
    graph = {node: dict(map(parser, input(f"{node}: ").split(", "))) for node in nodes}
    starting_node = input("Enter the starting node: ")
    return starting_node, graph


def print_shortest_paths(starting_node, paths):
    for node, distance in paths.items():
        print(f"The shortest distance from {starting_node} to {node} is {distance}")


if __name__ == "__main__":
    main()
