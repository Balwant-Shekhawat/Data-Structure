import queue
q = queue.Queue(maxsize=20)

class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None


def BFS(root):
    if root is None:
        return None

    print(root.data)
    if root.left is not None:
        q.put(root.left)

    if root.right is not None:
        q.put(root.right)

    if not q.empty():
        child_node = q.get()
        BFS(child_node)
    else:
        return None


if __name__ == "__main__":
    tree1 = BinaryTree()
    tree1.root = Node(1)
    tree1.root.left = Node(2)
    tree1.root.right = Node(3)
    tree1.root.left.right = Node(4)
    tree1.root.left.left = Node(5)

    BFS(tree1.root)