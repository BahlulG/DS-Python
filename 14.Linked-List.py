class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print('LL is empty')
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, '-->', end=' ')
                temp = temp.next

    def add_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def add_after_node(self, data, x):
        temp = self.head
        while temp is not None and temp.data is not x:
            temp = temp.next
        if temp is None:
            print('Node is not presented in LL', '\n')
        else:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node

    def add_before_node(self, data, x):
        if self.head is None:
            print('Node is not presented in LL', '\n')
        elif self.head.data is x:
            self.add_begin(data)

        temp = self.head
        while temp.next is not None and temp.next.data is not x:
            temp = temp.next
        if temp.next is None:
            print('Node is not presented in LL', '\n')
        else:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node

    def del_head(self):
        if self.head is None:
            print('LL is empty')
        else:
            self.head = self.head.next

    def del_end(self):
        temp = self.head
        if temp is None:
            print('LL is empty')
        elif temp.next is None:
            print('This is head of LL, use "del_head" function')
        else:
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def del_by_val(self, x):
        temp = self.head
        if temp is None:
            print('LL is empty')
        elif temp.data is x:
            self.head = temp.next
        else:
            while temp.next is not None and temp.next.data is not x:
                temp = temp.next
            if temp.next is not None:
                temp.next = temp.next.next
            else:
                print('Node is not presented in LL', '\n')


LL = LinkedList()
LL.add_begin(10)
LL.add_end(40)
LL.add_after_node(123, 40)
LL.add_end(50)
LL.add_end(44)
LL.del_by_val(10)
# LL.del_end()
LL.print_LL()
