class Node:

    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = None  # pointer to parent node in tree
        self.balance = 0  # balance of node in tree (max dist. to leaf) NEW FOR AVL
