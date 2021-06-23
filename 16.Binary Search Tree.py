class BST:
    def __init__(self, key):
        self.key = key
        self.LeftChild = None
        self.RightChild = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:  # for duplicate values to be ignored. You can write for Left and Right Child
            return

        if data > self.key:
            if self.RightChild:  # If Right Child is not None, meaning if Right Child has Node
                self.RightChild.insert(data)
            else:
                self.RightChild = BST(data)
        else:
            if self.LeftChild:
                self.LeftChild.insert(data)
            else:
                self.LeftChild = BST(data)

    def search(self, data):
        if data == self.key:
            print('Node is found')
            return
        if data > self.key:
            if self.RightChild:
                self.RightChild.search(data)
            else:
                print('Node is not presented in Tree')
        else:
            if self.LeftChild:
                self.LeftChild.search(data)
            else:
                print('Node is not presented in Tree')

    def preorder(self):  # Print Root, Left Child, Right Child
        print(self.key, end=' ')
        if self.LeftChild:
            self.LeftChild.preorder()
        if self.RightChild:
            self.RightChild.preorder()

    def inorder(self):  # Print Left Child, Root, Right Child
        if self.LeftChild:
            self.LeftChild.inorder()
        print(self.key, end=' ')
        if self.RightChild:
            self.RightChild.inorder()

    def postorder(self):  # Print Left Child, Right Child, Root
        if self.LeftChild:
            self.LeftChild.postorder()
        if self.RightChild:
            self.RightChild.postorder()
        print(self.key, end=' ')

    def min_node(self):
        current = self.key
        while self.LeftChild:
            current = current.Leftchild
        print('The smallest value of the tree is: ', current.key)

    def max_node(self):
        current = self.key
        while self.RightChild:
            current = current.RightChild
        print('The greatest value of the tree is: ', current.key)

    def delete(self, data):
        if self.key is None:
            print('Tree is empty')
            return

        if data < self.key:
            if self.LeftChild:
                self.LeftChild = self.LeftChild.delete(data)
            else:
                print('Given Node is not present in Tree')

        elif data > self.key:
            if self.RightChild:
                self.RightChild = self.RightChild.delete(data)
            else:
                print('Given Node is not present in Tree')

        else:
            if self.LeftChild is None:
                temp = self.RightChild
                self = None
                return temp
            if self.RightChild is None:
                temp = self.LeftChild
                self = None
                return temp
            node = self.RightChild
            while node.LeftChild:
                node = node.LeftChild
            self.key = node.key
            self.RightChild = self.RightChild.delete(node.key)
        return self


root = BST(10)
L1 = [6, 3, 1, 6, 98, 3, 7]
for i in L1:
    root.insert(i)
root.search(3)

root.preorder()
print()
root.inorder()
print()
root.postorder()
print()
root.delete(60)
root.postorder()
