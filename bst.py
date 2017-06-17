# Binary Search Tree


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

    def search(self, tree, node):
        if tree:
            if node == tree.val:
                return tree
            elif node < tree.val and tree.left:
                return self.search(tree.left, node)
            elif node > tree.val and tree.right:
                return self.search(tree.right, node)
            else:
                print("Not found")

    def search_iter(self, node):
        tree = self.root
        while tree and tree.val != node:
            if node < tree.val:
                tree = tree.left
            else:
                tree = tree.right
        return tree

    def insert(self, tree, node):
        if not tree:
            self.root = node
        elif node.val < tree.val:
            if not tree.left:
                tree.left = node
                node.parent = tree
            else:
                self.insert(tree.left, node)
        else:
            if not tree.right:
                tree.right = node
                node.parent = tree
            else:
                self.insert(tree.right, node)

    def insert_iter(self, tree, node):
        y = None
        while tree:
            y = tree
            if node.val < tree.val:
                tree = tree.left
            else:
                tree = tree.right
        node.parent = y
        if not y:
            self.root = node
        elif node.val < y.val:
            y.left = node
        else:
            y.right = node

    def printbt(self, tree, level):
        if tree.right:
            self.printbt(tree.right, level + 1)
        for i in range(level):
            print("   ", end="")
        print(tree.val)
        if tree.left:
            self.printbt(tree.left, level + 1)

    def inorder(self, tree):
        if tree.left:
            self.inorder(tree.left)
        print(tree.val, end=" ")
        if tree.right:
            self.inorder(tree.right)

    def inorder_iter(self, tree):
        stk = []
        while len(stk) != 0 or tree:
            if tree:
                stk.append(tree)
                tree = tree.left
            else:
                tree = stk.pop()
                print(tree.val, end=" ")
                tree = tree.right

    def successor(self, x):
        x = self.search_iter(x)
        if x.right:
            return tree_min(x.right)
        y = x.parent
        while y and x == y.right:
            x = y
            y = y.parent
        return y

    def transplant(self, u, v):
        if not u.parent:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent

    def delete(self, z):
        if not z.left:
            self.transplant(z, z.right)
        elif not z.right:
            self.transplant(z, z.left)
        else:
            y = tree_min(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y

    def left_rotate(self, x):
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

    def right_rotate(self, x):
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


bst = BST()
node5 = Node(5)
node2 = Node(2)
nodem4 = Node(-4)
node3 = Node(3)
node12 = Node(12)
node9 = Node(9)
node21 = Node(21)
node19 = Node(19)
node25 = Node(25)
bst.insert_iter(bst.root, node5)
bst.insert_iter(bst.root, node2)
bst.insert_iter(bst.root, nodem4)
bst.insert_iter(bst.root, node3)
bst.insert(bst.root, node12)
bst.insert(bst.root, node9)
bst.insert(bst.root, node21)
bst.insert(bst.root, node19)
bst.insert(bst.root, node25)
bst.printbt(bst.root, 0)
print(bst.search_iter(24))
print(bst.successor(3).val)
bst.delete(node21)
bst.inorder(bst.root)
# bst.left_rotate(node12)
# print("")
# bst.printbt(bst.root, 0)
# print()
