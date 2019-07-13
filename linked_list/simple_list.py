class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        # Initially setting heading as None because for empty LinkedList,
        # head points to NULL
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

    def insert_at_beginning(self, item):
        obj = Node(item)
        obj.next = self.head
        self.head = obj

    def insert_at_end(self, item):
        obj = Node(item)
        temp = self.head
        # Here we will check if the next element is present or not in while loop,
        # If we write "while temp:" ,then it will execute till temp become None and
        # Property next of None cannot be accessed
        while temp.next:
            temp = temp.next
        temp.next = obj

    def insert_at_pos(self, item, pos):
        obj = Node(item)
        temp = self.head
        k = 1
        while temp:
            if k == pos:
                temp2 = temp.next
                temp.next = obj
                obj.next = temp2
            temp = temp.next
            k = k + 1

    def delete_a_node(self, item):
        temp = self.head

        while temp:
            prev = temp
            temp = temp.next
            if temp.data == item:
                prev.next = temp.next
                break

        if temp:
            temp = None

    def get_length_of_list(self):
        count = 0
        temp = self.head
        while temp:
            count = count + 1
            temp = temp.next
        return count

    def swap_nodes(self, pos1, pos2):
        temp = self.head
        i = 0
        k = 0
        node1 = None
        prev1 = None
        node2 = None
        prev2 = None
        while temp:

            if i == pos1:
                node1 = temp
                break
            prev1 = temp
            temp = temp.next
            i = i+1
        # print(prev1.data)
        # print(node1.data)
        temp2 = self.head
        while temp2:

            if k == pos2:
                node2 = temp2
                break
            prev2 = temp2
            temp2 = temp2.next
            k = k + 1

        # print(prev2.data)
        # print(node2.data)
        # If either node1 or node2 is not present, nothing to do
        if node1 is None or node2 is None:
            return

        # If node1 is not head of linked list, then prev1 should not be None
        if prev1 is not None:
            prev1.next = node2
        else:
            self.head = node2

        # If node2 is not head of linked list, then prev1 should not be None
        if prev2 is not None:
            prev2.next = node1
        else:
            self.head = node1

        # Swap the nodes
        prev2.next = node1
        tmp = node2.next
        node2.next = node1.next
        node1.next = tmp

    def reverse_list(self):
        prev = None
        current = self.head

        while current:
            next = current.next
            current.next = prev

            prev = current
            current = next
        self.head = prev


if __name__ == "__main__":

    obj = LinkedList()

    # Creating a linked list with 3 Nodes, But Initially the next pointers
    # of all nodes is NULL
    obj.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Connectin each Node of linked list with each other
    obj.head.next = second
    second.next = third

    #obj.print_list()

    # Insert 4 at the begginging of the linked list
    obj.insert_at_beginning(4)

    #obj.print_list()

    # Insert 5 at the end of the linked list
    obj.insert_at_end(5)

    #obj.print_list()

    # Insert 6 at the 2nd position of the linked list
    obj.insert_at_pos(6, 2)
    #obj.print_list()
    length1 = obj.get_length_of_list()
    print("length of list before deletion is {}".format(length1))

    # Delete 3 from the linked list
    obj.delete_a_node(3)
    obj.print_list()
    length2 = obj.get_length_of_list()
    print("length of list after deletion is {}".format(length2))

    # Swap 1 and 3 position
    obj.swap_nodes(1, 3)
    obj.print_list()
    print("-------------------------")

    # Reverse the list
    obj.reverse_list()
    obj.print_list()


