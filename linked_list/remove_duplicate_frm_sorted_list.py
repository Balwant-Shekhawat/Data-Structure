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

    def print_list(self):
        if self.head is None:
            return None

        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def remove_duplicate(self):
        if self.head is None:
            return None

        temp = self.head
        while temp.next:
            if temp.data == temp.next.data:
                new = temp.next.next
                # It deletes the variable
                temp.next = None
                temp.next = new
            else:
                temp = temp.next
        return self.head


if __name__ == "__main__":
    list1 = LinkedList()
    list1.append(11)
    list1.append(11)
    list1.append(11)
    list1.append(21)
    list1.append(43)
    list1.append(43)
    list1.append(60)

    list1.print_list()
    print("------------------------------")
    list1.remove_duplicate()
    list1.print_list()


