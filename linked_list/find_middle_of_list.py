class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, item):
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
            return

        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = new_node

    def print_list(self):
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.next


def find_middle(head1):
    if head1 is None:
        return None
    start = head1
    end = head1
    while end.next:
        end = end.next
        if end.next:
            end = end.next
        start = start.next
    return start


def delete_middle(head1):
    if head1 is None:
        return None

    start = head1
    end = head1
    prev = None
    while end.next:
        prev = start
        start = start.next
        end = end.next
        if end.next:
            end = end.next

    prev.next = start.next
    start = None
    return head1


if __name__ == "__main__":
    list1 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    # list1.append(4)
    # list1.append(5)
    # list1.append(6)
    # list1.append(7)

    list1.print_list()

    middle = find_middle(list1.head)

    print("The middle element of list is {}".format(middle.data))

    list2 = LinkedList()
    list2.head = delete_middle(list1.head)

    print("---------------------------")
    list2.print_list()
