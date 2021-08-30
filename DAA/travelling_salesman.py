from math import ceil


class Graph:
    def __init__(self, graph):
        self.nodes = len(graph)
        self.graph = graph

        self.__final_path = []
        self.__final_res = float("infinity")

    def tsp(self):
        curr_bound = 0
        curr_path = [None] * (self.nodes + 1)
        visited = set()

        for i in range(self.nodes):
            curr_bound += sum(self.__two_lowest_distance(i))
        curr_bound = ceil(curr_bound / 2)

        visited.add(0)
        curr_path[0] = 0
        self.tsp_rec(curr_bound, 0, curr_path, 1, visited)

        return self.__final_res, self.__final_path

    def tsp_rec(self, curr_bound, curr_weight, curr_path, level, visited):
        if level == self.nodes:
            if self.graph[curr_path[level - 1]][curr_path[0]] != 0:
                curr_res = curr_weight + self.graph[curr_path[level - 1]][curr_path[0]]
                if curr_res < self.__final_res:
                    self.__final_path = curr_path.copy()
                    self.__final_path[-1] = curr_path[0]
                    self.__final_res = curr_res
            return

        for i in range(self.nodes):
            if self.graph[curr_path[level - 1]][i] != 0 and i not in visited:
                curr_bound_backup = curr_bound
                visited_backup = visited.copy()
                curr_weight += self.graph[curr_path[level - 1]][i]

                a, b = self.__two_lowest_distance(curr_path[level - 1])
                c, _ = self.__two_lowest_distance(i)
                if level == 1:
                    curr_bound -= (a + c) / 2
                else:
                    curr_bound -= (b + c) / 2

                if curr_bound + curr_weight < self.__final_res:
                    curr_path[level] = i
                    visited.add(i)
                    self.tsp_rec(curr_bound, curr_weight, curr_path, level + 1, visited)

                curr_weight -= self.graph[curr_path[level - 1]][i]
                curr_bound = curr_bound_backup
                visited = visited_backup

    def __two_lowest_distance(self, row):
        distances = self.graph[row].copy()
        distances.pop(row)

        first_min = second_min = float("infinity")
        for distance in distances:
            if distance <= first_min:
                first_min, second_min = distance, first_min
            elif distance < second_min:
                second_min = distance
        return first_min, second_min


def main():
    nodes = int(input("Enter the number of nodes: "))
    print("Enter the distance matrix: ")
    matrix = [list(map(int, input().split(" "))) for _ in range(nodes)]

    graph = Graph(matrix)
    cost, path = graph.tsp()

    print("Minimum cost:", cost)
    print("Path:", " -> ".join(map(str, path)))


if __name__ == "__main__":
    main()
