class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


order = {}
def vertical_traversal(root, level):
    if root is None:
        return None
    if level not in order:
        order[level] = []

    order[level].append(root.data)

    if root.left is not None:
        vertical_traversal(root.left, level + 1)
    if root.right is not None:
        vertical_traversal(root.right, level - 1)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.left = Node(10)
    root.right.right.right = Node(9)
    root.right.right.left.right = Node(11)
    root.right.right.left.right.right = Node(12)

    vertical_traversal(root, 0)
    print("List is {}".format(order))