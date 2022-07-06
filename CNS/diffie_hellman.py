def main():
    p = int(input("Enter a prime number: "))
    g = int(input(f"Enter a primitive root modulo {p}: "))

    a, b = map(int, input("Enter private keys for Alice and Bob: ").split())

    x = int(pow(g, a, p))
    y = int(pow(g, b, p))

    ka = int(pow(y, a, p))
    kb = int(pow(x, b, p))

    print(f"Secret key for the Alice is: {ka}")
    print(f"Secret Key for the Bob is: {kb}")


if __name__ == '__main__':
    main()
