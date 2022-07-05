from string import ascii_lowercase


class VigenereCipher:
    def __init__(self, key):
        self.key = key
        self.alphabet = ascii_lowercase
        self.index = {char: i for i, char in enumerate(self.alphabet)}

    def transform(self, letter, index, encrypt=True):
        shift = self.index[self.key[index % len(self.key)]]
        shift = shift if encrypt else -shift
        return self.alphabet[(self.index[letter] + shift) % len(self.alphabet)]

    def encrypt(self, plaintext):
        return "".join(self.transform(c, i, True) for i, c in enumerate(plaintext) if c in self.alphabet)

    def decrypt(self, ciphertext):
        return "".join(self.transform(c, i, False) for i, c in enumerate(ciphertext) if c in self.alphabet)


def main():
    key = input("Enter the key: ")
    cipher = VigenereCipher(key)
    plaintext = input("Enter the plaintext: ")
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)
    print(f"Ciphertext: {encrypted}")
    print(f"Decrypted: {decrypted}")


if __name__ == "__main__":
    main()
