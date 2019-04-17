from BinaryTress.BinarySearchTree import Tree
from array import array

tree = Tree()
tree.seed(50)
a = array('i', [3, 70, 1, 40, 6, 4, 120])

for val in a:
    tree.insert(val)
tree.traverse()

root = tree.root
succ = Tree.inordersuccessor(70, root)
pred = Tree.inorderpredecessor(70, root)
print("Maximum Node :", tree.getmax(True))
print("Minimum Node :", tree.getmin(True))
print("The inorder predecessor : ", pred.data if pred is not None else None)
print("The inorder successor : ", succ.data if succ is not None else None)
