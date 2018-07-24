
"""Binary Tree"""

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add_node(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self.add_node(val, self.root)

    def add_node_in_tree(self, val, node):
        if(val < node.value):
            if(node.left is not None):
                self.add_node(val, node.left)
            else:
                node.left = Node(val)
        else:
            if(node.right is not None):
                self.add_node_in_tree(val, node.right)
            else:
                node.right = Node(val)

    def find(self, val):
        if(self.root is not None):
            return self.find_value(val, self.root)
        else:
            return None

    def find(self, val, node):
        if(val == node.value):
            return node
        elif(val < node.value and node.left is not None):
            self.find_value(val, node.left)
        elif(val > node.value and node.right is not None):
            self.find_value(val, node.right)

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    def printTree(self):
        if(self.root != None):
            self.printTree(self.root)

    def printTree(self, node):
        if(node != None):
            self.printTree(node.left)
            print str(node.value) + ' '
            self.printTree(node.right)

#     3
# 0     4
#   2      8
tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
print (tree.find(3)).v
print tree.find(10)
tree.deleteTree()
tree.printTree()