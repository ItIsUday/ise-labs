from collections import defaultdict


class Colors:
    GREEN = "\033[32;1m"
    RESET = "\033[0m"


def gen_shift_table(pattern):
    m = len(pattern)
    shift_table = defaultdict(lambda: m)
    for i in range(m - 1):
        shift_table[pattern[i]] = m - i - 1

    return shift_table


def find_pattern(text, pattern):
    m, n = len(pattern), len(text)
    table = gen_shift_table(pattern)
    i = m - 1

    while i <= n - 1:
        matched = 0
        while matched < m and pattern[m - matched - 1] == text[i - matched]:
            matched += 1

        if matched == m:
            return i - matched + 1
        else:
            i += table[text[i]]


def main():
    text = input("Enter a text: ")
    pattern = input("Enter a pattern: ")

    if start := find_pattern(text, pattern):
        end = start + len(pattern)
        print("Pattern found")
        print(f"{text[:start]}{Colors.GREEN}{text[start:end]}{Colors.RESET}{text[end:]}")
    else:
        print("Pattern not found")


if __name__ == "__main__":
    main()
