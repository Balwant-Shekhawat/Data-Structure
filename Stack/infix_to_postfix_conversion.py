class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        if item is not None:
            self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop(len(self.items) - 1)

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]

    def print(self):
        if len(self.items) is None:
            return None

        for item in self.items:
            print(item)

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

def infix_to_postfix(exp):
    # Rules:
    # 1) if item is operand, print it.
    # 2) if item is ")" Pop and print items from stack until a "(" paranthesis is popped(But do not print "(")
    # 3) else, Pop and print items until one of lower priority than item is encountered or a
    # "(" is encountered or the stack is empty, Push item
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    output = ""
    stack1 = Stack()
    for item in exp:
        if item.isalnum():
            output = output + item
        elif item == ")":
            popped_item = stack1.pop()
            while popped_item != "(":
                output = output + popped_item
                if not stack1.isEmpty():
                    popped_item = stack1.pop()
                else:
                    break

        elif item == "(":
            stack1.push(item)
        else:
            top_element = stack1.peek()

            while not stack1.isEmpty() and top_element in precedence and item in precedence and precedence[item] <= precedence[top_element]:
                output = output + stack1.pop()
                top_element = stack1.peek()
            stack1.push(item)

    while not stack1.isEmpty():
         output = output + stack1.pop()
    return output


if __name__ == "__main__":

    exp1 = 'A*B-(C+D)+E'
    postfix1 = infix_to_postfix(exp1)
    print("PostFix of {} is {}".format(exp1, postfix1))

    exp2 = '(A+B)*C-(D-E)*(F+G)'
    postfix2 = infix_to_postfix(exp2)
    print("PostFix of {} is {}".format(exp2, postfix2))

    exp3 = 'a+b*(c^d-e)^(f+g*h)-i'
    postfix3 = infix_to_postfix(exp3)
    print("PostFix of {} is {}".format(exp3, postfix3))