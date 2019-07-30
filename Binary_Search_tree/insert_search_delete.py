class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


def insert(root, item):
    new_node = Node(item)
    if root is None:

        root = new_node
        return None
    elif root.data > item:
        if root.left is None:
            root.left = new_node
        else:
            insert(root.left, item)
    elif root.data < item:
        if root.right is None:
            root.right = new_node
        else:
            insert(root.right, item)

def inorder(root):
    if root is None:
        return None
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def search(root, item):
    if root is None:
        return False
    if root.data == item:
        return True
    if item < root.data:
        res = search(root.left, item)
    else:
        res = search(root.right, item)
    return res


def delete(root, item, parent=None):
    if root is None:
        return None

    if root.data > item:
        delete(root.left, item, root)
    elif root.data < item:
        delete(root.right, item, root)
    else:
        if root.left is not None and root.right is not None:
            # Delete a node having 2 child
            successor = root.right
            while successor.left:
                successor = successor.left
            root.data = successor.data
            delete(root.right, successor.data, root)

        elif root.left is not None or root.right is not None:
            # Delete a node having 1 child
            child = root.left if root.left else root.right
            root.data = child.data
            delete(child, child.data, root)
        else:
            # Delete a node having no child
            if parent:
                if parent.left.data == item:
                    parent.left = None
                if parent.right.data == item:
                    parent.right = None
                return None
            else:
                root = None
                return False

if __name__ == "__main__":
    r = Node(50)
    insert(r, 30)
    insert(r, 20)
    insert(r, 40)
    insert(r, 70)
    insert(r, 60)
    insert(r, 80)

    inorder(r)

    res = search(r, 40)
    if res:
        print("Item Found")
    else:
        print("Not Found")

    delete(r, 50)
    inorder(r)