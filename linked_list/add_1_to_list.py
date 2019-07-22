# Add 1 to a number represented as linked list
# Number is represented in linked list such that each digit corresponds to a node
# in linked list. Add 1 to it. For example 1999 is represented as (1-> 9-> 9 -> 9)
# and adding 1 to it should change it to (2->0->0->0)
#
# Below are the steps :
#
# 1) Reverse given linked list. For example, 1-> 9-> 9 -> 9 is converted
#     to 9-> 9 -> 9 ->1.
# 2) Start traversing linked list from leftmost node and add 1 to it.
#     If there is a carry, move to the next node. Keep moving to the next node
#     while there is a carry.
# 3) Reverse modified linked list and return head.


class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            return None
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def reverse_list(self):
        if self.head is None:
            return None

        prev = None
        current = self.head

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def add_no_to_list_elements(self, n):
        if self.head is None:
            return None

        self.reverse_list()
        temp = self.head
        while temp:
            sum = temp.data + n
            carry = sum//10
            remainder = sum % 10
            print("Sum = {}, carry = {}".format(sum, carry))
            temp.data = remainder
            #exit(0)
            if carry > 0:
                temp = temp.next
            else:
                break
        self.reverse_list()

    def swap_list_in_group_of_given_size(self, head, k):
        cnt = 0
        tmp = head
        prev_elem = None
        first_prev = None
        while tmp is not None:
            cnt = cnt + 1
            if cnt == 1:
                first = tmp
                if first == head:
                    first_prev = None
                else:
                    first_prev = elem

            if tmp != head:
                prev_elem = elem
                # print("prev", prev_elem.data)
            elem = tmp
            # print(elem.data)

            if cnt == k:
                next_first = first.next
                next_elem = elem.next

                if first_prev is None:
                    tmp_head = elem
                    tmp_head.next = head.next

                if elem.next is not None:

                    prev_elem.next = first
                    tmp_head.next = first.next
                    first.next = next_elem
                    elem = first
                    tmp = first
                    if first_prev is not None:
                        first_prev.next = elem


                if elem.next is None:
                    elem.next = first.next
                    if first_prev is not None:
                        first_prev.next = elem
                    prev_elem.next = first
                    first.next = None


                cnt = 0
            tmp = tmp.next
        head = tmp_head
        return head

    def reverse_list_in_group_of_given_size(self, head, k):
        tmp = head
        count = 0
        next = None
        prev = None
        while tmp is not None and count < k:
            next = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = next
            count += 1

            if count == k:
                head.next = self.reverse_list_in_group_of_given_size(next, k)

        return prev




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

    list1.print_list()
    print("--------------")

    # list1.add_no_to_list_elements(1)
    # list1.print_list()

    list2 = LinkedList()
    list2.head = list1.reverse_list_in_group_of_given_size(list1.head, 10)
    list2.print_list()
