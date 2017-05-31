# AVL


class Node():

    def __init__(self, i):
        self.val = i
        self.parent = None
        self.left = None
        self.right = None
        self.bf = 0

    def is_left_child(self):
        return self.parent.left == self

    def is_right_child(self):
        return self.parent.right == self


def tree_min(tree):
    while tree.left:
        tree = tree.left
    return tree


def tree_max(tree):
    while tree.right:
        tree = tree.right
    return tree


class AVL():

    def __init__(self):
        self.root = None

    def printbt(self, tree, level):
        if tree.right:
            self.printbt(tree.right, level + 1)
        for i in range(level):
            print("   ", end="")
        print(tree.val)
        if tree.left:
            self.printbt(tree.left, level + 1)

    def avl_insert(self, tree, n):
        if not self.root:
            self.root = n
        elif n.val < tree.val:
            if not tree.left:
                tree.left = n
                n.parent = tree
                self.avl_updatebf(n)
            else:
                self.avl_insert(tree.left, n)
        else:
            if not tree.right:
                tree.right = n
                n.parent = tree
                self.avl_updatebf(n)
            else:
                self.avl_insert(tree.right, n)

    def avl_updatebf(self, n):
        if 1 < n.bf or n.bf < -1:
            self.avl_rebalance(n)
        elif n.parent:
            if n.is_left_child():
                n.parent.bf += 1
            elif n.is_right_child():
                n.parent.bf -= 1
            if n.parent.bf != 0:
                self.avl_updatebf(n.parent)

    def avl_rebalance(self, n):
        if n.bf < 0:
            if n.right.bf > 0:
                self.rotate_right(n.right)
                self.rotate_left(n)
            else:
                self.rotate_left(n)
        elif n.bf > 0:
            if n.left.bf < 0:
                self.rotate_left(n.left)
                self.rotate_right(n)
            else:
                self.rotate_right(n)

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        x.bf = x.bf + 1 - min(y.bf, 0)
        y.bf = y.bf + 1 - max(x.bf, 0)

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not y.parent:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y
        x.bf = x.bf - 1 - max(y.bf, 0)
        y.bf = y.bf - 1 - min(x.bf, 0)

avl = AVL()
avl.avl_insert(avl.root, Node(5))
avl.avl_insert(avl.root, Node(2))
avl.avl_insert(avl.root, Node(-4))
avl.avl_insert(avl.root, Node(3))
avl.avl_insert(avl.root, Node(12))
avl.avl_insert(avl.root, Node(9))
avl.avl_insert(avl.root, Node(21))
avl.avl_insert(avl.root, Node(19))
avl.avl_insert(avl.root, Node(25))
avl.printbt(avl.root, 0)
