def n_queens(n):
    def backtrack(r):
        nonlocal n, column, anti_diagonal, diagonal, output, result
        if r == n:
            result.append(output[:])
            return

        for c in range(n):
            if c in column or (r + c) in anti_diagonal or (r - c) in diagonal:
                continue

            column.add(c)
            anti_diagonal.add(r + c)
            diagonal.add(r - c)
            output.append('-' * c + 'Q' + '-' * (n - c - 1))
            backtrack(r + 1)

            column.remove(c)
            anti_diagonal.remove(r + c)
            diagonal.remove(r - c)
            output.pop()

    if n == 0:
        return []
    column = set()
    anti_diagonal = set()
    diagonal = set()
    output = []
    result = []

    backtrack(0)
    return result


def main():
    queens = int(input("Enter the number of queens: "))
    solutions = n_queens(queens)
    print(f"There are {len(solutions)} solutions")
    for board in solutions:
        print(*board, sep="\n", end="\n\n")


if __name__ == "__main__":
    main()
