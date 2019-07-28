class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None


def print_node_at_k_dist_from_root(root, distance):
    if root is None:
        return None

    if distance == 0:
        return [root.data]
    k = 0
    queue = []
    queue.append(root)
    queue.append(None)
    while len(queue) != 0:
        item = queue.pop(0)
        if item is None:
            k = k + 1
            if k == distance:
                return [elem.data for elem in queue if elem is not None]
            queue.append(None)
            continue
        else:
            if item.left is not None:
                queue.append(item.left)
            if item.right is not None:
                queue.append(item.right)


if __name__ == "__main__":
    #t1 = BinaryTree()
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.right.right = Node(90)

    result = print_node_at_k_dist_from_root(root, 2)
    print(','.join([str(i) for i in result]))