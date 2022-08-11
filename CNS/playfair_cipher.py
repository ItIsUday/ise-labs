from string import ascii_lowercase


class PlayfairCipher:
    def __init__(self, key):
        self.key = key
        self.alphabet = ascii_lowercase
        self.filler = "x"
        self.omitted = "j"
        self.key_matrix = self.create_key_matrix()
        self.key_to_index = {char: (i, j) for i, row in enumerate(self.key_matrix) for j, char in enumerate(row)}
        self.key_to_index[self.omitted] = self.key_to_index["i"]

    def create_key_matrix(self):
        key_set = dict.fromkeys(self.key)
        key_list = list(key_set)
        key_list.extend(char for char in self.alphabet if char not in key_set and char != self.omitted)
        key_matrix = [key_list[i * 5:(i + 1) * 5] for i in range(5)]
        return key_matrix

    def insert_filler(self, plaintext):
        new_plaintext = []
        for i, char in enumerate(plaintext):
            new_plaintext.append(char)
            if (i < len(plaintext) - 1 and char == plaintext[i + 1]) or (
                    i == len(plaintext) - 1 and len(new_plaintext) % 2 == 1):
                new_plaintext.append(self.filler)

        return new_plaintext

    def encrypt(self, plaintext):
        plaintext = "".join(char for char in plaintext if char.islower())
        new_plaintext = self.insert_filler(plaintext)
        ciphertext = []

        for i in range(0, len(new_plaintext), 2):
            i1, j1 = self.key_to_index[new_plaintext[i]]
            i2, j2 = self.key_to_index[new_plaintext[i + 1]]
            if i1 == i2:
                ciphertext.extend((self.key_matrix[i1][(j1 + 1) % 5], self.key_matrix[i2][(j2 + 1) % 5]))
            elif j1 == j2:
                ciphertext.extend((self.key_matrix[(i1 + 1) % 5][j1], self.key_matrix[(i2 + 1) % 5][j2]))
            else:
                ciphertext.extend((self.key_matrix[i1][j2], self.key_matrix[i2][j1]))

        return "".join(ciphertext)

    def decrypt(self, ciphertext):
        pass


def main():
    key = input("Enter the key: ")
    cipher = PlayfairCipher(key)
    plaintext = input("Enter the plaintext: ")
    print(f"Ciphertext: {cipher.encrypt(plaintext)}")


if __name__ == "__main__":
    main()
