class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None


def create_tree(preorder, inorder):
    if len(preorder) == 0 or len(inorder) == 0:
        return None
    #current_elem = 0;
    current_elem = preorder.pop(0)
    print("Current Element {}, preorder = {}, inorder = {}".format(current_elem, preorder, inorder))
    #exit(0)
    new_node = Node(current_elem)
    pos = inorder.index(current_elem)
    new_node.left = create_tree(preorder, inorder[0:pos])
    new_node.right = create_tree(preorder, inorder[pos+1:])
    return new_node


def inorder_traversal(root):
    if root is None:
        return None
    inorder_traversal(root.left)
    print(root.data)
    inorder_traversal(root.right)


if __name__ == "__main__":
    preorder = "ABDECF"
    inorder = "DBEAFC"
    preorder = [item for item in preorder]
    inorder = [item for item in inorder]
    tree1 = BinaryTree()
    tree1.root = create_tree(preorder, inorder)
    inorder_traversal(tree1.root)

