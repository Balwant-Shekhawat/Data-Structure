class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None


def calc_max_width(root):
    if root is None:
        return 0
    queue = []
    max_width = 0
    queue.append(root)
    level = 1
    while len(queue) != 0:
        print("Level {}, Values in queue {}".format(level,[item.data for item in queue]))
        elem = queue.pop(0)
        if elem.left is not None:
            print("Appending Left Child {} of {}".format(elem.left.data, elem.data))
            queue.append(elem.left)
        if elem.right is not None:
            print("Appending Right Child {} of {}".format(elem.right.data, elem.data))
            queue.append(elem.right)

        if max_width < len(queue):
            max_width = len(queue)
        print("Max Width After Level {}, is {}, final Queue {}".format(level, max_width, [item.data for item in queue]))
        level = level+1

    return max_width


if __name__ == "__main__":
    t1 = BinaryTree()
    t1.root = Node(1)
    t1.root.left = Node(2)
    t1.root.right = Node(3)
    t1.root.left.left = Node(4)
    t1.root.left.right = Node(5)
    t1.root.right.right = Node(8)
    t1.root.right.right.left = Node(6)
    t1.root.right.right.right = Node(7)

    max_width = calc_max_width(t1.root)
    #print(max_width)