from BinaryTress.Node import Node
from queue import Queue


class Tree:

    def __init__(self):
        self.root = None
        self.size = 0

    #initialize the tree
    def seed(self, rootvalue):
        if self.root is None:
            self.root=Node(rootvalue)
            return True
        else:
            return False

    #insert nodes to tree
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.insert(data)
        self.size += 1

    def traverse(self):
        if self.root.data is None:
            return
        else:
            self.root.inorder()

    def getmin(self, onlydata=False):
        node = self.root.getmin()
        if node is not None and onlydata is True:
            return node.data
        else:
            return node

    def getmax(self, onlydata=False):
        node = self.root.getmax()
        if node is not None and onlydata is True:
            return node.data
        else:
            return node

    def delete(self, data):
        status = self.root.remove(data, self.root)
        if status:
            self.size -= 1

    # Computes the number of nodes in tree
    @staticmethod
    def size(rootnode):
        if rootnode is None:
            return 0
        else:
            return Tree.size(rootnode.leftChild) + 1 + Tree.size(rootnode.rightChild)

    # Computes the maximum depth of tree
    @staticmethod
    def maxdepth(rootnode):
        if rootnode is None:
            return 0
        else:
            return max(Tree.maxdepth(rootnode.leftChild), Tree.maxdepth(rootnode.rightChild)) + 1

    # maximumof two numbers
    @staticmethod
    def max(num1, num2):
        if num1 < num2:
            return num2
        else:
            return num1

    # Remove Tree
    def erasetree(self):
        """ This function traverses tree in post order to
                    to delete each and every node of the tree """
        Tree._deletetree(self.root)
        self.root = None

    # Delte the Tree
    def _deletetree(rootnode):
        """ This function traverses tree in post order to
            to delete each and every node of the tree """
        if rootnode is None:
            return
        Tree._deletetree(rootnode.leftChild)
        Tree._deletetree(rootnode.rightChild)
        """ then delete the node """
        rootnode.leftChild = None
        rootnode.rightChild = None
        rootnode.data = None

    # Level order traversal of a tree
    @staticmethod
    def levelordertraversal(rootnode):
        if rootnode is None:
            return
        else:
            q = Queue(maxsize=0)
            l = []
            q.put(rootnode)
            while q.empty() is False:
                temp = q.get()
                l.append(temp.data)
                if temp.leftChild is not None:
                    q.put(temp.leftChild)
                if temp.rightChild is not None:
                    q.put(temp.rightChild)
            return l

    # calculate number of leaf nodes
    @staticmethod
    def leafcount(rootnode):
        if rootnode is None:
            return
        temp = rootnode
        left, right = 0, 0
        if temp.leftChild is None and temp.rightChild is None:
            return 1
        else:
            if temp.leftChild is not None:
                left = Tree.leafcount(temp.leftChild)
            if temp.rightChild is not None:
                right = Tree.leafcount(temp.rightChild)
        return left + right

    # swap the two adjacent leaf pair
    @staticmethod
    def swapleafpair(rootnode):
        if rootnode is None:
            return
        temp = rootnode
        q = Queue(maxsize=0)
        leaf = None
        q.put(temp)
        while q.empty() is False:
            temp = q.get()

            if temp.leftChild is None and temp.rightChild is None:
                if leaf is None:
                    leaf = temp
                else:
                    leaf.data, temp.data = temp.data, leaf.data
                    leaf = None
            if temp.leftChild is not None:
                q.put(temp.leftChild)
            if temp.rightChild is not None:
                q.put(temp.rightChild)

    # print only leaf nodes
    @staticmethod
    def getleafs(rootnode):
        if rootnode is None:
            return
        temp = rootnode
        q = Queue(maxsize=0)
        leafs = []
        q.put(temp)
        while q.empty() is False:
            temp = q.get()
            if temp.leftChild is None and temp.rightChild is None:
                leafs.append(temp.data)
            if temp.leftChild is not None:
                q.put(temp.leftChild)
            if temp.rightChild is not None:
                q.put(temp.rightChild)
        return leafs

    # function to return inorder successor
    @staticmethod
    def inordersuccessor(data, rootnode):
        successor = None
        node = Tree.search(rootnode, data)
        if rootnode is None or node is None:
            return successor
        temp = rootnode
        if node.rightChild is not None:
            successor = node.rightChild.getmin()
            return successor
        while temp is not None:
            if node.data < temp.data:
                successor = temp
                temp = temp.leftChild
            elif node.data > temp.data:
                temp = temp.rightChild
            else:
                break
        return successor

    # function to return inorder predecessor
    @staticmethod
    def inorderpredecessor(data, rootnode):
        node = Tree.search(rootnode, data)
        if rootnode is None or node is None:
            return None
        predecessor = None
        if node.leftChild is not None:
            predecessor = node.leftChild.getmax(False)
        temp = rootnode
        while temp is not None:
            if node.data > temp.data:
                predecessor = temp
                temp = temp.rightChild
            elif node.data < temp.data:
                temp = temp.leftChild
            else:
                break
        return predecessor

    # function to return the node with data
    @staticmethod
    def search(rootnode, data):
        node = None
        while rootnode is not None:
            if rootnode.data == data:
                node = rootnode
                break
            else:
                if data < rootnode.data:
                    rootnode = rootnode.leftChild
                else:
                    rootnode = rootnode.rightChild
        return node
