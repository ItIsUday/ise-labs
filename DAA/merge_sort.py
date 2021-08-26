from math import log
from random import sample

from prettytable import PrettyTable


def merge(arr, start, mid, end):
    left_copy, right_copy = arr[start:mid + 1], arr[mid + 1:end + 1]
    ops_count, p, q, r = 0, 0, 0, start

    while p < len(left_copy) and q < len(right_copy):
        if left_copy[p] <= right_copy[q]:
            arr[r] = left_copy[p]
            p += 1
        else:
            arr[r] = right_copy[q]
            q += 1
        ops_count += 1
        r += 1

    while p < len(left_copy):
        arr[r] = left_copy[p]
        p += 1
        r += 1
        ops_count += 1

    while q < len(right_copy):
        arr[r] = right_copy[q]
        q += 1
        r += 1
        ops_count += 1

    return ops_count


def merge_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start >= end:
        return 0

    mid = (end + start) // 2
    left_ops_count = merge_sort(arr, start, mid)
    right_ops_count = merge_sort(arr, mid + 1, end)
    merge_ops_count = merge(arr, start, mid, end)

    return left_ops_count + right_ops_count + merge_ops_count


def merge_sort_complexity(length):
    return length * log(length, 2)


def sort_from_io():
    print("Enter the elements of an array: ", end="")
    array = list(map(int, input().split(" ")))
    merge_sort(array)
    print("After sorting:", array)


def complexity_analysis():
    table = PrettyTable(["Size: n", "Ascending, t(n)", "Ascending, g(n)",
                         "Descending, t(n)", "Descending, g(n)",
                         "Random, t(n)", "Random, g(n)"])

    size = 32
    for i in range(5):
        row = [size]
        array_to_sort = list(range(size))
        row.append(merge_sort(array_to_sort))
        row.append(merge_sort_complexity(size))

        array_to_sort = list(range(size, 0, -1))
        row.append(merge_sort(array_to_sort))
        row.append(merge_sort_complexity(size))

        array_to_sort = sample(range(size), size)
        row.append(merge_sort(array_to_sort))
        row.append(merge_sort_complexity(size))

        table.add_row(row)
        size *= 2

    print(table)


def main():
    print("\t\tMerge Sort")
    choice = int(input("Enter 1 to try merge sort or 2 for complexity analysis: "))
    if choice == 1:
        sort_from_io()
    elif choice == 2:
        complexity_analysis()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
