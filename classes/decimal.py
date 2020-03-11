class Decimal(object):
    def __init__(self, data):
        self.data = data

    def to_binary(self):
        result = ""
        num = self.data
        while num > 0:
            result += str(num % 2)
            num = num // 2
        return result[::-1]



if __name__ == "__main__":
    de = Decimal(42)
    print(de.to_binary())