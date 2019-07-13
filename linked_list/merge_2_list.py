class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, item):
        obj = Node(item)
        if self.head is None:
            self.head = obj
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = obj

    def print_list(self):
        """Traverse the linked list"""
        temp = self.head
        # Here if write "while temp.next:" , It will iterate for n-1 times only
        while temp:
            print(temp.data)
            temp = temp.next


def merge_list_recursion(head1, head2):
    temp = None
    if head1 is None:
        return head2

    if head2 is None:
        return head1

    if head1.data <= head2.data:
        temp = head1
        temp.next = merge_list(head1.next, head2)
    else:
        temp = head2
        temp.next = merge_list(head1, head2.next)

    return temp


def merge_list(head1, head2):
    # Smallest Element
    dummy_node = Node(None)

    temp = dummy_node
    while True:
        if head1 is None:
            temp.next = head2
            return dummy_node.next

        if head2 is None:
            temp.next = head1
            return dummy_node.next

        if head1.data <= head2.data:
            temp.next = head1
            head1 = head1.next
        else:
            temp.next = head2
            head2 = head2.next

        temp = temp.next

    return dummy_node




if __name__ == "__main__":
    # Create linked list :
    # 10->20->30->40->50
    list1 = LinkedList()
    list1.append(10)
    list1.append(20)
    list1.append(30)
    list1.append(40)
    list1.append(50)

    list1.print_list()

    # Create linked list 2 :
    # 5->15->18->35->60
    list2 = LinkedList()
    list2.append(5)
    list2.append(15)
    list2.append(18)
    list2.append(35)
    list2.append(60)

    list2.print_list()

    # Create linked list 3
    list3 = LinkedList()

    list3.head = merge_list(list1.head, list2.head)
    print("------------------------------")
    list3.print_list()
