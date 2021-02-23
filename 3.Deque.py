class DEQUE:
    def __init__(self):
        self.name = []

    def addFront(self, item):
        self.name.append(item)

    def addRear(self, item):
        self.name.insert(0, item)

    def removeFront(self):
        return self.name.pop()

    def removeRear(self):
        return self.name.pop(0)

    def isEmpty(self):
        return len(self.name) == 0

    def size(self):
        return len(self.name)


def palindrome(word):
    d = DEQUE()
    for i in word:
        d.addRear(i)
    stillEqual = True
    while d.size() > 1 and stillEqual:
        first = d.removeRear()
        last = d.removeFront()
        if first != last:
            stillEqual = False
        return stillEqual


print(palindrome("radar"))
