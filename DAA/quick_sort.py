from random import sample

from prettytable import PrettyTable


def partition(arr, start, end):
    pivot = arr[start]
    low, high, ops_count = start + 1, end, 0

    while True:
        while low <= high and arr[high] >= pivot:
            high -= 1
            ops_count += 1

        while low <= high and arr[low] <= pivot:
            low += 1
            ops_count += 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break

    arr[start], arr[high] = arr[high], arr[start]

    return high, ops_count


def quick_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start >= end:
        return 0

    part_index, part_ops_count = partition(arr, start, end)
    left_ops_count = quick_sort(arr, start, part_index - 1)
    right_ops_count = quick_sort(arr, part_index + 1, end)

    return part_ops_count + left_ops_count + right_ops_count


def sort_from_io():
    print("Enter the elements of an array: ", end="")
    array = list(map(int, input().split(" ")))
    quick_sort(array)
    print("After sorting:", array)


def quick_sort_complexity(length):
    return length ** 2


def complexity_analysis():
    table = PrettyTable(["Size: n", "Ascending, t(n)", "Ascending, g(n)",
                         "Descending, t(n)", "Descending, g(n)",
                         "Random, t(n)", "Random, g(n)"])

    size = 32
    for i in range(5):
        row = [size]
        array_to_sort = list(range(size))
        row.append(quick_sort(array_to_sort))
        row.append(quick_sort_complexity(size))

        array_to_sort = list(range(size, 0, -1))
        row.append(quick_sort(array_to_sort))
        row.append(quick_sort_complexity(size))

        array_to_sort = sample(range(size), size)
        row.append(quick_sort(array_to_sort))
        row.append(quick_sort_complexity(size))

        table.add_row(row)
        size *= 2

    print(table)


if __name__ == "__main__":
    print("\t\tQuick Sort")
    choice = int(input("Enter 1 to try quick sort or 2 for complexity analysis: "))
    if choice == 1:
        sort_from_io()
    elif choice == 2:
        complexity_analysis()
    else:
        print("Invalid choice")
