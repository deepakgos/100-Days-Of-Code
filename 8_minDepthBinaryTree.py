class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

def minDepth(node):
    if (node == None):
        return 0
    else:
        lDepth = minDepth(node.left)
        rDepth = minDepth(node.right)

        if lDepth < rDepth:
            return lDepth + 1
        else:
            return rDepth + 1
        
node = Node(1)
node.left = Node(2)
node.left.left = Node(4)
node.left.left.right = Node(7)
node.left.right = Node(5)

node.right = Node(3)
node.right.right = Node(6)

print("Min depth of Binary Tree is :", minDepth(node))
