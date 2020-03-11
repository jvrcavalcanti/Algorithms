class Binary(object):
    def __init__(self, data):
        self.data = data

    def to_decimal(self):
        reverse = self.data[::-1]
        pot = 0
        sum = 0
        for bit in reverse:
            sum += int(bit) * (2 ** pot)
            pot += 1
        return sum


if __name__ == "__main__":
    bi = Binary("101010")
    print(bi.to_decimal())