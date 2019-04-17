from AVLTrees2.Node import Node
from queue import Queue


class AVLTree:
    def __init__(self):
        self.root = None

    # get the balance of the node
    def get_height(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.max(self.get_height(node.left_child), self.get_height(node.right_child))

    # Balance the tree
    def get_balance(self, node):
        if node is None:
            return 0
        left = self.get_height(node.left_child)
        right = self.get_height(node.right_child)
        return left - right

    # calculate the maximum of two numbers
    def max(self, val1, val2):
        if val1 > val2:
            return val1
        else:
            return val2

    # Calculate the magnitude of number
    def mod(self, val):
        if val < 0:
            return -val
        else:
            return val

    # left rotate the tree
    def left_rotate(self, node):
        parent = node.parent
        temp = node.right_child
        left = temp.left_child
        node.right_child = left
        if left is not None:
            left.parent = node
        temp.left_child = node
        temp.parent = node.parent
        node.parent = temp
        if parent is None:
            self.root = temp
        else:
            if temp.data < parent.data:
                parent.left_child = temp
            else:
                parent.right_child = temp
        return temp

    # right rotate the tree
    def right_rotate(self, node):

        parent = node.parent
        temp = node.left_child
        right = temp.right_child
        node.left_child = right
        if right is not None:
            right.parent = node
        temp.right_child = node
        temp.parent = node.parent
        node.parent = temp
        if parent is None:
            self.root = temp
        else:
            if temp.data < parent.data:
                parent.left_child = temp
            else:
                parent.right_child = temp
        return temp

    # inOrder traversal of the tree
    def traverse(self, root):
        if root is None:
            return
        if root.left_child is not None:
            self.traverse(root.left_child)
        print(root.data)
        if root.right_child is not None:
            self.traverse(root.right_child)

    # insert multiple
    def insert_many(self, args=[]):
        for val in args:
            self.insert(val, self.root)

    # insert node into tree
    def insert(self, data, root):
        if self.root is None:
            self.root = Node(data)
            return
        node = Node(data)
        temp = root
        temp_parent = temp
        while temp is not None:
            temp_parent = temp
            if data < temp.data:
                temp = temp.left_child
            elif data >= temp.data:
                temp = temp.right_child
        if data < temp_parent.data:
            temp_parent.left_child = node
        else:
            temp_parent.right_child = node
        node.parent = temp_parent
        # go from the inserted node towards the root and check if the tree is unbalanced at any node
        temp = node

        balance = 0
        while temp is not None:
            balance = self.mod(self.get_balance(temp))
            if balance > 1:
                break
            temp = temp.parent
        if balance < 2:
            return
            # calculate first two moves
        first_move = False
        second_move = False
        temp_parent = temp
        if data < temp.data:
            first_move = False
            temp = temp.left_child
        else:
            first_move = True
            temp = temp.right_child
        if data < temp.data:
            second_move = False
        else:
            second_move = True
        parent = temp_parent.parent
        # check for the appropriate rotation like LL,RR,RL,LR
        if first_move is True and second_move is True:
            self.left_rotate(temp_parent)
        elif first_move is False and second_move is False:
            self.right_rotate(temp_parent)
        elif first_move is True and second_move is False:
            self.right_rotate(temp_parent.right_child)
            self.left_rotate(temp_parent)
        else:
            self.left_rotate(temp_parent.left_child)
            self.right_rotate(temp_parent)

    # Level order traversal of a tree
    def levelordertraversal(self, rootnode):
        if rootnode is None:
            return
        else:
            q = Queue(maxsize=0)
            l = []
            q.put(rootnode)
            while q.empty() is False:
                temp = q.get()
                l.append(temp.data)
                print(f'{temp.data:5} ==> {self.get_balance(temp):5}')
                if temp.left_child is not None:
                    q.put(temp.left_child)
                if temp.right_child is not None:
                    q.put(temp.right_child)
            return l
