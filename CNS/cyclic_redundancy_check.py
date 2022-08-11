class CRC:
    def __init__(self):
        self.codeword = None

    @staticmethod
    def xor(a, b):
        return ''.join('0' if a[i] == b[i] else '1' for i in range(1, len(b)))

    def divide(self, message, key):
        pick = len(key)
        tmp = message[:pick]

        while pick < len(message):
            if tmp[0] == '1':
                tmp = self.xor(key, tmp) + message[pick]
            else:
                tmp = self.xor('0' * pick, tmp) + message[pick]
            pick += 1

        tmp = self.xor(key, tmp) if tmp[0] == "1" else self.xor('0' * pick, tmp)

        remainder = tmp
        return remainder

    def encode_data(self, data, key):
        l_key = len(key)
        append_data = data + '0' * (l_key - 1)
        remainder = self.divide(append_data, key)
        self.codeword = data + remainder
        print("Remainder: ", remainder)
        print("Data: ", self.codeword)

    def decode_data(self, data, key):
        r = self.divide(data, key)
        print(f"The remainder is {r} and so {'No Error' if int(r) == 0 else 'Error'}")


def main():
    data = input("Enter a data word in binary: ")
    generator = input("Enter a generator in binary: ")
    c = CRC()
    c.encode_data(data, generator)
    c.decode_data(c.codeword, generator)
    print(c.codeword)


if __name__ == "__main__":
    main()
