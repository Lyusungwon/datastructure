# practice


class Node():

    def __init__(self, i):
        self.val = i
        self.parent = None
        self.left = None
        self.right = None


def tree_min(tree):
    while tree.left:
        tree = tree.left
    return tree


def tree_max(tree):
    while tree.right:
        tree = tree.right
    return tree


class BST():

    def __init__(self):
        self.root = None

    def insert(self, tree, node):

    def printbt(self, tree, level):
        if tree.right:
            self.printbt(tree.right, level + 1)
        for i in range(level):
            print(" ", end="")
        print(tree.val)
        if tree.left:
            self.printbt(tree.left, level + 1)

    def inorder(self, tree):
        self.inorder(tree.left)
        print(tree.val, end=" ")
        self.inorder(tree.right)

    def inorder_iter(self, tree):

    def transplant(self, u, v):

    def delete(self, z):

    def left_rotate(self, z):

        # bst = BST()
        # node5 = Node(5)
        # node2 = Node(2)
        # nodem4 = Node(-4)
        # node3 = Node(3)
        # node12 = Node(12)
        # node9 = Node(9)
        # node21 = Node(21)
        # node19 = Node(19)
        # node25 = Node(25)
        # bst.insert(bst.root, node5)
        # bst.insert(bst.root, node2)
        # bst.insert(bst.root, nodem4)
        # bst.insert(bst.root, node3)
        # bst.insert(bst.root, node12)
        # bst.insert(bst.root, node9)
        # bst.insert(bst.root, node21)
        # bst.insert(bst.root, node19)
        # bst.insert(bst.root, node25)
        # bst.printbt(bst.root, 0)
        # bst.inorder_iter(bst.root)
        # print()
