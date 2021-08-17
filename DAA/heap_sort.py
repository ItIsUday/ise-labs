from math import log
from random import sample

from prettytable import PrettyTable


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    ops_count = 0

    if left < n and arr[i] < arr[left]:
        largest = left
        ops_count += 1

    if right < n and arr[largest] < arr[right]:
        largest = right
        ops_count += 1

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        ops_count += heapify(arr, n, largest)

    return ops_count


def heap_sort(arr):
    n = len(arr)
    ops_count = 0

    for i in range(n // 2, -1, -1):
        ops_count += heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        ops_count += heapify(arr, i, 0)

    return ops_count


def heap_sort_complexity(length):
    return length * log(length, 2)


def sort_from_io():
    print("Enter the elements of an array: ", end="")
    array = list(map(int, input().split(" ")))
    heap_sort(array)
    print("After sorting:", array)


def complexity_analysis():
    table = PrettyTable(["Size: n", "Ascending, t(n)", "Ascending, g(n)",
                         "Descending, t(n)", "Descending, g(n)",
                         "Random, t(n)", "Random, g(n)"])

    size = 32
    for i in range(5):
        row = [size]
        array_to_sort = list(range(size))
        row.append(heap_sort(array_to_sort))
        row.append(heap_sort_complexity(size))

        array_to_sort = list(range(size, 0, -1))
        row.append(heap_sort(array_to_sort))
        row.append(heap_sort_complexity(size))

        array_to_sort = sample(range(size), size)
        row.append(heap_sort(array_to_sort))
        row.append(heap_sort_complexity(size))

        table.add_row(row)
        size *= 2

    print(table)


def main():
    print("\t\tHeap Sort")
    choice = int(input("Enter 1 to try heap sort or 2 for complexity analysis: "))
    if choice == 1:
        sort_from_io()
    elif choice == 2:
        complexity_analysis()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
