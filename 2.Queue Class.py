class QUEUE:
    def __init__(self):
        self.name = []

    def enqueue(self, item):
        self.name.insert(0, item)

    def dequeue(self):
        return self.name.pop()

    def isEmpty(self):
        return len(self.name) == 0

    def size(self):
        return len(self.name)


def hotPotato(namelist, num):
    name_queue = QUEUE()

    for name in namelist:
        name_queue.enqueue(name)

    while name_queue.size() > 1:
        for _ in range(num):
            name_queue.enqueue(name_queue.dequeue())

        name_queue.dequeue()

    print(name_queue.dequeue())


hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7)
