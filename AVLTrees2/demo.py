from AVLTrees2.Tree import AVLTree

tree=AVLTree()
tree.insert(21,tree.root)
tree.insert_many([26,30,9,4,14,28,18,15,10,2,3,7])
print(tree.levelordertraversal(tree.root))
print("Tree root :",tree.root.data)