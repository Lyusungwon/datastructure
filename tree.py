# Tree


class TreeNode:

    def __init__(self):
        self.val = 0
        self.children = None
        self.next = None

    def addChild(self, child):
        if self.children:
            child.next = self.children
            self.children = child
        else:
            self.children = child


def printTree(tree, level):
    node = tree
    while node:
        for i in range(level):
            print("   ", end="")
        print(node.val)
        printTree(node.children, level + 1)
        node = node.next


def heightTree(tree):
    child = tree.children
    height = 0
    while child:
        if height < heightTree(child):
            height = heightTree(child)
        child = child.next
    return height + 1


# node = TreeNode()
# print(node.val)
# child = TreeNode()
# child1 = TreeNode()
# child2 = TreeNode()
# child3 = TreeNode()
# node.addChild(child)
# node.addChild(child1)
# node.addChild(child2)
# child1.addChild(child3)
# printTree(node, 1)
# print(heightTree(node))
