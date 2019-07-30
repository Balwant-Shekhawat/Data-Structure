class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_all_ancestor(root, target):
    if root is None:
        return False
    if root.data == target:
        return True

    if(print_all_ancestor(root.left, target) or print_all_ancestor(root.right, target)):
        print(root.data)
        return True

    #return None

def print_single_ancestor(root, target):
    if root is None:
        return False

    if root.data == target:
        return True

    if (print_single_ancestor(root.left, target) or print_single_ancestor(root.right, target)):
        print(root.data)

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

    print_all_ancestor(root, 11)
    print_single_ancestor(root,11)