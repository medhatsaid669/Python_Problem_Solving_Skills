class Hello:
    def __init__(self):
        self.counter = 1234


class Hack:
    pass


if __name__ == '__main__':
    h = Hack()
    Hello.__init__(h)
    print(h.counter)





















