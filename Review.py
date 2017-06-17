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


class Node():

    def __init__(self, i):
        self.val = i
        self.left = None
        self.right = None


class BST():

    def __init__(self):
        self.root = None

    def search(self, tree, node):
        if tree:
            if node < tree.val:
                return self.search(tree.left, node)
            elif node > tree.val:
                return self.search(tree.right, node)
            elif node == tree.val:
                return tree
            else:
                print("Not Found")

    def search_iter(self, node):
        tree = self.root
        if tree:
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
            print("  ", end=" ")
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
                print(tree, end=" ")
                tree = tree.right

    def successor(self, x):
        tree = self.search_iter(x)
        if x.right:
            return tree_min(x.right)
        y = x.parent
        while y and y.right == x:
            x = y
            y = y.parent
        return y

    def transplant(self, u, v):
        if not u.parent:
            self.root = v
        elif not u.left:
            u.parent.right = v
        else:
            u.parent.left = v
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
