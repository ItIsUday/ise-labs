class Client:
    def __init__(self, rate, data=[]):
        self.rate = rate
        self.data = data

    def __str__(self):
        return f"<Client Rate: {self.rate}, Data: {self.data}>"


class Buffer:
    def __init__(self, buffer_size, buffer=[]):
        self.buffer_size = buffer_size
        self.buffer = buffer

    def check_state(self):
        return len(self.buffer) == 0

    def __str__(self):
        return f"<Buffer size: {self.buffer_size}, Buffer: {self.buffer}>"


def main():
    base_state = True
    buffer = Buffer(int(input("Enter buffer size: ")))
    client = Client(int(input("Enter client acceptance rate in bps: ")))
    while base_state:
        data_to_send = input("Enter a string send by the server: ")
        count = 0
        if buffer.check_state():
            for i in range(len(data_to_send)):
                if i < client.rate:
                    client.data.append(data_to_send[i])
                else:
                    if count < buffer.buffer_size:
                        buffer.buffer.append(data_to_send[i])
                        count = len(buffer.buffer)
                    else:
                        print("Data loss" + data_to_send[i])
        else:
            j = 0
            for i in range(len(data_to_send) + len(buffer.buffer)):
                if i < client.rate:
                    if len(buffer.buffer):
                        client.data.append(buffer.buffer[0])
                        del buffer.buffer[0]
                    else:
                        client.data.append(data_to_send[j])
                        j += 1
                else:
                    if len(buffer.buffer) <= buffer.buffer_size:
                        if j < len(data_to_send):
                            buffer.buffer.append(data_to_send[j])
                            j += 1
                    else:
                        if j < len(data_to_send):
                            print(f"Data loss: {data_to_send[j]}")
                            j += 1

        print(buffer)
        print(client)


if __name__ == '__main__':
    main()
