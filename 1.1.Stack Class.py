class STACK:
    def __init__(self):
        self.name = []

    def push(self, item):
        self.name.append(item)

    def peek(self):
        return self.name[-1]

    def pop(self):
        return self.name.pop()

    def isEmpty(self):
        return len(self.name) == 0

    def size(self):
        return len(self.name)

    def itself(self):
        print(self.name)


def divideBy2(num):
    s = STACK()
    while num > 0:
        s.push(num % 2)
        num = num // 2
    s.itself()

    new_string = ''
    while not s.isEmpty():
        new_string += str(s.pop())
    print(new_string)


divideBy2(233)
