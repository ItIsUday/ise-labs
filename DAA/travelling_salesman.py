from math import ceil


def copy_to_final(curr_path):
    global final_path
    final_path = curr_path.copy()
    final_path[-1] = curr_path[0]


def two_lowest_distance(adj, i):
    distances = adj[i].copy()
    distances.pop(i)

    first_min = second_min = float("infinity")
    for distance in distances:
        if distance <= first_min:
            first_min, second_min = distance, first_min
        elif distance < second_min:
            second_min = distance
    return first_min, second_min


def tsp_rec(adj, curr_bound, curr_weight, level, curr_path, visited):
    global final_res

    if level == N:
        if adj[curr_path[level - 1]][curr_path[0]] != 0:
            curr_res = curr_weight + adj[curr_path[level - 1]][curr_path[0]]
            if curr_res < final_res:
                copy_to_final(curr_path)
                final_res = curr_res
        return

    for i in range(N):
        if adj[curr_path[level - 1]][i] != 0 and not visited[i]:
            temp = curr_bound
            curr_weight += adj[curr_path[level - 1]][i]

            if level == 1:
                curr_bound -= ((two_lowest_distance(adj, curr_path[level - 1])[0] +
                                two_lowest_distance(adj, i)[0]) / 2)
            else:
                curr_bound -= ((two_lowest_distance(adj, curr_path[level - 1])[1] +
                                two_lowest_distance(adj, i)[0]) / 2)

            if curr_bound + curr_weight < final_res:
                curr_path[level] = i
                visited[i] = True

                tsp_rec(adj, curr_bound, curr_weight,
                        level + 1, curr_path, visited)
            curr_weight -= adj[curr_path[level - 1]][i]
            curr_bound = temp

            visited = [False] * len(visited)
            for j in range(level):
                if curr_path[j] != -1:
                    visited[curr_path[j]] = True


def tsp(adj):
    curr_bound = 0
    curr_path = [-1] * (N + 1)
    visited = [False] * N

    for i in range(N):
        curr_bound += (sum(two_lowest_distance(adj, i)))

    curr_bound = ceil(curr_bound / 2)

    visited[0] = True
    curr_path[0] = 0

    tsp_rec(adj, curr_bound, 0, 1, curr_path, visited)


N = int(input("Enter the number of nodes: "))
print("Enter the distance matrix: ")
graph = [list(map(int, input().split(" "))) for _ in range(N)]

final_path = []
final_res = float("infinity")
tsp(graph)

print("Minimum cost:", final_res)
print("Path:", " -> ".join(map(str, final_path)))
