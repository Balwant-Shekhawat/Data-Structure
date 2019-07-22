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
        if self.head is None:
            return None
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.next


def nth_node_from_the_end(head1, n):
    if head1 is None:
        return None

    slow_ptr = head1
    fast_ptr = head1
    counter = 1
    while fast_ptr.next:
        if counter != n:
            fast_ptr = fast_ptr.next
            counter = counter + 1
            continue

        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next


    print("{}th node from the end is {}".format(n, slow_ptr.data))





if __name__ == "__main__":
    list1 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list1.append(4)
    list1.append(5)
    list1.append(6)
    list1.append(7)
    list1.append(8)
    list1.append(9)
    list1.append(10)

    list1.print_list()
    nth_node_from_the_end(list1.head, 1)
    nth_node_from_the_end(list1.head, 4)
    nth_node_from_the_end(list1.head, 6)
