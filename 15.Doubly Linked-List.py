class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Doubly_LinkedList:
    def __init__(self):
        self.head = None

    def print_DLL(self):
        if self.head is None:
            print('DLL is empty')
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, '-->', end=' ')
                temp = temp.next

    def print_DLL_reverse(self):
        if self.head is None:
            print('DLL is empty')
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            while temp.prev is not None:
                print(temp.data, '-->', end=' ')
                temp = temp.prev

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        temp = self.head
        if self.head is None:
            self.head = new_node
        else:
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def add_before(self, data, x):
        temp = self.head
        if temp is None:
            print('DLL is empty')
        else:
            while temp.data is not x and temp.next is not None:
                temp = temp.next
            if temp.data is not x:
                print('value not found in DLL')
            elif temp.prev is None:
                self.add_begin(data)
            else:
                new_node = Node(data)
                new_node.prev = temp.prev
                temp.prev.next = new_node
                new_node.next = temp
                temp.prev = new_node

    def add_after(self, data, x):
        temp = self.head
        if temp is None:
            print('DLL is empty')
        else:
            while temp.data is not x and temp.next is not None:
                temp = temp.next
            if temp.data is not x:
                print('value not found in DLL')
            else:
                new_node = Node(data)
                new_node.prev = temp
                new_node.next = temp.next
                temp.next = new_node

    def del_begin(self):
        temp = self.head
        if temp is None:
            print('DLL is empty')
        else:
            temp = self.head.next
            self.head = temp

    def del_end(self):
        temp = self.head
        if temp is None:
            print('DLL is empty')
        elif temp.next is None:
            self.head = None
        else:
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None

    def del_by_val(self, x):
        temp = self.head
        if temp is None:
            print('DLL is empty')
        else:
            while temp.data is not x and temp.next is not None:
                temp = temp.next
            if temp.data is not x:
                print('value not found in DLL')
            elif temp.next is None:
                temp.prev.next = None
            else:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
