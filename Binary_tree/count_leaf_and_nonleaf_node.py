class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

leaf = []
nonleaf = []
def count_leaf_and_non_leaf(root):
    if root is None:
        return None

    if root.left is None and root.right is None:
        leaf.append(root)
    else:
        nonleaf.append(root)

    count_leaf_and_non_leaf(root.left)
    count_leaf_and_non_leaf(root.right)
    return [leaf, nonleaf]


if __name__ == "__main__":
    tree1 = BinaryTree()
    tree1.root = Node(1)
    tree1.root.left = Node(2)
    tree1.root.right = Node(3)
    tree1.root.left.left = Node(4)
    tree1.root.left.right = Node(5)
    tree1.root.left.right.left = Node(6)
    tree1.root.left.right.left.right = Node(7)

    result = count_leaf_and_non_leaf(tree1.root)
    print("Total Leaf Nodes = {}, i.e {} ".format(len(result[0]), [item.data for item in result[0]]))
    print("Total Non-Leaf Nodes = {}, i.e {} ".format(len(result[1]), [item.data for item in result[1]]))


