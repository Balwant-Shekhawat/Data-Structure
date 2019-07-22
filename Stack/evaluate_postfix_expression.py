class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        return None

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        return None

    def print(self):
        for item in self.items:
            print(item)


def evaluate_postfix_expression(exp):
    """Rules:
    1) If item is Operand push it into stack
    2) If item is unary operator, pop single item from stack, else
        if item is binary operator pop 2 elements from the stack
        and perform calculation on it and push back the result back into the stack
    3) In the end we will have only 1 item in stack, which is our result than just print peek element
    """

    stack1 = Stack()
    for item in exp:
        if item.isalnum():
            stack1.push(item)
        else:
            elem1 = stack1.pop()
            elem2 = stack1.pop()
            # Second operand will be put before while evaluating
            result = str(eval(elem2 + item + elem1))
            stack1.push(result)

    return stack1.peek()


if __name__ == "__main__":
    exp1 = '123*+5-'
    result1 = evaluate_postfix_expression(exp1)
    print("Postfix evaluation of {} is {}".format(exp1, result1))
