class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

def max_height_binary_tree(node):
    if (node == None):
        return 0
    else:
        lDepth = max_height_binary_tree(node.left) #1
        rDepth = max_height_binary_tree(node.right) #2

        if lDepth > rDepth: #3
            return (1 + lDepth)
        else:
            return (1 + rDepth)

node = Node(1)
node.left = Node(2)
node.left.left = Node(4)
node.left.left.right = Node(7)
node.left.right = Node(5)

node.right = Node(3)
node.right.right = Node(6)

print("Max height of Binary Tree is :", max_height_binary_tree(node))

# max height of binary tree is 1 + number of edges in the longest path or the total number of nodes in the longest path