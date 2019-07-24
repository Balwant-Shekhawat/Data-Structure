# In Case of Tree DFS Means Pre,Post,Inorder Traversal
# These order works with Binary Tree only
# DFS For Graph is different
class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None


def preorder_traversal(root):
    if root is None:
        print("Empty Condition")
        return None

    print(root.data)
    preorder_traversal(root.left)
    preorder_traversal(root.right)


def inorder_traversal(root):
    if root is None:
        return None
    inorder_traversal(root.left)
    print(root.data)
    inorder_traversal(root.right)


def postorder_traversal(root):
    if root is None:
        return None
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data)


if __name__ == "__main__":
    tree1 = BinaryTree()
    tree1.root = Node(1)
    tree1.root.left = Node(2)
    tree1.root.right = Node(3)
    tree1.root.left.left = Node(4)

    print("**********Preorder Traversal************** ")
    preorder_traversal(tree1.root)

    print("**********Inorder Traversal************** ")
    inorder_traversal(tree1.root)

    print("**********Postorder Traversal************** ")
    postorder_traversal(tree1.root)