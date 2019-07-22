class StackNode:
    def __init__(self, item):
        self.item = item
        self.next = None


class StackList:
    def __init__(self):
        self.head = None

    def push(self, item):
        new_node = StackNode(item)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def print_stack(self):
        if self.head is None:
            return None

        tmp = self.head
        while tmp:
            print(tmp.item)
            tmp = tmp.next

    def pop(self):
        if self.head is None:
            return None

        tmp = self.head
        self.head = tmp.next
        tmp.next = None
        return tmp.item

    def isEmpty(self):
        return self.head is None

    def size(self):
        if self.head is None:
            return 0

        count = 0
        tmp = self.head
        while tmp:
            count = count + 1
            tmp = tmp.next
        return count

    def peek(self):
        if self.head is None:
            return None

        return self.head.item


if __name__ == "__main__":
    stack1 = StackList()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)

    stack1.print_stack()

    popped_element = stack1.pop()
    print("Popped Element is {}".format(popped_element))

    isStackEmpty = stack1.isEmpty()
    print("Is Stack empty {}".format(isStackEmpty))

    sizeOfStack = stack1.size()
    print("Length of stack is {}".format(sizeOfStack))

    peekElement = stack1.peek()
    print("Top element on stack is {}".format(peekElement))