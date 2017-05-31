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
        if not self.root:
            self.root = node
        if node.val < tree.val:
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
                self.inset(tree.right, node)

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
        stk = []
        if len(stk) == 0 or tree:
            if tree:
                stk.append(tree)
                tree = tree.left
            else:
                tree = stk.pop()
                print(tree.val, end=" ")
                tree = tree.right

    def transplant(self, u, v):
        if not u.parent:
            self.root = v
        elif u.parent.left == u:
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
                z.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            z.left.parent = y

    def left_rotate(self, z):
        y = z.right
        z.right = y.left
        if y.left:
            y.left.parent = z
        if not z.parent:
            self.root = y
        elif z.parent.right == z:

            #(a)
print('(a)')
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
bst.insert(bst.root, node5)
bst.insert(bst.root, node2)
bst.insert(bst.root, nodem4)
bst.insert(bst.root, node3)
bst.insert(bst.root, node12)
bst.insert(bst.root, node9)
bst.insert(bst.root, node21)
bst.insert(bst.root, node19)
bst.insert(bst.root, node25)
bst.printbt(bst.root, 0)
bst.inorder_iter(bst.root)
print()
