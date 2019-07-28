# Iterative Python program to find the nodes at k distance from the root

# A Binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.nextRight = None


def connect(root):
    if root is None:
        return None

    k = 1
    queue = []
    queue.append(root)
    queue.append(None)
    while len(queue) != 0:
        item = queue.pop(0)
        if item is None:
            k = k + 1
            for i in range(len(queue)):
                if i > 0 and queue[i] is not None:
                    queue[i-1].nextRight = queue[i]
            if len(queue) > 0 and queue[len(queue)-1] is not None:
                queue.append(None)
                continue
            else:
                return None

        else:
            if item.left is not None:
                queue.append(item.left)
            if item.right is not None:
                queue.append(item.right)

def traverse_tree(root):
    if root is None:
        return None
    if root.nextRight:
        print("nextRight of", root.data,"is", root.nextRight.data)
    else:
        print("nextRight of", root.data, "is", -1)
    traverse_tree(root.left)
    traverse_tree(root.right)
# Driver program to test the above function
"""
Constructed binary tree is 
              10 
            /   \ 
          8      2 
        /         \ 
      3            90 
"""
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.right.right.left = Node(10)
root.right.right.right = Node(11)

connect(root)
traverse_tree(root)



# This code is contributed by Balwant Singh(Balwant1707)
