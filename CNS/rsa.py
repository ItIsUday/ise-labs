from random import randrange


class RSA:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.public_key, self.private_key = self.generate_keypair()

    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    @staticmethod
    def is_prime(num):
        if num == 2:
            return True
        if num < 2 or num % 2 == 0:
            return False
        for n in range(3, int(num ** 0.5) + 2, 2):
            if num % n == 0:
                return False
        return True

    def generate_keypair(self):
        if not (self.is_prime(self.p) and self.is_prime(self.q)):
            raise ValueError('Both numbers must be prime.')
        elif self.p == self.q:
            raise ValueError('p and q cannot be equal')

        n = self.p * self.q
        phi = (self.p - 1) * (self.q - 1)
        e = randrange(1, phi)

        g = self.gcd(e, phi)
        while g != 1:
            e = randrange(1, phi)
            g = self.gcd(e, phi)

        d = pow(e, -1, phi)

        return (e, n), d

    def encrypt(self, plaintext):
        key, n = self.public_key
        return [pow(ord(char), key, n) for char in plaintext]

    def decrypt(self, ciphertext):
        _, n = self.public_key
        key = self.private_key
        return ''.join(chr(pow(char, key, n)) for char in ciphertext)


def main():
    p, q = map(int, input("Enter two distinct prime numbers: ").split())
    rsa = RSA(p, q)

    print(f"Public key is {rsa.public_key} and private key is {rsa.private_key}")

    message = input("Enter a message to encrypt with the public key: ")
    encrypted_msg = rsa.encrypt(message)

    print(f"Encrypted message: {''.join(map(str, encrypted_msg))}")
    print(f"Decrypted message: {rsa.decrypt(encrypted_msg)}")


if __name__ == '__main__':
    main()
