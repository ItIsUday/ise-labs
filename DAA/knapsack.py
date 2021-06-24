def knapsack(capacity, values, weights, items):
    table = [[0 for _ in range(capacity + 1)] for _ in range(items + 1)]

    for i in range(1, items + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                table[i][w] = max(values[i - 1] + table[i - 1][w - weights[i - 1]],
                                  table[i - 1][w])
            else:
                table[i][w] = table[i - 1][w]

    return table[items][capacity]


def main():
    items = int(input("Enter the number of items: "))
    capacity = int(input("Enter the capacity of knapsack: "))
    weights = list(map(int, input("Enter the weights: ").split(" ")))
    values = list(map(int, input("Enter the values: ").split(" ")))

    print(f"Maximum value for given capacity is {knapsack(capacity, values, weights, items)}")


if __name__ == '__main__':
    main()
