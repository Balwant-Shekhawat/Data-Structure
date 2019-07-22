class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    stack1 = Stack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)

    popped_item = stack1.pop()
    print("Item Poped is {} ".format(popped_item))

    isStackEmpty = stack1.isEmpty()
    print("Is Stack Empty {}".format(isStackEmpty))

    stack_len = stack1.size()
    print("Size of stack is {}".format(stack_len))