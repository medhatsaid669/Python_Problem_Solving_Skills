class MyPair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return f'({self.first}, {self.second})'

    def __lt__(self, other):
        if not isinstance(other, MyPair):
            return NotImplementedError

        return (self.first, self.second) < (other.first, other.second)


if __name__ == '__main__':
    p1 = MyPair(5, 10)
    print(p1 < 50)




