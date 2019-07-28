class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None


def count_nodes(root):
    if root is None:
        return 0

    count = 0
    queue = []
    queue.append(root)

    while len(queue) != 0:
        node = queue.pop(0)
        count = count + 1
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    return count

def count_nodes_recursively(root):
    if root is None:
        return 0

    return 1 + count_nodes_recursively(root.left) + count_nodes_recursively(root.right)


if __name__ == "__main__":
    tree1 = BinaryTree()
    tree1.root = Node(1)
    tree1.root.left = Node(2)
    tree1.root.right = Node(3)
    tree1.root.left.left = Node(4)
    tree1.root.left.right = Node(5)
    tree1.root.left.right.left = Node(6)

    count = count_nodes(tree1.root)
    print("Number of Node are {} ".format(count))

    count = count_nodes_recursively(tree1.root)
    print("Number of Node are {} ".format(count))