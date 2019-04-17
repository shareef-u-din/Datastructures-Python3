class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if data < self.data:
            if not self.leftChild:
                self.leftChild = Node(data)
            else:
                self.leftChild.insert(data)
        else:
            if not self.rightChild:
                self.rightChild = Node(data)
            else:
                self.rightChild.insert(data)

    def inorder(self):
        if self is None:
            return
        if self.leftChild is not None:
            self.leftChild.inorder()
        print(self.data)
        if self.rightChild is not None:
            self.rightChild.inorder()

    def getmin(self,onlydata=True):
        while self.leftChild is not None:
            self = self.leftChild
        return self


    def getmax(self):
        while self.rightChild is not None:
            self = self.rightChild
        return self

    def remove(self, data, parent):
        """find node to remove"""
        while self and self.data != data:
            parent = self
            if data < self.data:
                self = self.leftChild
            if data > self.data:
                self = self.rightChild

        # if data not found
        if self is None or self.data != data:
            return False
        # if node is a leaf
        elif self.leftChild is None and self.rightChild is None:
            if data < parent.data:
                parent.leftChild = None
            else:
                parent.rightChild = None
            del self
            return True
        # if it has left children
        elif self.leftChild is not None and self.rightChild is None:
            if data < parent.data:
                parent.leftChild = self.leftChild
            else:
                parent.rightChild = self.leftChild
            return True
        # if it has right children
        elif self.rightChild is not None and self.leftChild is None:
            if data < parent.data:
                parent.leftChild = self.rightChild
            else:
                parent.rightChild = self.rightChild
            return True
        # if it has both the children
        else:
            self.data = self.rightChild.getmin()
            self.rightChild.remove(self.data, self)
