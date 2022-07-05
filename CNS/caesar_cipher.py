class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift % 26

    def encrypt(self, plain_text):
        return ''.join(chr(ord(c) + self.shift) for c in plain_text)

    def decrypt(self, cipher_text):
        return ''.join(chr(ord(c) - self.shift) for c in cipher_text)


def main():
    shift = int(input("Enter the shift value: "))
    text = input("Enter a text: ")

    cipher = CaesarCipher(shift)
    encrypted = cipher.encrypt(text)
    decrypted = cipher.decrypt(encrypted)
    print(f"Encrypted: {encrypted}", f"Decrypted: {decrypted}", sep='\n')


if __name__ == "__main__":
    main()
