from string import ascii_lowercase


class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift
        self.alphabet = ascii_lowercase
        self.index = {char: i for i, char in enumerate(self.alphabet)}

    def encrypt(self, plaintext):
        return ''.join(self.alphabet[(self.index[c] + self.shift) % 26] for c in plaintext if c in self.index)

    def decrypt(self, ciphertext):
        return ''.join(self.alphabet[(self.index[c] - self.shift) % 26] for c in ciphertext if c in self.index)


def main():
    shift = int(input("Enter the shift value: "))
    text = input("Enter a text: ")

    cipher = CaesarCipher(shift)
    encrypted = cipher.encrypt(text)
    decrypted = cipher.decrypt(encrypted)
    print(f"Encrypted: {encrypted}", f"Decrypted: {decrypted}", sep='\n')


if __name__ == "__main__":
    main()
