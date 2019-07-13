class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        # Initially setting heading as None because for empty LinkedList,
        # head points to NULL
        self.head = None

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
    obj.print_list()