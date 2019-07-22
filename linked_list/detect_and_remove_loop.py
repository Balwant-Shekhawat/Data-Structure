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
            return self.head

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        return self.head

    def print_list(self):
        if self.head is None:
            return None

        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


def detect_and_remove_loop(head1):
    if head1 is None:
        return False

    slow_ptr = head1
    fast_ptr = head1
    loop_exist = False
    while fast_ptr.next:
        fast_ptr = fast_ptr.next
        if fast_ptr.next:
            fast_ptr = fast_ptr.next
        slow_ptr = slow_ptr.next
        if slow_ptr == fast_ptr:
            loop_exist = True
            break
    if loop_exist:
        # Code to detect start of loop
        slow_ptr = head1
        prev_ptr = fast_ptr
        while slow_ptr != fast_ptr:
            slow_ptr = slow_ptr.next
            prev_ptr = fast_ptr
            fast_ptr = fast_ptr.next
        print("Loop Start From Node {}".format(prev_ptr.next.data))
        prev_ptr.next = None
    else:
        print("No Loop Exist")
        return False


if __name__ == "__main__":
    list1 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list1.append(4)
    list1.append(5)
    list1.append(6)
    list1.append(7)

    print(list1.head.next.next.next.next.next.next.data)
    print(list1.head.next.next.next.data)
    # Create a loop for testing
    list1.head.next.next.next.next.next.next.next = list1.head.next.next.next

    detect_and_remove_loop(list1.head)
    list1.print_list()
